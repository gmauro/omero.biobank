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
IceImport.load("omero_model_Reagent_ice")
from omero.rtypes import rlong
_omero = Ice.openModule("omero")
_omero_model = Ice.openModule("omero.model")
__name__ = "omero.model"
class ReagentI(_omero_model.Reagent):

      NAME =  "ome.model.screen.Reagent_name"
      REAGENTIDENTIFIER =  "ome.model.screen.Reagent_reagentIdentifier"
      SCREEN =  "ome.model.screen.Reagent_screen"
      WELLLINKS =  "ome.model.screen.Reagent_wellLinks"
      ANNOTATIONLINKS =  "ome.model.screen.Reagent_annotationLinks"
      DESCRIPTION =  "ome.model.screen.Reagent_description"
      DETAILS =  "ome.model.screen.Reagent_details"
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
              self._wellLinksSeq = []
              self._wellLinksLoaded = True;
          else:
              self._wellLinksSeq = []
              self._wellLinksLoaded = False;

          if load:
              self._annotationLinksSeq = []
              self._annotationLinksLoaded = True;
          else:
              self._annotationLinksSeq = []
              self._annotationLinksLoaded = False;

          pass

      def __init__(self, id = None, loaded = True):
          super(ReagentI, self).__init__()
          # Relying on omero.rtypes.rlong's error-handling
          self._id = rlong(id)
          self._loaded = loaded
          if self._loaded:
             self._details = _omero_model.DetailsI()
             self._toggleCollectionsLoaded(True)

      def unload(self, current = None):
          self._loaded = False
          self.unloadName( )
          self.unloadReagentIdentifier( )
          self.unloadScreen( )
          self.unloadWellLinks( )
          self.unloadAnnotationLinks( )
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
          return  True ;
      def isLink(self, current = None):
          return  False ;
      def shallowCopy(self, current = None):
            if not self._loaded: return self.proxy()
            copy = ReagentI()
            copy._id = self._id;
            copy._version = self._version;
            copy._details = None  # Unloading for the moment.
            raise omero.ClientError("NYI")
      def proxy(self, current = None):
          if self._id is None: raise omero.ClientError("Proxies require an id")
          return ReagentI( self._id.getValue(), False )

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

      def unloadName(self, ):
          self._nameLoaded = False
          self._name = None;

      def getName(self, current = None):
          self.errorIfUnloaded()
          return self._name

      def setName(self, _name, current = None):
          self.errorIfUnloaded()
          self._name = _name
          pass

      def unloadReagentIdentifier(self, ):
          self._reagentIdentifierLoaded = False
          self._reagentIdentifier = None;

      def getReagentIdentifier(self, current = None):
          self.errorIfUnloaded()
          return self._reagentIdentifier

      def setReagentIdentifier(self, _reagentIdentifier, current = None):
          self.errorIfUnloaded()
          self._reagentIdentifier = _reagentIdentifier
          pass

      def unloadScreen(self, ):
          self._screenLoaded = False
          self._screen = None;

      def getScreen(self, current = None):
          self.errorIfUnloaded()
          return self._screen

      def setScreen(self, _screen, current = None):
          self.errorIfUnloaded()
          self._screen = _screen
          pass

      def unloadWellLinks(self, current = None):
          self._wellLinksLoaded = False
          self._wellLinksSeq = None;

      def _getWellLinks(self, current = None):
          self.errorIfUnloaded()
          return self._wellLinksSeq

      def _setWellLinks(self, _wellLinks, current = None):
          self.errorIfUnloaded()
          self._wellLinksSeq = _wellLinks
          self.checkUnloadedProperty(_wellLinks,'wellLinksLoaded')

      def isWellLinksLoaded(self):
          return self._wellLinksLoaded

      def sizeOfWellLinks(self, current = None):
          self.errorIfUnloaded()
          if not self._wellLinksLoaded: return -1
          return len(self._wellLinksSeq)

      def copyWellLinks(self, current = None):
          self.errorIfUnloaded()
          if not self._wellLinksLoaded: self.throwNullCollectionException("wellLinksSeq")
          return list(self._wellLinksSeq)

      def iterateWellLinks(self):
          self.errorIfUnloaded()
          if not self._wellLinksLoaded: self.throwNullCollectionException("wellLinksSeq")
          return iter(self._wellLinksSeq)

      def addWellReagentLink(self, target, current = None):
          self.errorIfUnloaded()
          if not self._wellLinksLoaded: self.throwNullCollectionException("wellLinksSeq")
          self._wellLinksSeq.append( target );
          target.setChild( self )

      def addAllWellReagentLinkSet(self, targets, current = None):
          self.errorIfUnloaded()
          if  not self._wellLinksLoaded: self.throwNullCollectionException("wellLinksSeq")
          self._wellLinksSeq.extend( targets )
          for target in targets:
              target.setChild( self )

      def removeWellReagentLink(self, target, current = None):
          self.errorIfUnloaded()
          if not self._wellLinksLoaded: self.throwNullCollectionException("wellLinksSeq")
          self._wellLinksSeq.remove( target )
          target.setChild( None )

      def removeAllWellReagentLinkSet(self, targets, current = None):
          self.errorIfUnloaded()
          if not self._wellLinksLoaded: self.throwNullCollectionException("wellLinksSeq")
          for elt in targets:
              elt.setChild( None )
              self._wellLinksSeq.remove( elt )

      def clearWellLinks(self, current = None):
          self.errorIfUnloaded()
          if not self._wellLinksLoaded: self.throwNullCollectionException("wellLinksSeq")
          for elt in self._wellLinksSeq:
              elt.setChild( None )
          self._wellLinksSeq = list()

      def reloadWellLinks(self, toCopy, current = None):
          self.errorIfUnloaded()
          if self._wellLinksLoaded:
              raise omero.ClientError("Cannot reload active collection: wellLinksSeq")
          if not toCopy:
              raise omero.ClientError("Argument cannot be null")
          if toCopy.getId().getValue() != self.getId().getValue():
             raise omero.ClientError("Argument must have the same id as this instance")
          if toCopy.getDetails().getUpdateEvent().getId().getValue() < self.getDetails().getUpdateEvent().getId().getValue():
             raise omero.ClientError("Argument may not be older than this instance")
          copy = toCopy.copyWellLinks() # May also throw
          for elt in copy:
              elt.setChild( self )
          self._wellLinksSeq = copy
          toCopy.unloadWellLinks()
          self._wellLinksLoaded = True

      def getWellLinksCountPerOwner(self, current = None):
          return self._wellLinksCountPerOwner

      def linkWell(self, addition, current = None):
          self.errorIfUnloaded()
          if not self._wellLinksLoaded: self.throwNullCollectionException("wellLinksSeq")
          link = _omero_model.WellReagentLinkI()
          link.link( addition, self );
          self.addWellReagentLinkToBoth( link, True )
          return link

      def addWellReagentLinkToBoth(self, link, bothSides):
          self.errorIfUnloaded()
          if not self._wellLinksLoaded: self.throwNullCollectionException("wellLinksSeq")
          self._wellLinksSeq.append( link )
          if bothSides and link.getParent().isLoaded():
              link.getParent().addWellReagentLinkToBoth( link, False )

      def findWellReagentLink(self, removal, current = None):
          self.errorIfUnloaded()
          if not self._wellLinksLoaded: self.throwNullCollectionException("wellLinksSeq")
          result = list()
          for link in self._wellLinksSeq:
              if link.getParent() == removal: result.append(link)
          return result

      def unlinkWell(self, removal, current = None):
          self.errorIfUnloaded()
          if not self._wellLinksLoaded: self.throwNullCollectionException("wellLinksSeq")
          toRemove = self.findWellReagentLink(removal)
          for next in toRemove:
              self.removeWellReagentLinkFromBoth( next, True )

      def removeWellReagentLinkFromBoth(self, link, bothSides, current = None):
          self.errorIfUnloaded()
          if not self._wellLinksLoaded: self.throwNullCollectionException("wellLinksSeq")
          self._wellLinksSeq.remove( link )
          if bothSides and link.getParent().isLoaded():
              link.getParent().removeWellReagentLinkFromBoth(link, False)

      def linkedWellList(self, current = None):
          self.errorIfUnloaded()
          if not self.wellLinksLoaded: self.throwNullCollectionException("WellLinks")
          linked = []
          for link in self._wellLinksSeq:
              linked.append( link.getParent() )
          return linked

      def unloadAnnotationLinks(self, current = None):
          self._annotationLinksLoaded = False
          self._annotationLinksSeq = None;

      def _getAnnotationLinks(self, current = None):
          self.errorIfUnloaded()
          return self._annotationLinksSeq

      def _setAnnotationLinks(self, _annotationLinks, current = None):
          self.errorIfUnloaded()
          self._annotationLinksSeq = _annotationLinks
          self.checkUnloadedProperty(_annotationLinks,'annotationLinksLoaded')

      def isAnnotationLinksLoaded(self):
          return self._annotationLinksLoaded

      def sizeOfAnnotationLinks(self, current = None):
          self.errorIfUnloaded()
          if not self._annotationLinksLoaded: return -1
          return len(self._annotationLinksSeq)

      def copyAnnotationLinks(self, current = None):
          self.errorIfUnloaded()
          if not self._annotationLinksLoaded: self.throwNullCollectionException("annotationLinksSeq")
          return list(self._annotationLinksSeq)

      def iterateAnnotationLinks(self):
          self.errorIfUnloaded()
          if not self._annotationLinksLoaded: self.throwNullCollectionException("annotationLinksSeq")
          return iter(self._annotationLinksSeq)

      def addReagentAnnotationLink(self, target, current = None):
          self.errorIfUnloaded()
          if not self._annotationLinksLoaded: self.throwNullCollectionException("annotationLinksSeq")
          self._annotationLinksSeq.append( target );
          target.setParent( self )

      def addAllReagentAnnotationLinkSet(self, targets, current = None):
          self.errorIfUnloaded()
          if  not self._annotationLinksLoaded: self.throwNullCollectionException("annotationLinksSeq")
          self._annotationLinksSeq.extend( targets )
          for target in targets:
              target.setParent( self )

      def removeReagentAnnotationLink(self, target, current = None):
          self.errorIfUnloaded()
          if not self._annotationLinksLoaded: self.throwNullCollectionException("annotationLinksSeq")
          self._annotationLinksSeq.remove( target )
          target.setParent( None )

      def removeAllReagentAnnotationLinkSet(self, targets, current = None):
          self.errorIfUnloaded()
          if not self._annotationLinksLoaded: self.throwNullCollectionException("annotationLinksSeq")
          for elt in targets:
              elt.setParent( None )
              self._annotationLinksSeq.remove( elt )

      def clearAnnotationLinks(self, current = None):
          self.errorIfUnloaded()
          if not self._annotationLinksLoaded: self.throwNullCollectionException("annotationLinksSeq")
          for elt in self._annotationLinksSeq:
              elt.setParent( None )
          self._annotationLinksSeq = list()

      def reloadAnnotationLinks(self, toCopy, current = None):
          self.errorIfUnloaded()
          if self._annotationLinksLoaded:
              raise omero.ClientError("Cannot reload active collection: annotationLinksSeq")
          if not toCopy:
              raise omero.ClientError("Argument cannot be null")
          if toCopy.getId().getValue() != self.getId().getValue():
             raise omero.ClientError("Argument must have the same id as this instance")
          if toCopy.getDetails().getUpdateEvent().getId().getValue() < self.getDetails().getUpdateEvent().getId().getValue():
             raise omero.ClientError("Argument may not be older than this instance")
          copy = toCopy.copyAnnotationLinks() # May also throw
          for elt in copy:
              elt.setParent( self )
          self._annotationLinksSeq = copy
          toCopy.unloadAnnotationLinks()
          self._annotationLinksLoaded = True

      def getAnnotationLinksCountPerOwner(self, current = None):
          return self._annotationLinksCountPerOwner

      def linkAnnotation(self, addition, current = None):
          self.errorIfUnloaded()
          if not self._annotationLinksLoaded: self.throwNullCollectionException("annotationLinksSeq")
          link = _omero_model.ReagentAnnotationLinkI()
          link.link( self, addition );
          self.addReagentAnnotationLinkToBoth( link, True )
          return link

      def addReagentAnnotationLinkToBoth(self, link, bothSides):
          self.errorIfUnloaded()
          if not self._annotationLinksLoaded: self.throwNullCollectionException("annotationLinksSeq")
          self._annotationLinksSeq.append( link )

      def findReagentAnnotationLink(self, removal, current = None):
          self.errorIfUnloaded()
          if not self._annotationLinksLoaded: self.throwNullCollectionException("annotationLinksSeq")
          result = list()
          for link in self._annotationLinksSeq:
              if link.getChild() == removal: result.append(link)
          return result

      def unlinkAnnotation(self, removal, current = None):
          self.errorIfUnloaded()
          if not self._annotationLinksLoaded: self.throwNullCollectionException("annotationLinksSeq")
          toRemove = self.findReagentAnnotationLink(removal)
          for next in toRemove:
              self.removeReagentAnnotationLinkFromBoth( next, True )

      def removeReagentAnnotationLinkFromBoth(self, link, bothSides, current = None):
          self.errorIfUnloaded()
          if not self._annotationLinksLoaded: self.throwNullCollectionException("annotationLinksSeq")
          self._annotationLinksSeq.remove( link )

      def linkedAnnotationList(self, current = None):
          self.errorIfUnloaded()
          if not self.annotationLinksLoaded: self.throwNullCollectionException("AnnotationLinks")
          linked = []
          for link in self._annotationLinksSeq:
              linked.append( link.getChild() )
          return linked

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

_omero_model.ReagentI = ReagentI
