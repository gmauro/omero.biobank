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
IceImport.load("omero_model_Event_ice")
from omero.rtypes import rlong
_omero = Ice.openModule("omero")
_omero_model = Ice.openModule("omero.model")
__name__ = "omero.model"
class EventI(_omero_model.Event):

      STATUS =  "ome.model.meta.Event_status"
      TIME =  "ome.model.meta.Event_time"
      EXPERIMENTER =  "ome.model.meta.Event_experimenter"
      EXPERIMENTERGROUP =  "ome.model.meta.Event_experimenterGroup"
      TYPE =  "ome.model.meta.Event_type"
      CONTAININGEVENT =  "ome.model.meta.Event_containingEvent"
      LOGS =  "ome.model.meta.Event_logs"
      SESSION =  "ome.model.meta.Event_session"
      DETAILS =  "ome.model.meta.Event_details"
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
          if load:
              self._logsSeq = []
              self._logsLoaded = True;
          else:
              self._logsSeq = []
              self._logsLoaded = False;

          pass

      def __init__(self, id = None, loaded = True):
          super(EventI, self).__init__()
          # Relying on omero.rtypes.rlong's error-handling
          self._id = rlong(id)
          self._loaded = loaded
          if self._loaded:
             self._details = _omero_model.DetailsI()
             self._toggleCollectionsLoaded(True)

      def unload(self, current = None):
          self._loaded = False
          self.unloadStatus( )
          self.unloadTime( )
          self.unloadExperimenter( )
          self.unloadExperimenterGroup( )
          self.unloadType( )
          self.unloadContainingEvent( )
          self.unloadLogs( )
          self.unloadSession( )
          self.unloadDetails( )

      def isLoaded(self, current = None):
          return self._loaded
      def unloadCollections(self, current = None):
          self._toggleCollectionsLoaded( False )
      def isGlobal(self, current = None):
          return  True ;
      def isMutable(self, current = None):
          return  False ;
      def isAnnotated(self, current = None):
          return  False ;
      def isLink(self, current = None):
          return  False ;
      def shallowCopy(self, current = None):
            if not self._loaded: return self.proxy()
            copy = EventI()
            copy._id = self._id;
            copy._details = None  # Unloading for the moment.
            raise omero.ClientError("NYI")
      def proxy(self, current = None):
          if self._id is None: raise omero.ClientError("Proxies require an id")
          return EventI( self._id.getValue(), False )

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

      def unloadTime(self, ):
          self._timeLoaded = False
          self._time = None;

      def getTime(self, current = None):
          self.errorIfUnloaded()
          return self._time

      def setTime(self, _time, current = None):
          self.errorIfUnloaded()
          self._time = _time
          pass

      def unloadExperimenter(self, ):
          self._experimenterLoaded = False
          self._experimenter = None;

      def getExperimenter(self, current = None):
          self.errorIfUnloaded()
          return self._experimenter

      def setExperimenter(self, _experimenter, current = None):
          self.errorIfUnloaded()
          self._experimenter = _experimenter
          pass

      def unloadExperimenterGroup(self, ):
          self._experimenterGroupLoaded = False
          self._experimenterGroup = None;

      def getExperimenterGroup(self, current = None):
          self.errorIfUnloaded()
          return self._experimenterGroup

      def setExperimenterGroup(self, _experimenterGroup, current = None):
          self.errorIfUnloaded()
          self._experimenterGroup = _experimenterGroup
          pass

      def unloadType(self, ):
          self._typeLoaded = False
          self._type = None;

      def getType(self, current = None):
          self.errorIfUnloaded()
          return self._type

      def setType(self, _type, current = None):
          self.errorIfUnloaded()
          self._type = _type
          pass

      def unloadContainingEvent(self, ):
          self._containingEventLoaded = False
          self._containingEvent = None;

      def getContainingEvent(self, current = None):
          self.errorIfUnloaded()
          return self._containingEvent

      def setContainingEvent(self, _containingEvent, current = None):
          self.errorIfUnloaded()
          self._containingEvent = _containingEvent
          pass

      def unloadLogs(self, current = None):
          self._logsLoaded = False
          self._logsSeq = None;

      def _getLogs(self, current = None):
          self.errorIfUnloaded()
          return self._logsSeq

      def _setLogs(self, _logs, current = None):
          self.errorIfUnloaded()
          self._logsSeq = _logs
          self.checkUnloadedProperty(_logs,'logsLoaded')

      def isLogsLoaded(self):
          return self._logsLoaded

      def sizeOfLogs(self, current = None):
          self.errorIfUnloaded()
          if not self._logsLoaded: return -1
          return len(self._logsSeq)

      def copyLogs(self, current = None):
          self.errorIfUnloaded()
          if not self._logsLoaded: self.throwNullCollectionException("logsSeq")
          return list(self._logsSeq)

      def iterateLogs(self):
          self.errorIfUnloaded()
          if not self._logsLoaded: self.throwNullCollectionException("logsSeq")
          return iter(self._logsSeq)

      def addEventLog(self, target, current = None):
          self.errorIfUnloaded()
          if not self._logsLoaded: self.throwNullCollectionException("logsSeq")
          self._logsSeq.append( target );
          target.setEvent( self )

      def addAllEventLogSet(self, targets, current = None):
          self.errorIfUnloaded()
          if  not self._logsLoaded: self.throwNullCollectionException("logsSeq")
          self._logsSeq.extend( targets )
          for target in targets:
              target.setEvent( self )

      def removeEventLog(self, target, current = None):
          self.errorIfUnloaded()
          if not self._logsLoaded: self.throwNullCollectionException("logsSeq")
          self._logsSeq.remove( target )
          target.setEvent( None )

      def removeAllEventLogSet(self, targets, current = None):
          self.errorIfUnloaded()
          if not self._logsLoaded: self.throwNullCollectionException("logsSeq")
          for elt in targets:
              elt.setEvent( None )
              self._logsSeq.remove( elt )

      def clearLogs(self, current = None):
          self.errorIfUnloaded()
          if not self._logsLoaded: self.throwNullCollectionException("logsSeq")
          for elt in self._logsSeq:
              elt.setEvent( None )
          self._logsSeq = list()

      def reloadLogs(self, toCopy, current = None):
          self.errorIfUnloaded()
          if self._logsLoaded:
              raise omero.ClientError("Cannot reload active collection: logsSeq")
          if not toCopy:
              raise omero.ClientError("Argument cannot be null")
          if toCopy.getId().getValue() != self.getId().getValue():
             raise omero.ClientError("Argument must have the same id as this instance")
          copy = toCopy.copyLogs() # May also throw
          for elt in copy:
              elt.setEvent( self )
          self._logsSeq = copy
          toCopy.unloadLogs()
          self._logsLoaded = True

      def unloadSession(self, ):
          self._sessionLoaded = False
          self._session = None;

      def getSession(self, current = None):
          self.errorIfUnloaded()
          return self._session

      def setSession(self, _session, current = None):
          self.errorIfUnloaded()
          self._session = _session
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

_omero_model.EventI = EventI
