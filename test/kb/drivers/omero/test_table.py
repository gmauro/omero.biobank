# BEGIN_COPYRIGHT
# END_COPYRIGHT

import os, unittest, uuid
import itertools as it
import numpy as np

from bl.vl.kb.drivers.omero.proxy_core import ProxyCore


OME_HOST = os.getenv("OME_HOST", "localhost")
OME_USER = os.getenv("OME_USER", "root")
OME_PASS = os.getenv("OME_PASS", "romeo")

RES_SIZE = 256
VID_SIZE = 64
ARRAY_SIZE = 64

N_ROWS = 16


def get_random_table_name():
  return '%s.h5' % uuid.uuid4().hex


class TestProxyCore(unittest.TestCase):

  def __make_fields(self):
    fields =  [
      ('string', 'r_type', 'Result object type', RES_SIZE, None),
      ('string', 'r_vid', 'Result object VID', VID_SIZE, None),
      ('long', 'r_id', 'Result object ID', None ),
      ('string', 'o_vid', 'Action VID', VID_SIZE, None),
      ('string', 't_vid', 'Action target object VID', VID_SIZE, None),
      ('string', 'i_vid', 'Root tree VID', VID_SIZE, None),
      ('double_array', 'a_d_type', 'DoubleArray', ARRAY_SIZE),
      ('long_array', 'a_l_type', 'LongArray', ARRAY_SIZE),
      ]
    return fields

  def __fill_table(self, pc, table_name, n_rows):
    rec_desc = pc.get_table_headers(table_name)
    data = np.zeros(n_rows, dtype=rec_desc)
    data['r_id'] =  np.arange(n_rows)
    data['r_type'] = ['r_type%04d' % i for i in xrange(n_rows)]
    data['r_vid'] = ['r_vid%04d' % i for i in xrange(n_rows)]
    data['o_vid'] = ['o_vid%04d' % i for i in xrange(n_rows)]
    data['t_vid'] = ['t_vid%04d' % i for i in xrange(n_rows)]
    data['i_vid'] = ['i_vid%04d' % i for i in xrange(n_rows)]
    data['a_d_type'] = [np.random.random(ARRAY_SIZE) for i in xrange(n_rows)]
    data['a_l_type'] = [
      np.random.randint(0, 2**63-1, ARRAY_SIZE) for i in xrange(n_rows)
      ]
    pc.add_table_rows(table_name, data[:-1])
    pc.add_table_row(table_name, data[-1])
    return data

  def test_create_delete(self):
    fields = self.__make_fields()
    table_name = get_random_table_name()
    try:
      pc = ProxyCore(OME_HOST, OME_USER, OME_PASS)
      pc.create_table(table_name, fields)
      rec_desc = pc.get_table_headers(table_name)
      for f, n in it.izip(fields, rec_desc):
        self.assertEqual(f[1], n[0])
        if f[0] == 'string':
          self.assertEqual('|S%d' % f[3], n[1])
        elif f[0] == 'long':
          self.assertEqual('i8', n[1])
        elif f[0] == 'double_array':
          self.assertEqual('(%d,)float64' % f[3], n[1])
        elif f[0] == 'long_array':
          self.assertEqual('(%d,)int64' % f[3], n[1])
    finally:
      pc.delete_table(table_name)

  def test_table_rows(self):
    fields = self.__make_fields()
    table_name = get_random_table_name()
    try:
      pc = ProxyCore(OME_HOST, OME_USER, OME_PASS)
      pc.create_table(table_name, fields)
      data = self.__fill_table(pc, table_name, N_ROWS)
      rows = pc.get_table_rows(table_name, None)
    finally:
      pc.delete_table(table_name)
    self.assertTrue(np.all(data == rows))

  def test_table_rows_iterator(self):
    fields = self.__make_fields()
    table_name = get_random_table_name()
    try:
      pc = ProxyCore(OME_HOST, OME_USER, OME_PASS)
      pc.create_table(table_name, fields)
      data = self.__fill_table(pc, table_name, N_ROWS)
      row_it = pc.get_table_rows_iterator(table_name)
    finally:
      pc.delete_table(table_name)
    for i, row in enumerate(row_it):
      self.assertTrue(row == data[i])

  def test_update_row(self):
    fields = self.__make_fields()
    table_name = get_random_table_name()
    try:
      pc = ProxyCore(OME_HOST, OME_USER, OME_PASS)
      pc.create_table(table_name, fields)
      data = self.__fill_table(pc, table_name, N_ROWS)
      r = pc.get_table_rows(table_name, None)
      self.assertTrue(np.all(data == r))
      m = N_ROWS/2
      urow = data[m].copy()
      urow['o_vid'] = 'foo' + urow['o_vid']
      pc.update_table_row(
        table_name, '(r_vid == "%s")' % data[m]['r_vid'], urow
        )
      r = pc.get_table_rows(table_name, '(r_vid == "%s")' % data[m]['r_vid'])
    finally:
      pc.delete_table(table_name)
    self.assertEqual(len(r), 1)
    self.assertTrue(urow == r[0])

  def test_selections(self):
    fields = self.__make_fields()
    table_name = get_random_table_name()
    try:
      pc = ProxyCore(OME_HOST, OME_USER, OME_PASS)
      pc.create_table(table_name, fields)
      data = self.__fill_table(pc, table_name, N_ROWS)
      M = N_ROWS/2
      r = pc.get_table_rows(table_name, '(r_vid == "%s")' % data[M]['r_vid'])
      irange = xrange(N_ROWS/4, (3*N_ROWS)/4)
      selectors = ['(r_vid == "%s")' % data[i]['r_vid'] for i in irange]
      sel_classic = '|'.join(selectors)
      rows_classic = pc.get_table_rows(table_name, selector=sel_classic)
      sel_lite = selectors
      rows_lite = pc.get_table_rows(table_name, selector=sel_lite)
    finally:
      pc.delete_table(table_name)
    self.assertEqual(len(r), 1)
    self.assertTrue(data[M] == r[0])
    for i, r in it.izip(irange, rows_classic):
      self.assertTrue(data[i] == r)
    for i, r in it.izip(irange, rows_lite):
      self.assertTrue(data[i] == r)


def suite():
  suite = unittest.TestSuite()
  suite.addTest(TestProxyCore('test_create_delete'))
  suite.addTest(TestProxyCore('test_table_rows'))
  suite.addTest(TestProxyCore('test_table_rows_iterator'))
  suite.addTest(TestProxyCore('test_update_row'))
  suite.addTest(TestProxyCore('test_selections'))
  return suite


if __name__ == '__main__':
  runner = unittest.TextTestRunner(verbosity=2)
  runner.run((suite()))
