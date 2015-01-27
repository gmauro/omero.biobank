"""
   /*
   **   Generated by blitz/templates/resouces/combined.vm
   **
   **   Copyright 2007, 2008 Glencoe Software, Inc. All rights reserved.
   **   Use is subject to license terms supplied in LICENSE.txt
   **
   */
"""
import Ice
import IceImport
import omero
IceImport.load("omero_model_DetailsI")
IceImport.load("omero_model_ActionOnAction_ice")
from omero.rtypes import rlong
_omero = Ice.openModule("omero")
_omero_model = Ice.openModule("omero.model")
__name__ = "omero.model"
class ActionOnActionI(_omero_model.ActionOnAction):

      TARGET =  "ome.model.vl.ActionOnAction_target"
      VID =  "ome.model.vl.ActionOnAction_vid"
      BEGINTIME =  "ome.model.vl.ActionOnAction_beginTime"
      ENDTIME =  "ome.model.vl.ActionOnAction_endTime"
      SETUP =  "ome.model.vl.ActionOnAction_setup"
      DEVICE =  "ome.model.vl.ActionOnAction_device"
      ACTIONCATEGORY =  "ome.model.vl.ActionOnAction_actionCategory"
      OPERATOR =  "ome.model.vl.ActionOnAction_operator"
      CONTEXT =  "ome.model.vl.ActionOnAction_context"
      DESCRIPTION =  "ome.model.vl.ActionOnAction_description"
      DETAILS =  "ome.model.vl.ActionOnAction_details"
      def errorIfUnloaded(self):
          if not self._loaded:
              raise _omero.UnloadedEntityException("Object unloaded:"+str(self))

      def throwNullCollectionException(self,propertyName):
          raise _omero.UnloadedEntityException(""+
          "Error updating collection:" + propertyName +"\n"+
          "Collection is currently null. This can be seen\n" +
          "by testing \""+ propertyName +"Loaded\". This implies\n"+
          "that this collection was unloaded. Please refresh this object\n"+
          "in order to update this collection.\n")

      def _toggleCollectionsLoaded(self,load):
          pass

      def __init__(self, id = None, loaded = True):
          super(ActionOnActionI, self).__init__()
          # Relying on omero.rtypes.rlong's error-handling
          self._id = rlong(id)
          self._loaded = loaded
          if self._loaded:
             self._details = _omero_model.DetailsI()
             self._toggleCollectionsLoaded(True)

      def unload(self, current = None):
          self._loaded = False
          self.unloadTarget( )
          self.unloadVid( )
          self.unloadBeginTime( )
          self.unloadEndTime( )
          self.unloadSetup( )
          self.unloadDevice( )
          self.unloadActionCategory( )
          self.unloadOperator( )
          self.unloadContext( )
          self.unloadDescription( )
          self.unloadDetails( )

      def isLoaded(self, current = None):
          return self._loaded
      def unloadCollections(self, current = None):
          self._toggleCollectionsLoaded( False )
      def isGlobal(self, current = None):
          return  False ;
      def isMutable(self, current = None):
          return  True ;
      def isAnnotated(self, current = None):
          return  False ;
      def isLink(self, current = None):
          return  False ;
      def shallowCopy(self, current = None):
            if not self._loaded: return self.proxy()
            copy = ActionOnActionI()
            copy._id = self._id;
            copy._version = self._version;
            copy._details = None  # Unloading for the moment.
            raise omero.ClientError("NYI")
      def proxy(self, current = None):
          if self._id is None: raise omero.ClientError("Proxies require an id")
          return ActionOnActionI( self._id.getValue(), False )

      def getDetails(self, current = None):
          self.errorIfUnloaded()
          return self._details

      def unloadDetails(self, current = None):
          self._details = None

      def getId(self, current = None):
          return self._id

      def setId(self, _id, current = None):
          self._id = _id

      def checkUnloadedProperty(self, value, loadedField):
          if value == None:
              self.__dict__[loadedField] = False
          else:
              self.__dict__[loadedField] = True

      def getVersion(self, current = None):
          self.errorIfUnloaded()
          return self._version

      def setVersion(self, version, current = None):
          self.errorIfUnloaded()
          self._version = version

      def unloadTarget(self, ):
          self._targetLoaded = False
          self._target = None;

      def getTarget(self, current = None):
          self.errorIfUnloaded()
          return self._target

      def setTarget(self, _target, current = None):
          self.errorIfUnloaded()
          self._target = _target
          pass

      def unloadVid(self, ):
          self._vidLoaded = False
          self._vid = None;

      def getVid(self, current = None):
          self.errorIfUnloaded()
          return self._vid

      def setVid(self, _vid, current = None):
          self.errorIfUnloaded()
          self._vid = _vid
          pass

      def unloadBeginTime(self, ):
          self._beginTimeLoaded = False
          self._beginTime = None;

      def getBeginTime(self, current = None):
          self.errorIfUnloaded()
          return self._beginTime

      def setBeginTime(self, _beginTime, current = None):
          self.errorIfUnloaded()
          self._beginTime = _beginTime
          pass

      def unloadEndTime(self, ):
          self._endTimeLoaded = False
          self._endTime = None;

      def getEndTime(self, current = None):
          self.errorIfUnloaded()
          return self._endTime

      def setEndTime(self, _endTime, current = None):
          self.errorIfUnloaded()
          self._endTime = _endTime
          pass

      def unloadSetup(self, ):
          self._setupLoaded = False
          self._setup = None;

      def getSetup(self, current = None):
          self.errorIfUnloaded()
          return self._setup

      def setSetup(self, _setup, current = None):
          self.errorIfUnloaded()
          self._setup = _setup
          pass

      def unloadDevice(self, ):
          self._deviceLoaded = False
          self._device = None;

      def getDevice(self, current = None):
          self.errorIfUnloaded()
          return self._device

      def setDevice(self, _device, current = None):
          self.errorIfUnloaded()
          self._device = _device
          pass

      def unloadActionCategory(self, ):
          self._actionCategoryLoaded = False
          self._actionCategory = None;

      def getActionCategory(self, current = None):
          self.errorIfUnloaded()
          return self._actionCategory

      def setActionCategory(self, _actionCategory, current = None):
          self.errorIfUnloaded()
          self._actionCategory = _actionCategory
          pass

      def unloadOperator(self, ):
          self._operatorLoaded = False
          self._operator = None;

      def getOperator(self, current = None):
          self.errorIfUnloaded()
          return self._operator

      def setOperator(self, _operator, current = None):
          self.errorIfUnloaded()
          self._operator = _operator
          pass

      def unloadContext(self, ):
          self._contextLoaded = False
          self._context = None;

      def getContext(self, current = None):
          self.errorIfUnloaded()
          return self._context

      def setContext(self, _context, current = None):
          self.errorIfUnloaded()
          self._context = _context
          pass

      def unloadDescription(self, ):
          self._descriptionLoaded = False
          self._description = None;

      def getDescription(self, current = None):
          self.errorIfUnloaded()
          return self._description

      def setDescription(self, _description, current = None):
          self.errorIfUnloaded()
          self._description = _description
          pass


      def ice_postUnmarshal(self):
          """
          Provides additional initialization once all data loaded
          """
          pass # Currently unused


      def ice_preMarshal(self):
          """
          Provides additional validation before data is sent
          """
          pass # Currently unused

      def __getattr__(self, name):
          import __builtin__
          """
          Reroutes all access to object.field through object.getField() or object.isField()
          """
          field  = "_" + name
          capitalized = name[0].capitalize() + name[1:]
          getter = "get" + capitalized
          questn = "is" + capitalized
          try:
              self.__dict__[field]
              if hasattr(self, getter):
                  method = getattr(self, getter)
                  return method()
              elif hasattr(self, questn):
                  method = getattr(self, questn)
                  return method()
          except:
              pass
          raise AttributeError("'%s' object has no attribute '%s' or '%s'" % (self.__class__.__name__, getter, questn))

      def __setattr__(self, name, value):
          """
          Reroutes all access to object.field through object.getField(), with the caveat
          that all sets on variables starting with "_" are permitted directly.
          """
          if name.startswith("_"):
              self.__dict__[name] = value
              return
          else:
              field  = "_" + name
              setter = "set" + name[0].capitalize() + name[1:]
              if hasattr(self, field) and hasattr(self, setter):
                  method = getattr(self, setter)
                  return method(value)
          raise AttributeError("'%s' object has no attribute '%s'" % (self.__class__.__name__, setter))

_omero_model.ActionOnActionI = ActionOnActionI
