import omero.rtypes as ort

from bl.vl.sample.kb.drivers.omero.wrapper import OmeroWrapper
from bl.vl.sample.kb.drivers.omero.study import Study
import bl.vl.utils           as vlu
import bl.vl.utils.ome_utils as vluo

import bl.vl.individual.kb as kb

import time

from individual import Individual

class Enrollment(OmeroWrapper, kb.Enrollment):

  OME_TABLE = "Enrollment"

  def __setup__(self, ome_obj, study, individual, study_code):
    ome_obj.vid = ort.rstring(vlu.make_vid())
    ome_obj.study = study.ome_obj
    ome_obj.individual = individual.ome_obj
    ome_obj.studyCode = ort.rstring(study_code)
    ome_obj.stCodeUK = vluo.make_unique_key(study.id, study_code)
    ome_obj.stIndUK =  vluo.make_unique_key(study.id, individual.id)

  def __init__(self, from_=None, study=None, individual=None, study_code=None, **kw):
    ome_type = self.get_ome_type()
    if not from_ is None:
      ome_obj = from_
    else:
      if study is None or individual is None or  study_code is None:
        raise ValueError('Enrollment study, individual, study_code cannot be None')
      #FIXME
      assert isinstance(study, Study) and isinstance(individual, Individual)
      ome_obj = ome_type()
      self.__setup__(ome_obj, study, individual, study_code)
    super(Enrollment, self).__init__(ome_obj, **kw)

  def __handle_validation_errors__(self):
    if self.individual is None:
      raise kb.KBError("Enrollment individual can't be None")
    elif self.study is None:
      raise kb.KBError("Enrollment study can't be None")
    elif self.studyCode is None:
      raise kb.KBError("Enrollment studyCode can't be None")
    else:
      super(Enrollment, self).__handle_validation_errors__()

  def __setattr__(self, name, value):
    if name == 'individual':
      self.ome_obj.stIndUK = vluo.make_unique_key(self.study.id, value.id)
      return setattr(self.ome_obj, name, value.ome_obj)
    elif name == 'study':
      self.ome_obj.stCodeUK = vluo.make_unique_key(study.id, self.studyCode)
      self.ome_obj.stIndUK = vluo.make_unique_key(study.id, self.individual.id)
      return setattr(self.ome_obj, name, value.ome_obj)
    else:
      return super(Enrollment, self).__setattr__(name, value)

  def __getattr__(self, name):
    if name == 'individual':
      return Individual(self.ome_obj.individual, proxy=self.proxy)
    elif name == 'study':
      return Study(self.ome_obj.study, proxy=self.proxy)
    else:
      return super(Enrollment, self).__getattr__(name)

