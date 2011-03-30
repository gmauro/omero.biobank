from wrapper import OmeroWrapper

import omero.rtypes as ort

import vl.lib.utils           as vlu
import vl.lib.utils.ome_utils as vluo

import bl.lib.sample.kb as kb

from sample import Sample
from sample import ContainerSlot
from samples_container import SamplesContainer
from study  import Study
from action import Action

import time


#----------------------------------------------------------------------
class ActionOnSample(Action, kb.ActionOnSample):

  OME_TABLE = "ActionOnSample"

  def __handle_validation_errors__(self):
    if self.target is None:
      raise kb.KBError("ActionOnSample target can't be None")
    else:
      super(ActionOnSample, self).__handle_validation_errors__()

  def __setattr__(self, name, value):
    if name == 'target':
      return setattr(self.ome_obj, name, value.ome_obj)
    else:
      return super(ActionOnSample, self).__setattr__(name, value)

  def __getattr__(self, name):
    if name == 'target':
      return Sample(self.ome_obj.device)
    else:
      return super(ActionOnSample, self).__getattr__(name)


#----------------------------------------------------------------------
class ActionOnContainer(Action, kb.ActionOnContainer):

  OME_TABLE = "ActionOnContainer"

  def __handle_validation_errors__(self):
    if self.target is None:
      raise kb.KBError("ActionOnContainer target can't be None")
    else:
      super(ActionOnContainer, self).__handle_validation_errors__()

  def __setattr__(self, name, value):
    if name == 'target':
      return setattr(self.ome_obj, name, value.ome_obj)
    else:
      return super(ActionOnContainer, self).__setattr__(name, value)

  def __getattr__(self, name):
    if name == 'target':
      return SamplesContainer(self.ome_obj.device)
    else:
      return super(ActionOnContainer, self).__getattr__(name)

#----------------------------------------------------------------------
class ActionOnSampleSlot(Action, kb.ActionOnSampleSlot):

  OME_TABLE = "ActionOnSampleSlot"

  def __handle_validation_errors__(self):
    if self.target is None:
      raise kb.KBError("ActionOnSampleSlot target can't be None")
    else:
      super(ActionOnSampleSlot, self).__handle_validation_errors__()

  def __setattr__(self, name, value):
    if name == 'target':
      return setattr(self.ome_obj, name, value.ome_obj)
    else:
      return super(ActionOnSampleSlot, self).__setattr__(name, value)

  def __getattr__(self, name):
    if name == 'target':
      return ContainerSlot(self.ome_obj.device)
    else:
      return super(ActionOnSampleSlot, self).__getattr__(name)


