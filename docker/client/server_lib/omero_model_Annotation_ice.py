# **********************************************************************
#
# Copyright (c) 2003-2011 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************
#
# Ice version 3.4.2
#
# <auto-generated>
#
# Generated from file `Annotation.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

import Ice, IcePy, __builtin__
import omero_model_IObject_ice
import omero_RTypes_ice
import omero_System_ice
import omero_Collections_ice

# Included module omero
_M_omero = Ice.openModule('omero')

# Included module omero.model
_M_omero.model = Ice.openModule('omero.model')

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Included module omero.sys
_M_omero.sys = Ice.openModule('omero.sys')

# Included module omero.api
_M_omero.api = Ice.openModule('omero.api')

# Start of module omero
__name__ = 'omero'

# Start of module omero.model
__name__ = 'omero.model'

if not _M_omero.model.__dict__.has_key('AnnotationAnnotationLink'):
    _M_omero.model._t_AnnotationAnnotationLink = IcePy.declareClass('::omero::model::AnnotationAnnotationLink')
    _M_omero.model._t_AnnotationAnnotationLinkPrx = IcePy.declareProxy('::omero::model::AnnotationAnnotationLink')

if not _M_omero.model.__dict__.has_key('Annotation'):
    _M_omero.model._t_Annotation = IcePy.declareClass('::omero::model::Annotation')
    _M_omero.model._t_AnnotationPrx = IcePy.declareProxy('::omero::model::Annotation')

if not _M_omero.model.__dict__.has_key('Details'):
    _M_omero.model._t_Details = IcePy.declareClass('::omero::model::Details')
    _M_omero.model._t_DetailsPrx = IcePy.declareProxy('::omero::model::Details')

if not _M_omero.model.__dict__.has_key('_t_AnnotationAnnotationLinksSeq'):
    _M_omero.model._t_AnnotationAnnotationLinksSeq = IcePy.defineSequence('::omero::model::AnnotationAnnotationLinksSeq', (), _M_omero.model._t_AnnotationAnnotationLink)

if not _M_omero.model.__dict__.has_key('_t_AnnotationLinkedAnnotationSeq'):
    _M_omero.model._t_AnnotationLinkedAnnotationSeq = IcePy.defineSequence('::omero::model::AnnotationLinkedAnnotationSeq', (), _M_omero.model._t_Annotation)

if not _M_omero.model.__dict__.has_key('Annotation'):
    _M_omero.model.Annotation = Ice.createTempClass()
    class Annotation(_M_omero.model.IObject):
        def __init__(self, _id=None, _details=None, _loaded=False, _version=None, _ns=None, _description=None, _annotationLinksSeq=None, _annotationLinksLoaded=False, _annotationLinksCountPerOwner=None):
            if __builtin__.type(self) == _M_omero.model.Annotation:
                raise RuntimeError('omero.model.Annotation is an abstract class')
            _M_omero.model.IObject.__init__(self, _id, _details, _loaded)
            self._version = _version
            self._ns = _ns
            self._description = _description
            self._annotationLinksSeq = _annotationLinksSeq
            self._annotationLinksLoaded = _annotationLinksLoaded
            self._annotationLinksCountPerOwner = _annotationLinksCountPerOwner

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::model::Annotation', '::omero::model::IObject')

        def ice_id(self, current=None):
            return '::omero::model::Annotation'

        def ice_staticId():
            return '::omero::model::Annotation'
        ice_staticId = staticmethod(ice_staticId)

        def getVersion(self, current=None):
            pass

        def setVersion(self, theVersion, current=None):
            pass

        def getNs(self, current=None):
            pass

        def setNs(self, theNs, current=None):
            pass

        def getDescription(self, current=None):
            pass

        def setDescription(self, theDescription, current=None):
            pass

        def unloadAnnotationLinks(self, current=None):
            pass

        def sizeOfAnnotationLinks(self, current=None):
            pass

        def copyAnnotationLinks(self, current=None):
            pass

        def addAnnotationAnnotationLink(self, target, current=None):
            pass

        def addAllAnnotationAnnotationLinkSet(self, targets, current=None):
            pass

        def removeAnnotationAnnotationLink(self, theTarget, current=None):
            pass

        def removeAllAnnotationAnnotationLinkSet(self, targets, current=None):
            pass

        def clearAnnotationLinks(self, current=None):
            pass

        def reloadAnnotationLinks(self, toCopy, current=None):
            pass

        def getAnnotationLinksCountPerOwner(self, current=None):
            pass

        def linkAnnotation(self, addition, current=None):
            pass

        def addAnnotationAnnotationLinkToBoth(self, link, bothSides, current=None):
            pass

        def findAnnotationAnnotationLink(self, removal, current=None):
            pass

        def unlinkAnnotation(self, removal, current=None):
            pass

        def removeAnnotationAnnotationLinkFromBoth(self, link, bothSides, current=None):
            pass

        def linkedAnnotationList(self, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.model._t_Annotation)

        __repr__ = __str__

    _M_omero.model.AnnotationPrx = Ice.createTempClass()
    class AnnotationPrx(_M_omero.model.IObjectPrx):

        def getVersion(self, _ctx=None):
            return _M_omero.model.Annotation._op_getVersion.invoke(self, ((), _ctx))

        def begin_getVersion(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Annotation._op_getVersion.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getVersion(self, _r):
            return _M_omero.model.Annotation._op_getVersion.end(self, _r)

        def setVersion(self, theVersion, _ctx=None):
            return _M_omero.model.Annotation._op_setVersion.invoke(self, ((theVersion, ), _ctx))

        def begin_setVersion(self, theVersion, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Annotation._op_setVersion.begin(self, ((theVersion, ), _response, _ex, _sent, _ctx))

        def end_setVersion(self, _r):
            return _M_omero.model.Annotation._op_setVersion.end(self, _r)

        def getNs(self, _ctx=None):
            return _M_omero.model.Annotation._op_getNs.invoke(self, ((), _ctx))

        def begin_getNs(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Annotation._op_getNs.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getNs(self, _r):
            return _M_omero.model.Annotation._op_getNs.end(self, _r)

        def setNs(self, theNs, _ctx=None):
            return _M_omero.model.Annotation._op_setNs.invoke(self, ((theNs, ), _ctx))

        def begin_setNs(self, theNs, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Annotation._op_setNs.begin(self, ((theNs, ), _response, _ex, _sent, _ctx))

        def end_setNs(self, _r):
            return _M_omero.model.Annotation._op_setNs.end(self, _r)

        def getDescription(self, _ctx=None):
            return _M_omero.model.Annotation._op_getDescription.invoke(self, ((), _ctx))

        def begin_getDescription(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Annotation._op_getDescription.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getDescription(self, _r):
            return _M_omero.model.Annotation._op_getDescription.end(self, _r)

        def setDescription(self, theDescription, _ctx=None):
            return _M_omero.model.Annotation._op_setDescription.invoke(self, ((theDescription, ), _ctx))

        def begin_setDescription(self, theDescription, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Annotation._op_setDescription.begin(self, ((theDescription, ), _response, _ex, _sent, _ctx))

        def end_setDescription(self, _r):
            return _M_omero.model.Annotation._op_setDescription.end(self, _r)

        def unloadAnnotationLinks(self, _ctx=None):
            return _M_omero.model.Annotation._op_unloadAnnotationLinks.invoke(self, ((), _ctx))

        def begin_unloadAnnotationLinks(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Annotation._op_unloadAnnotationLinks.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_unloadAnnotationLinks(self, _r):
            return _M_omero.model.Annotation._op_unloadAnnotationLinks.end(self, _r)

        def sizeOfAnnotationLinks(self, _ctx=None):
            return _M_omero.model.Annotation._op_sizeOfAnnotationLinks.invoke(self, ((), _ctx))

        def begin_sizeOfAnnotationLinks(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Annotation._op_sizeOfAnnotationLinks.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_sizeOfAnnotationLinks(self, _r):
            return _M_omero.model.Annotation._op_sizeOfAnnotationLinks.end(self, _r)

        def copyAnnotationLinks(self, _ctx=None):
            return _M_omero.model.Annotation._op_copyAnnotationLinks.invoke(self, ((), _ctx))

        def begin_copyAnnotationLinks(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Annotation._op_copyAnnotationLinks.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_copyAnnotationLinks(self, _r):
            return _M_omero.model.Annotation._op_copyAnnotationLinks.end(self, _r)

        def addAnnotationAnnotationLink(self, target, _ctx=None):
            return _M_omero.model.Annotation._op_addAnnotationAnnotationLink.invoke(self, ((target, ), _ctx))

        def begin_addAnnotationAnnotationLink(self, target, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Annotation._op_addAnnotationAnnotationLink.begin(self, ((target, ), _response, _ex, _sent, _ctx))

        def end_addAnnotationAnnotationLink(self, _r):
            return _M_omero.model.Annotation._op_addAnnotationAnnotationLink.end(self, _r)

        def addAllAnnotationAnnotationLinkSet(self, targets, _ctx=None):
            return _M_omero.model.Annotation._op_addAllAnnotationAnnotationLinkSet.invoke(self, ((targets, ), _ctx))

        def begin_addAllAnnotationAnnotationLinkSet(self, targets, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Annotation._op_addAllAnnotationAnnotationLinkSet.begin(self, ((targets, ), _response, _ex, _sent, _ctx))

        def end_addAllAnnotationAnnotationLinkSet(self, _r):
            return _M_omero.model.Annotation._op_addAllAnnotationAnnotationLinkSet.end(self, _r)

        def removeAnnotationAnnotationLink(self, theTarget, _ctx=None):
            return _M_omero.model.Annotation._op_removeAnnotationAnnotationLink.invoke(self, ((theTarget, ), _ctx))

        def begin_removeAnnotationAnnotationLink(self, theTarget, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Annotation._op_removeAnnotationAnnotationLink.begin(self, ((theTarget, ), _response, _ex, _sent, _ctx))

        def end_removeAnnotationAnnotationLink(self, _r):
            return _M_omero.model.Annotation._op_removeAnnotationAnnotationLink.end(self, _r)

        def removeAllAnnotationAnnotationLinkSet(self, targets, _ctx=None):
            return _M_omero.model.Annotation._op_removeAllAnnotationAnnotationLinkSet.invoke(self, ((targets, ), _ctx))

        def begin_removeAllAnnotationAnnotationLinkSet(self, targets, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Annotation._op_removeAllAnnotationAnnotationLinkSet.begin(self, ((targets, ), _response, _ex, _sent, _ctx))

        def end_removeAllAnnotationAnnotationLinkSet(self, _r):
            return _M_omero.model.Annotation._op_removeAllAnnotationAnnotationLinkSet.end(self, _r)

        def clearAnnotationLinks(self, _ctx=None):
            return _M_omero.model.Annotation._op_clearAnnotationLinks.invoke(self, ((), _ctx))

        def begin_clearAnnotationLinks(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Annotation._op_clearAnnotationLinks.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_clearAnnotationLinks(self, _r):
            return _M_omero.model.Annotation._op_clearAnnotationLinks.end(self, _r)

        def reloadAnnotationLinks(self, toCopy, _ctx=None):
            return _M_omero.model.Annotation._op_reloadAnnotationLinks.invoke(self, ((toCopy, ), _ctx))

        def begin_reloadAnnotationLinks(self, toCopy, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Annotation._op_reloadAnnotationLinks.begin(self, ((toCopy, ), _response, _ex, _sent, _ctx))

        def end_reloadAnnotationLinks(self, _r):
            return _M_omero.model.Annotation._op_reloadAnnotationLinks.end(self, _r)

        def getAnnotationLinksCountPerOwner(self, _ctx=None):
            return _M_omero.model.Annotation._op_getAnnotationLinksCountPerOwner.invoke(self, ((), _ctx))

        def begin_getAnnotationLinksCountPerOwner(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Annotation._op_getAnnotationLinksCountPerOwner.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getAnnotationLinksCountPerOwner(self, _r):
            return _M_omero.model.Annotation._op_getAnnotationLinksCountPerOwner.end(self, _r)

        def linkAnnotation(self, addition, _ctx=None):
            return _M_omero.model.Annotation._op_linkAnnotation.invoke(self, ((addition, ), _ctx))

        def begin_linkAnnotation(self, addition, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Annotation._op_linkAnnotation.begin(self, ((addition, ), _response, _ex, _sent, _ctx))

        def end_linkAnnotation(self, _r):
            return _M_omero.model.Annotation._op_linkAnnotation.end(self, _r)

        def addAnnotationAnnotationLinkToBoth(self, link, bothSides, _ctx=None):
            return _M_omero.model.Annotation._op_addAnnotationAnnotationLinkToBoth.invoke(self, ((link, bothSides), _ctx))

        def begin_addAnnotationAnnotationLinkToBoth(self, link, bothSides, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Annotation._op_addAnnotationAnnotationLinkToBoth.begin(self, ((link, bothSides), _response, _ex, _sent, _ctx))

        def end_addAnnotationAnnotationLinkToBoth(self, _r):
            return _M_omero.model.Annotation._op_addAnnotationAnnotationLinkToBoth.end(self, _r)

        def findAnnotationAnnotationLink(self, removal, _ctx=None):
            return _M_omero.model.Annotation._op_findAnnotationAnnotationLink.invoke(self, ((removal, ), _ctx))

        def begin_findAnnotationAnnotationLink(self, removal, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Annotation._op_findAnnotationAnnotationLink.begin(self, ((removal, ), _response, _ex, _sent, _ctx))

        def end_findAnnotationAnnotationLink(self, _r):
            return _M_omero.model.Annotation._op_findAnnotationAnnotationLink.end(self, _r)

        def unlinkAnnotation(self, removal, _ctx=None):
            return _M_omero.model.Annotation._op_unlinkAnnotation.invoke(self, ((removal, ), _ctx))

        def begin_unlinkAnnotation(self, removal, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Annotation._op_unlinkAnnotation.begin(self, ((removal, ), _response, _ex, _sent, _ctx))

        def end_unlinkAnnotation(self, _r):
            return _M_omero.model.Annotation._op_unlinkAnnotation.end(self, _r)

        def removeAnnotationAnnotationLinkFromBoth(self, link, bothSides, _ctx=None):
            return _M_omero.model.Annotation._op_removeAnnotationAnnotationLinkFromBoth.invoke(self, ((link, bothSides), _ctx))

        def begin_removeAnnotationAnnotationLinkFromBoth(self, link, bothSides, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Annotation._op_removeAnnotationAnnotationLinkFromBoth.begin(self, ((link, bothSides), _response, _ex, _sent, _ctx))

        def end_removeAnnotationAnnotationLinkFromBoth(self, _r):
            return _M_omero.model.Annotation._op_removeAnnotationAnnotationLinkFromBoth.end(self, _r)

        def linkedAnnotationList(self, _ctx=None):
            return _M_omero.model.Annotation._op_linkedAnnotationList.invoke(self, ((), _ctx))

        def begin_linkedAnnotationList(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Annotation._op_linkedAnnotationList.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_linkedAnnotationList(self, _r):
            return _M_omero.model.Annotation._op_linkedAnnotationList.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.model.AnnotationPrx.ice_checkedCast(proxy, '::omero::model::Annotation', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.model.AnnotationPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_omero.model._t_AnnotationPrx = IcePy.defineProxy('::omero::model::Annotation', AnnotationPrx)

    _M_omero.model._t_Annotation = IcePy.defineClass('::omero::model::Annotation', Annotation, (), True, _M_omero.model._t_IObject, (), (
        ('_version', (), _M_omero._t_RInt),
        ('_ns', (), _M_omero._t_RString),
        ('_description', (), _M_omero._t_RString),
        ('_annotationLinksSeq', (), _M_omero.model._t_AnnotationAnnotationLinksSeq),
        ('_annotationLinksLoaded', (), IcePy._t_bool),
        ('_annotationLinksCountPerOwner', (), _M_omero.sys._t_CountMap)
    ))
    Annotation._ice_type = _M_omero.model._t_Annotation

    Annotation._op_getVersion = IcePy.Operation('getVersion', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RInt, ())
    Annotation._op_setVersion = IcePy.Operation('setVersion', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RInt),), (), None, ())
    Annotation._op_getNs = IcePy.Operation('getNs', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RString, ())
    Annotation._op_setNs = IcePy.Operation('setNs', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RString),), (), None, ())
    Annotation._op_getDescription = IcePy.Operation('getDescription', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RString, ())
    Annotation._op_setDescription = IcePy.Operation('setDescription', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RString),), (), None, ())
    Annotation._op_unloadAnnotationLinks = IcePy.Operation('unloadAnnotationLinks', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), None, ())
    Annotation._op_sizeOfAnnotationLinks = IcePy.Operation('sizeOfAnnotationLinks', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), IcePy._t_int, ())
    Annotation._op_copyAnnotationLinks = IcePy.Operation('copyAnnotationLinks', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero.model._t_AnnotationAnnotationLinksSeq, ())
    Annotation._op_addAnnotationAnnotationLink = IcePy.Operation('addAnnotationAnnotationLink', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero.model._t_AnnotationAnnotationLink),), (), None, ())
    Annotation._op_addAllAnnotationAnnotationLinkSet = IcePy.Operation('addAllAnnotationAnnotationLinkSet', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero.model._t_AnnotationAnnotationLinksSeq),), (), None, ())
    Annotation._op_removeAnnotationAnnotationLink = IcePy.Operation('removeAnnotationAnnotationLink', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero.model._t_AnnotationAnnotationLink),), (), None, ())
    Annotation._op_removeAllAnnotationAnnotationLinkSet = IcePy.Operation('removeAllAnnotationAnnotationLinkSet', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero.model._t_AnnotationAnnotationLinksSeq),), (), None, ())
    Annotation._op_clearAnnotationLinks = IcePy.Operation('clearAnnotationLinks', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), None, ())
    Annotation._op_reloadAnnotationLinks = IcePy.Operation('reloadAnnotationLinks', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero.model._t_Annotation),), (), None, ())
    Annotation._op_getAnnotationLinksCountPerOwner = IcePy.Operation('getAnnotationLinksCountPerOwner', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero.sys._t_CountMap, ())
    Annotation._op_linkAnnotation = IcePy.Operation('linkAnnotation', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero.model._t_Annotation),), (), _M_omero.model._t_AnnotationAnnotationLink, ())
    Annotation._op_addAnnotationAnnotationLinkToBoth = IcePy.Operation('addAnnotationAnnotationLinkToBoth', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero.model._t_AnnotationAnnotationLink), ((), IcePy._t_bool)), (), None, ())
    Annotation._op_findAnnotationAnnotationLink = IcePy.Operation('findAnnotationAnnotationLink', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero.model._t_Annotation),), (), _M_omero.model._t_AnnotationAnnotationLinksSeq, ())
    Annotation._op_unlinkAnnotation = IcePy.Operation('unlinkAnnotation', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero.model._t_Annotation),), (), None, ())
    Annotation._op_removeAnnotationAnnotationLinkFromBoth = IcePy.Operation('removeAnnotationAnnotationLinkFromBoth', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero.model._t_AnnotationAnnotationLink), ((), IcePy._t_bool)), (), None, ())
    Annotation._op_linkedAnnotationList = IcePy.Operation('linkedAnnotationList', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero.model._t_AnnotationLinkedAnnotationSeq, ())

    _M_omero.model.Annotation = Annotation
    del Annotation

    _M_omero.model.AnnotationPrx = AnnotationPrx
    del AnnotationPrx

# End of module omero.model

__name__ = 'omero'

# End of module omero
