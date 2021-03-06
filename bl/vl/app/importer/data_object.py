# BEGIN_COPYRIGHT
# END_COPYRIGHT

"""
Import data_object
==================

Will read in a tsv file with at least the following columns::

   path data_sample size sha1
   /share/fs/v039303.cel V02902 39090 SHA1SHA1
   ...

and will instantiate, for each row, a DataObject that represents a
physical instance of a given DataSample.

Records that point to an unknown data sample vid will be noisily
ignored. The same will happen to records that have the same path of a
previously seen data object.
"""

import os, csv, copy

from bl.vl.kb.mimetypes import DATA_OBJECT_FILES as SUPPORTED_MIME_TYPES
import core


class Recorder(core.Core):
  def __init__(self, study_label=None,
               host=None, user=None, passwd=None, keep_tokens=1,
               action_setup_conf=None,
               batch_size=1000, operator='Alfred E. Neumann',
               logger=None):
    super(Recorder, self).__init__(host, user, passwd, keep_tokens=keep_tokens,
                                   study_label=study_label, logger=logger)
    self.batch_size = batch_size
    self.operator = operator
    self.action_setup_conf = action_setup_conf
    self.preloaded_data_objects = {}
    self.preloaded_data_samples = {}

  def record(self, records, otsv, rtsv, blocking_validation):
    def records_by_chunk(batch_size, records):
      offset = 0
      while len(records[offset:]) > 0:
        yield records[offset:offset+batch_size]
        offset += batch_size
    if not records:
      msg = 'No records are going to be imported'
      self.logger.critical(msg)
      raise core.ImporterValidationError(msg)
    study = self.find_study(records)
    self.preload_data_samples()
    self.preload_data_objects()
    records, bad_records = self.do_consistency_checks(records)
    for br in bad_records:
      rtsv.writerow(br)
    if blocking_validation and len(bad_records) >= 1:
      raise core.ImporterValidationError('%d invalid records' % len(bad_records))
    for i, c in enumerate(records_by_chunk(self.batch_size, records)):
      self.logger.info('start processing chunk %d' % i)
      self.process_chunk(otsv, c, study)
      self.logger.info('done processing chunk %d' % i)

  def preload_data_samples(self):
    self.preload_by_type('data_sample', self.kb.DataSample,
                         self.preloaded_data_samples)

  def preload_data_objects(self):
    self.logger.info('start preloading data objects')
    ds = self.kb.get_objects(self.kb.DataObject)
    for d in ds:
      self.preloaded_data_objects[d.path] = d
    self.logger.info('there are %d DataObject(s) in the kb'
                     % (len(self.preloaded_data_objects)))

  def do_consistency_checks(self, records):
    self.logger.info('start consistency checks')
    good_records = []
    bad_records = []
    mandatory_fields = ['path', 'mimetype', 'size', 'sha1']
    for i, r in enumerate(records):
      reject = 'Rejecting import of record %d: ' % i
      if self.missing_fields(mandatory_fields, r):
        f = 'missing mandatory field'
        self.logger.error(reject + f)
        bad_rec = copy.deepcopy(r)
        bad_rec['error'] = f
        bad_records.append(bad_rec)
        continue
      if r['path'] in self.preloaded_data_objects:
        f = 'there is a pre-existing data_object with path %s' % r['path']
        self.logger.error(reject + f)
        bad_rec = copy.deepcopy(r)
        bad_rec['error'] = f
        bad_records.append(bad_rec)
        continue
      if not r['data_sample'] in self.preloaded_data_samples:
        f = 'there is no known data_sample with ID %s' % r['data_sample']
        self.logger.error(reject + f)
        bad_rec = copy.deepcopy(r)
        bad_rec['error'] =  f
        bad_records.append(bad_rec)
        continue
      if r['mimetype'] not in SUPPORTED_MIME_TYPES:
        f = 'unknown mimetype %s' % r['mimetype']
        self.logger.error(reject + f)
        bad_rec = copy.deepcopy(r)
        bad_rec['error'] = f
        bad_records.append(bad_rec)
        continue
      try:
        int(r['size'])
      except ValueError, ve:
        f = 'bad size value %s' % r['size']
        self.logger.error(reject + f)
        bad_rec = copy.deepcopy(r)
        bad_rec['error'] = f
        bad_records.append(bad_rec)
        continue
      good_records.append(r)
    self.logger.info('done consistency checks')
    return good_records, bad_records

  def process_chunk(self, otsv, chunk, study):
    data_objects = []
    for r in chunk:
      sample = self.preloaded_data_samples[r['data_sample']]
      conf = {
        'path': r['path'],
        'mimetype': r['mimetype'],
        'size': int(r['size']),
        'sample': sample,
        'sha1': r['sha1'],
        }
      data_objects.append(self.kb.factory.create(self.kb.DataObject, conf))
    self.kb.save_array(data_objects)
    for do in data_objects:
      otsv.writerow({
        'study': study.label,
        'path': do.path,
        'type': do.get_ome_table(),
        #'vid': do.id,
        })
      self.logger.info('saved %s[%s,%s] as attached to %s' %
                       (do.path, do.mimetype, do.size, do.sample.id))


def make_parser(parser):
  parser.add_argument('--study', metavar="STRING",
                      help="overrides the study column value")
  parser.add_argument('--mimetype', metavar="STRING",
                      choices=SUPPORTED_MIME_TYPES,
                      help="overrides the mimetype column value")


def implementation(logger, host, user, passwd, args, close_handles):
  action_setup_conf = Recorder.find_action_setup_conf(args)
  recorder = Recorder(args.study,
                      host=host, user=user, passwd=passwd,
                      operator=args.operator,
                      action_setup_conf=action_setup_conf,
                      logger=logger)
  f = csv.DictReader(args.ifile, delimiter='\t')
  logger.info('start processing file %s' % args.ifile.name)
  records = [r for r in f]
  canonizer = core.RecordCanonizer(['study', 'mimetype'], args)
  canonizer.canonize_list(records)
  o = csv.DictWriter(args.ofile,
                     fieldnames=['study', 'path', 'type'],
                     delimiter='\t', lineterminator=os.linesep)
  o.writeheader()
  report_fnames = copy.deepcopy(f.fieldnames)
  report_fnames.append('error')
  report = csv.DictWriter(args.report_file, report_fnames,
                          delimiter='\t', lineterminator=os.linesep,
                          extrasaction='ignore')
  report.writeheader()
  try:
    recorder.record(records, o, report,
                    args.blocking_validator)
  except core.ImporterValidationError as ve:
    logger.critical(ve.message)
    raise
  finally:
    close_handles(args)
  logger.info('done processing file %s' % args.ifile.name)


help_doc = """
import new data object definitions into the KB and link
them to previously registered data samples.
"""


def do_register(registration_list):
  registration_list.append(('data_object', help_doc, make_parser,
                            implementation))
