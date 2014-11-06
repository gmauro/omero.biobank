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
IceImport.load("omero_model_Tube_ice")
from omero.rtypes import rlong
_omero = Ice.openModule("omero")
_omero_model = Ice.openModule("omero.model")
__name__ = "omero.model"
class TubeI(_omero_model.Tube):

      LABEL =  "ome.model.vl.Tube_label"
      BARCODE =  "ome.model.vl.Tube_barcode"
      VID =  "ome.model.vl.Tube_vid"
      ACTIVATIONDATE =  "ome.model.vl.Tube_activationDate"
      DESTRUCTIONDATE =  "ome.model.vl.Tube_destructionDate"
      CURRENTVOLUME =  "ome.model.vl.Tube_currentVolume"
      INITIALVOLUME =  "ome.model.vl.Tube_initialVolume"
      CONTENT =  "ome.model.vl.Tube_content"
      STATUS =  "ome.model.vl.Tube_status"
      ACTION =  "ome.model.vl.Tube_action"
      LASTUPDATE =  "ome.model.vl.Tube_lastUpdate"
      DETAILS =  "ome.model.vl.Tube_details"
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
          super(TubeI, self).__init__()
          # Relying on omero.rtypes.rlong's error-handling
          self._id = rlong(id)
          self._loaded = loaded
          if self._loaded:
             self._details = _omero_model.DetailsI()
             self._toggleCollectionsLoaded(True)

      def unload(self, current = None):
          self._loaded = False
          self.unloadLabel( )
          self.unloadBarcode( )
          self.unloadVid( )
          self.unloadActivationDate( )
          self.unloadDestructionDate( )
          self.unloadCurrentVolume( )
          self.unloadInitialVolume( )
          self.unloadContent( )
          self.unloadStatus( )
          self.unloadAction( )
          self.unloadLastUpdate( )
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
            copy = TubeI()
            copy._id = self._id;
            copy._version = self._version;
            copy._details = None  # Unloading for the moment.
            raise omero.ClientError("NYI")
      def proxy(self, current = None):
          if self._id is None: raise omero.ClientError("Proxies require an id")
          return TubeI( self._id.getValue(), False )

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

      def unloadLabel(self, ):
          self._labelLoaded = False
          self._label = None;

      def getLabel(self, current = None):
          self.errorIfUnloaded()
          return self._label

      def setLabel(self, _label, current = None):
          self.errorIfUnloaded()
          self._label = _label
          pass

      def unloadBarcode(self, ):
          self._barcodeLoaded = False
          self._barcode = None;

      def getBarcode(self, current = None):
          self.errorIfUnloaded()
          return self._barcode

      def setBarcode(self, _barcode, current = None):
          self.errorIfUnloaded()
          self._barcode = _barcode
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

      def unloadActivationDate(self, ):
          self._activationDateLoaded = False
          self._activationDate = None;

      def getActivationDate(self, current = None):
          self.errorIfUnloaded()
          return self._activationDate

      def setActivationDate(self, _activationDate, current = None):
          self.errorIfUnloaded()
          self._activationDate = _activationDate
          pass

      def unloadDestructionDate(self, ):
          self._destructionDateLoaded = False
          self._destructionDate = None;

      def getDestructionDate(self, current = None):
          self.errorIfUnloaded()
          return self._destructionDate

      def setDestructionDate(self, _destructionDate, current = None):
          self.errorIfUnloaded()
          self._destructionDate = _destructionDate
          pass

      def unloadCurrentVolume(self, ):
          self._currentVolumeLoaded = False
          self._currentVolume = None;

      def getCurrentVolume(self, current = None):
          self.errorIfUnloaded()
          return self._currentVolume

      def setCurrentVolume(self, _currentVolume, current = None):
          self.errorIfUnloaded()
          self._currentVolume = _currentVolume
          pass

      def unloadInitialVolume(self, ):
          self._initialVolumeLoaded = False
          self._initialVolume = None;

      def getInitialVolume(self, current = None):
          self.errorIfUnloaded()
          return self._initialVolume

      def setInitialVolume(self, _initialVolume, current = None):
          self.errorIfUnloaded()
          self._initialVolume = _initialVolume
          pass

      def unloadContent(self, ):
          self._contentLoaded = False
          self._content = None;

      def getContent(self, current = None):
          self.errorIfUnloaded()
          return self._content

      def setContent(self, _content, current = None):
          self.errorIfUnloaded()
          self._content = _content
          pass

      def unloadStatus(self, ):
          self._statusLoaded = False
          self._status = None;

      def getStatus(self, current = None):
          self.errorIfUnloaded()
          return self._status

      def setStatus(self, _status, current = None):
          self.errorIfUnloaded()
          self._status = _status
          pass

      def unloadAction(self, ):
          self._actionLoaded = False
          self._action = None;

      def getAction(self, current = None):
          self.errorIfUnloaded()
          return self._action

      def setAction(self, _action, current = None):
          self.errorIfUnloaded()
          self._action = _action
          pass

      def unloadLastUpdate(self, ):
          self._lastUpdateLoaded = False
          self._lastUpdate = None;

      def getLastUpdate(self, current = None):
          self.errorIfUnloaded()
          return self._lastUpdate

      def setLastUpdate(self, _lastUpdate, current = None):
          self.errorIfUnloaded()
          self._lastUpdate = _lastUpdate
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

_omero_model.TubeI = TubeI
