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
IceImport.load("omero_model_ChannelBinding_ice")
from omero.rtypes import rlong
_omero = Ice.openModule("omero")
_omero_model = Ice.openModule("omero.model")
__name__ = "omero.model"
class ChannelBindingI(_omero_model.ChannelBinding):

      RENDERINGDEF =  "ome.model.display.ChannelBinding_renderingDef"
      FAMILY =  "ome.model.display.ChannelBinding_family"
      COEFFICIENT =  "ome.model.display.ChannelBinding_coefficient"
      INPUTSTART =  "ome.model.display.ChannelBinding_inputStart"
      INPUTEND =  "ome.model.display.ChannelBinding_inputEnd"
      ACTIVE =  "ome.model.display.ChannelBinding_active"
      NOISEREDUCTION =  "ome.model.display.ChannelBinding_noiseReduction"
      RED =  "ome.model.display.ChannelBinding_red"
      GREEN =  "ome.model.display.ChannelBinding_green"
      BLUE =  "ome.model.display.ChannelBinding_blue"
      ALPHA =  "ome.model.display.ChannelBinding_alpha"
      DETAILS =  "ome.model.display.ChannelBinding_details"
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
          super(ChannelBindingI, self).__init__()
          # Relying on omero.rtypes.rlong's error-handling
          self._id = rlong(id)
          self._loaded = loaded
          if self._loaded:
             self._details = _omero_model.DetailsI()
             self._toggleCollectionsLoaded(True)

      def unload(self, current = None):
          self._loaded = False
          self.unloadRenderingDef( )
          self.unloadFamily( )
          self.unloadCoefficient( )
          self.unloadInputStart( )
          self.unloadInputEnd( )
          self.unloadActive( )
          self.unloadNoiseReduction( )
          self.unloadRed( )
          self.unloadGreen( )
          self.unloadBlue( )
          self.unloadAlpha( )
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
            copy = ChannelBindingI()
            copy._id = self._id;
            copy._version = self._version;
            copy._details = None  # Unloading for the moment.
            raise omero.ClientError("NYI")
      def proxy(self, current = None):
          if self._id is None: raise omero.ClientError("Proxies require an id")
          return ChannelBindingI( self._id.getValue(), False )

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

      def unloadRenderingDef(self, ):
          self._renderingDefLoaded = False
          self._renderingDef = None;

      def getRenderingDef(self, current = None):
          self.errorIfUnloaded()
          return self._renderingDef

      def setRenderingDef(self, _renderingDef, current = None):
          self.errorIfUnloaded()
          self._renderingDef = _renderingDef
          pass

      def unloadFamily(self, ):
          self._familyLoaded = False
          self._family = None;

      def getFamily(self, current = None):
          self.errorIfUnloaded()
          return self._family

      def setFamily(self, _family, current = None):
          self.errorIfUnloaded()
          self._family = _family
          pass

      def unloadCoefficient(self, ):
          self._coefficientLoaded = False
          self._coefficient = None;

      def getCoefficient(self, current = None):
          self.errorIfUnloaded()
          return self._coefficient

      def setCoefficient(self, _coefficient, current = None):
          self.errorIfUnloaded()
          self._coefficient = _coefficient
          pass

      def unloadInputStart(self, ):
          self._inputStartLoaded = False
          self._inputStart = None;

      def getInputStart(self, current = None):
          self.errorIfUnloaded()
          return self._inputStart

      def setInputStart(self, _inputStart, current = None):
          self.errorIfUnloaded()
          self._inputStart = _inputStart
          pass

      def unloadInputEnd(self, ):
          self._inputEndLoaded = False
          self._inputEnd = None;

      def getInputEnd(self, current = None):
          self.errorIfUnloaded()
          return self._inputEnd

      def setInputEnd(self, _inputEnd, current = None):
          self.errorIfUnloaded()
          self._inputEnd = _inputEnd
          pass

      def unloadActive(self, ):
          self._activeLoaded = False
          self._active = None;

      def getActive(self, current = None):
          self.errorIfUnloaded()
          return self._active

      def setActive(self, _active, current = None):
          self.errorIfUnloaded()
          self._active = _active
          pass

      def unloadNoiseReduction(self, ):
          self._noiseReductionLoaded = False
          self._noiseReduction = None;

      def getNoiseReduction(self, current = None):
          self.errorIfUnloaded()
          return self._noiseReduction

      def setNoiseReduction(self, _noiseReduction, current = None):
          self.errorIfUnloaded()
          self._noiseReduction = _noiseReduction
          pass

      def unloadRed(self, ):
          self._redLoaded = False
          self._red = None;

      def getRed(self, current = None):
          self.errorIfUnloaded()
          return self._red

      def setRed(self, _red, current = None):
          self.errorIfUnloaded()
          self._red = _red
          pass

      def unloadGreen(self, ):
          self._greenLoaded = False
          self._green = None;

      def getGreen(self, current = None):
          self.errorIfUnloaded()
          return self._green

      def setGreen(self, _green, current = None):
          self.errorIfUnloaded()
          self._green = _green
          pass

      def unloadBlue(self, ):
          self._blueLoaded = False
          self._blue = None;

      def getBlue(self, current = None):
          self.errorIfUnloaded()
          return self._blue

      def setBlue(self, _blue, current = None):
          self.errorIfUnloaded()
          self._blue = _blue
          pass

      def unloadAlpha(self, ):
          self._alphaLoaded = False
          self._alpha = None;

      def getAlpha(self, current = None):
          self.errorIfUnloaded()
          return self._alpha

      def setAlpha(self, _alpha, current = None):
          self.errorIfUnloaded()
          self._alpha = _alpha
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

_omero_model.ChannelBindingI = ChannelBindingI
