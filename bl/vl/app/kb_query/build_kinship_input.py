"""
This script generates the input file for the hadoop version of the
kinship algorithm.
The output file will be like

AA AB NN BB AB
BB NN AA AA AB
AA AA BB BB AB
...

* each colum represents a single data sample
* each row represents a specific SNP

NOTE WELL: if the output file is too big to be handled with the RAM of
the computer that runs this script, the file can be written as the
transposed version of the output format described above (each row will
represent a data sample and each column a SNP) and transposed using a
specific map-reduce job.

"""

import os, argparse, csv, logging, bz2
import numpy as np

from bl.vl.app.importer.core import Core
from bl.vl.genotype.algo import project_to_discrete_genotype


LOG_FORMAT = '%(asctime)s|%(levelname)-8s|%(message)s'
LOG_DATEFMT = '%Y-%m-%d %H:%M:%S'
LOG_LEVELS = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']


class KinshipWriter(object):
    """
    TODO: write something....
    """
    def __init__(self, mset, genotypes_out_file, samples_list_out_file,
                 transpose_output = False, ignore_duplicated = False):
        self.mset = mset
        self.out_k_file = genotypes_out_file
        self.out_ds_file = samples_list_out_file
        self.out_k_csvw = csv.writer(self.out_k_file, delimiter='\t')
        self.out_ds_csvw = csv.writer(self.out_ds_file, delimiter='\t')
        self.tro = transpose_output
        self.igd = ignore_duplicated
        self.out_data = []
        self.kb = self.mset.proxy

    def write_record(self, individual, data_collection_samples = None):
        """
        TODO: doc here...
        """
        allele_patterns = {0: 'AA', 1: 'BB', 2:'AB', 3: 'NN'}
        dsamples = self.kb.get_data_samples(individual, 'GenotypeDataSample')
        # First of all, filter by marker set
        dsamples = [d for d in dsamples if d.snpMarkersSet == self.mset]
        # If data_collection_items list has been provided, keep only
        # data samples that belongs to this list
        if data_collection_samples:
            dsamples = [d for d in dsamples if d in data_collection_samples]
        if len(dsamples) > 0:
            if self.igd:
                dsamples = dsamples[:1]
            for ds in dsamples:
                probs, _ = ds.resolve_to_data()
                if probs is not None:
                    self.out_ds_csvw.writerow([ds.id])
                    disc_probs = [allele_patterns[x]
                                  for x in project_to_discrete_genotype(probs)]
                    if self.tro:
                        self.out_k_csvw.writerow(disc_probs)
                    else:
                        self.out_data.append(disc_probs)
        
    def close(self):
        """
        TODO: doc here
        """
        if len(self.out_data) > 0:
            self.out_data = np.array(self.out_data).transpose()
            for d in self.out_data:
                self.out_k_csvw.writerow(d)
        self.out_k_file.close()
        self.out_ds_file.close()
        

class KinshipInputWriterApp(Core):
    def __init__(self, host = None, user = None, passwd = None, keep_tokens = 1,
                 logger = None, study_label = None, operator = 'Alfred E. Neumann'):
        super(KinshipInputWriterApp, self).__init__(host, user, passwd, keep_tokens=keep_tokens,
                                                    study_label=study_label, logger=logger)

    def dump(self, genotypes_out_file, samples_list_out_file, marker_set_label,
             data_collection_label = None, transpose_output = False, 
             ignore_duplicated = False, enable_compression = False,
             compression_level = None):
        self.logger.info('Loading individuals from study %s' % self.default_study.label)
        inds = [en.individual
                for en in self.kb.get_enrolled(self.default_study)]
        self.logger.info('Loaded %d individuals' % len(inds))

        self.logger.info('Loading marker set %s' % marker_set_label)
        mset = self.kb.get_snp_markers_set(marker_set_label)

        if data_collection_label:
            self.logger.info('Loading elements from data collection %s' % data_collection_label)
            dcoll = self.kb.get_data_collection(data_collection_label)
            dc_samples = [dci.dataSample
                          for dci in self.kb.get_data_collection_items(dcoll)]
            self.logger.info('Loaded %d elements' % len(dc_samples))
        else:
            dc_samples = None

        self.logger.info('Initializing writer')
        
        if enable_compression:
            genotypes_out_file.close()
            genotypes_out_file = bz2.BZ2File(os.path.abspath(genotypes_out_file.name),
                                             'w', compression_level)
        kw_args = {'mset' : mset,
                   'transpose_output' : transpose_output,
                   'ignore_duplicated' : ignore_duplicated,
                   'genotypes_out_file' : genotypes_out_file,
                   'samples_list_out_file' : samples_list_out_file}
        kinship_writer = KinshipWriter(**kw_args)

        self.logger.info('Writing records')
        for ind in inds:
            self.logger.debug('Writing record for individual %s (%d/%d)' % (ind.id,
                                                                            inds.index(ind) + 1,
                                                                            len(inds)))
            kinship_writer.write_record(ind, dc_samples)

        self.logger.info('Closing writer')
        kinship_writer.close()
        self.logger.info('Job complete')
                              
help_doc = """
Write input files that can be used to generate a kinship matrix using
individuals related to a specific study
"""

def make_parser(parser):
    parser.add_argument('--out_samples_list', type = argparse.FileType('w'),
                        help = 'output files with samples VID', required = True)
    parser.add_argument('--study', type = str, help = 'study label',
                        required = True)
    parser.add_argument('--marker_set', type = str, help = 'marker set label',
                        required = True)
    parser.add_argument('--data_collection', type = str, help = 'data collection label',
                        default = None)
    parser.add_argument('--transpose_output', action = 'store_true',
                        help = 'write the transposed version of the standard output')
    parser.add_argument('--ignore_duplicated', action='store_true',
                        help = 'if more than one data sample is connected to an indiviudal use only the first one')
    parser.add_argument('--compress_output', action = 'store_true',
                        help = 'write output files in compressed bzip2 format')
    parser.add_argument('--compression_level', type = int, choices = range(1,10),
                        help = 'compression level (read python bz2 documentation for legal values)',
                        default = 5)

def implementation(logger, host, user, passwd, args):
    app = KinshipInputWriterApp(host = host, user = user, passwd = passwd,
                                keep_tokens = args.keep_tokens, logger = logger,
                                study_label = args.study)
    app.dump(args.ofile, args.out_samples_list, args.marker_set, args.data_collection,
             args.transpose_output, args.ignore_duplicated, args.compress_output,
             args.compression_level)

def do_register(registration_list):
    registration_list.append(('kinship_input', help_doc, make_parser, implementation))
