# pylint: disable=E1103

# BEGIN_COPYRIGHT
# END_COPYRIGHT

import os, unittest, logging
import itertools as it
import numpy as np
logging.basicConfig(level=logging.ERROR)

from bl.vl.kb import KnowledgeBase as KB
from kb_object_creator import KBObjectCreator

import bl.vl.utils as vlu
VID_SIZE = vlu.DEFAULT_VID_LEN


OME_HOST = os.getenv("OME_HOST", "localhost")
OME_USER = os.getenv("OME_USER", "root")
OME_PASS = os.getenv("OME_PASS", "romeo")




class TestVCS(KBObjectCreator):

    def __init__(self, name):
        super(TestVCS, self).__init__(name)
        self.kill_list = []

    def create_reference_genome(self, action):
        conf = {'nChroms' : 10, 
                'maker': vlu.make_random_str(),
                'model': vlu.make_random_str(),
                'release' : vlu.make_random_str(),
                'label': vlu.make_random_str(),
                'status' : self.kb.DataSampleStatus.USABLE,
                'action': action}
        reference_genome = self.kb.factory.create(self.kb.ReferenceGenome,
                                                  conf).save()
        self.kill_list.append(reference_genome)
        return reference_genome

    def create_action(self):
        _, action = super(TestVCS, self).create_action()
        action = action.save()
        self.kill_list.append(action)
        return action

    def setUp(self):
        self.kb = KB(driver='omero')(OME_HOST, OME_USER, OME_PASS)

    def tearDown(self):
        while self.kill_list:
            self.kb.delete(self.kill_list.pop())

    def test_save_restore(self):
        VariantCallSupport = self.kb.VariantCallSupport
        nodes = np.array([(1, 1), (1, 2), (1, 3), (2, 1), (2, 3)], 
                        dtype=VariantCallSupport.NODES_DTYPE)
        field = np.array([(i, 'V%06d' % i, i) for i in range(len(nodes))],
                         dtype=[('index', '<i4'), 
                                ('source', '|S%d' % VID_SIZE), ('pos', '<i4')])
        action = self.create_action()
        reference_genome = self.create_reference_genome(action)
        label = vlu.make_random_str()
        conf = {'referenceGenome' : reference_genome,
                'label' : label,
                'status' : self.kb.DataSampleStatus.USABLE,
                'action': action}  
        vcs = self.kb.factory.create(VariantCallSupport, conf)
        vcs.define_support(nodes)
        vcs.define_field('origin', field)
        #self.kb.genomics.register_vcs(vcs)
        vcs.save()
        self.kill_list.append(vcs)
        dos = self.kb.get_objects(vcs)
        self.assertEqual(len(dos), 1)
        self.kb.del_from_cache(vcs.ome_obj) # do not do this at home.
        vcs2 = self.kb.genomics.get_vcs_by_label(label)
        self.assertTrue(np.alltrue(vcs2.get_nodes() == vcs.get_nodes()))
        o1 = vcs.get_field('origin') 
        o2 = vcs2.get_field('origin')
        for a, b in it.izip(o1, o2):
            for x, y in it.izip(a, b):
                self.assertEqual(x, y)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestVCS('test_save_restore'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run((suite()))
