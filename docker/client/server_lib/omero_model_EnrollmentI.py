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
IceImport.load("omero_model_Enrollment_ice")
from omero.rtypes import rlong
_omero = Ice.openModule("omero")
_omero_model = Ice.openModule("omero.model")
__name__ = "omero.model"
class EnrollmentI(_omero_model.Enrollment):

      VID =  "ome.model.vl.Enrollment_vid"
      INDIVIDUAL =  "ome.model.vl.Enrollment_individual"
      STUDY =  "ome.model.vl.Enrollment_study"
      STUDYCODE =  "ome.model.vl.Enrollment_studyCode"
      STCODEUK =  "ome.model.vl.Enrollment_stCodeUK"
      STINDUK =  "ome.model.vl.Enrollment_stIndUK"
      DETAILS =  "ome.model.vl.Enrollment_details"
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
          super(EnrollmentI, self).__init__()
          # Relying on omero.rtypes.rlong's error-handling
          self._id = rlong(id)
          self._loaded = loaded
          if self._loaded:
             self._details = _omero_model.DetailsI()
             self._toggleCollectionsLoaded(True)

      def unload(self, current = None):
          self._loaded = False
          self.unloadVid( )
          self.unloadIndividual( )
          self.unloadStudy( )
          self.unloadStudyCode( )
          self.unloadStCodeUK( )
          self.unloadStIndUK( )
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
            copy = EnrollmentI()
            copy._id = self._id;
            copy._version = self._version;
            copy._details = None  # Unloading for the moment.
            raise omero.ClientError("NYI")
      def proxy(self, current = None):
          if self._id is None: raise omero.ClientError("Proxies require an id")
          return EnrollmentI( self._id.getValue(), False )

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

      def unloadIndividual(self, ):
          self._individualLoaded = False
          self._individual = None;

      def getIndividual(self, current = None):
          self.errorIfUnloaded()
          return self._individual

      def setIndividual(self, _individual, current = None):
          self.errorIfUnloaded()
          self._individual = _individual
          pass

      def unloadStudy(self, ):
          self._studyLoaded = False
          self._study = None;

      def getStudy(self, current = None):
          self.errorIfUnloaded()
          return self._study

      def setStudy(self, _study, current = None):
          self.errorIfUnloaded()
          self._study = _study
          pass

      def unloadStudyCode(self, ):
          self._studyCodeLoaded = False
          self._studyCode = None;

      def getStudyCode(self, current = None):
          self.errorIfUnloaded()
          return self._studyCode

      def setStudyCode(self, _studyCode, current = None):
          self.errorIfUnloaded()
          self._studyCode = _studyCode
          pass

      def unloadStCodeUK(self, ):
          self._stCodeUKLoaded = False
          self._stCodeUK = None;

      def getStCodeUK(self, current = None):
          self.errorIfUnloaded()
          return self._stCodeUK

      def setStCodeUK(self, _stCodeUK, current = None):
          self.errorIfUnloaded()
          self._stCodeUK = _stCodeUK
          pass

      def unloadStIndUK(self, ):
          self._stIndUKLoaded = False
          self._stIndUK = None;

      def getStIndUK(self, current = None):
          self.errorIfUnloaded()
          return self._stIndUK

      def setStIndUK(self, _stIndUK, current = None):
          self.errorIfUnloaded()
          self._stIndUK = _stIndUK
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

_omero_model.EnrollmentI = EnrollmentI
