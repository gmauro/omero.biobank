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
# Generated from file `IContainer.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

import Ice, IcePy, __builtin__
import omero_ModelF_ice
import omero_ServicesF_ice
import omero_System_ice
import omero_Collections_ice

# Included module omero
_M_omero = Ice.openModule('omero')

# Included module omero.model
_M_omero.model = Ice.openModule('omero.model')

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Included module Glacier2
_M_Glacier2 = Ice.openModule('Glacier2')

# Included module omero.sys
_M_omero.sys = Ice.openModule('omero.sys')

# Included module omero.api
_M_omero.api = Ice.openModule('omero.api')

# Included module omero.grid
_M_omero.grid = Ice.openModule('omero.grid')

# Start of module omero
__name__ = 'omero'

# Start of module omero.api
__name__ = 'omero.api'

if not _M_omero.api.__dict__.has_key('IContainer'):
    _M_omero.api.IContainer = Ice.createTempClass()
    class IContainer(_M_omero.api.ServiceInterface):
        '''See IContainer.html'''
        def __init__(self):
            if __builtin__.type(self) == _M_omero.api.IContainer:
                raise RuntimeError('omero.api.IContainer is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::api::IContainer', '::omero::api::ServiceInterface')

        def ice_id(self, current=None):
            return '::omero::api::IContainer'

        def ice_staticId():
            return '::omero::api::IContainer'
        ice_staticId = staticmethod(ice_staticId)

        def loadContainerHierarchy_async(self, _cb, rootType, rootIds, options, current=None):
            pass

        def findContainerHierarchies_async(self, _cb, rootType, imageIds, options, current=None):
            pass

        def getImages_async(self, _cb, rootType, rootIds, options, current=None):
            pass

        def getUserImages_async(self, _cb, options, current=None):
            pass

        def getImagesByOptions_async(self, _cb, options, current=None):
            pass

        def getCollectionCount_async(self, _cb, type, property, ids, options, current=None):
            pass

        def retrieveCollection_async(self, _cb, obj, collectionName, options, current=None):
            pass

        def createDataObject_async(self, _cb, obj, options, current=None):
            pass

        def createDataObjects_async(self, _cb, dataObjects, options, current=None):
            pass

        def unlink_async(self, _cb, links, options, current=None):
            pass

        def link_async(self, _cb, links, options, current=None):
            pass

        def updateDataObject_async(self, _cb, obj, options, current=None):
            pass

        def updateDataObjects_async(self, _cb, objs, options, current=None):
            pass

        def deleteDataObject_async(self, _cb, obj, options, current=None):
            pass

        def deleteDataObjects_async(self, _cb, objs, options, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.api._t_IContainer)

        __repr__ = __str__

    _M_omero.api.IContainerPrx = Ice.createTempClass()
    class IContainerPrx(_M_omero.api.ServiceInterfacePrx):

        def loadContainerHierarchy(self, rootType, rootIds, options, _ctx=None):
            return _M_omero.api.IContainer._op_loadContainerHierarchy.invoke(self, ((rootType, rootIds, options), _ctx))

        def begin_loadContainerHierarchy(self, rootType, rootIds, options, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.IContainer._op_loadContainerHierarchy.begin(self, ((rootType, rootIds, options), _response, _ex, _sent, _ctx))

        def end_loadContainerHierarchy(self, _r):
            return _M_omero.api.IContainer._op_loadContainerHierarchy.end(self, _r)

        def loadContainerHierarchy_async(self, _cb, rootType, rootIds, options, _ctx=None):
            return _M_omero.api.IContainer._op_loadContainerHierarchy.invokeAsync(self, (_cb, (rootType, rootIds, options), _ctx))

        def findContainerHierarchies(self, rootType, imageIds, options, _ctx=None):
            return _M_omero.api.IContainer._op_findContainerHierarchies.invoke(self, ((rootType, imageIds, options), _ctx))

        def begin_findContainerHierarchies(self, rootType, imageIds, options, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.IContainer._op_findContainerHierarchies.begin(self, ((rootType, imageIds, options), _response, _ex, _sent, _ctx))

        def end_findContainerHierarchies(self, _r):
            return _M_omero.api.IContainer._op_findContainerHierarchies.end(self, _r)

        def findContainerHierarchies_async(self, _cb, rootType, imageIds, options, _ctx=None):
            return _M_omero.api.IContainer._op_findContainerHierarchies.invokeAsync(self, (_cb, (rootType, imageIds, options), _ctx))

        def getImages(self, rootType, rootIds, options, _ctx=None):
            return _M_omero.api.IContainer._op_getImages.invoke(self, ((rootType, rootIds, options), _ctx))

        def begin_getImages(self, rootType, rootIds, options, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.IContainer._op_getImages.begin(self, ((rootType, rootIds, options), _response, _ex, _sent, _ctx))

        def end_getImages(self, _r):
            return _M_omero.api.IContainer._op_getImages.end(self, _r)

        def getImages_async(self, _cb, rootType, rootIds, options, _ctx=None):
            return _M_omero.api.IContainer._op_getImages.invokeAsync(self, (_cb, (rootType, rootIds, options), _ctx))

        def getUserImages(self, options, _ctx=None):
            return _M_omero.api.IContainer._op_getUserImages.invoke(self, ((options, ), _ctx))

        def begin_getUserImages(self, options, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.IContainer._op_getUserImages.begin(self, ((options, ), _response, _ex, _sent, _ctx))

        def end_getUserImages(self, _r):
            return _M_omero.api.IContainer._op_getUserImages.end(self, _r)

        def getUserImages_async(self, _cb, options, _ctx=None):
            return _M_omero.api.IContainer._op_getUserImages.invokeAsync(self, (_cb, (options, ), _ctx))

        def getImagesByOptions(self, options, _ctx=None):
            return _M_omero.api.IContainer._op_getImagesByOptions.invoke(self, ((options, ), _ctx))

        def begin_getImagesByOptions(self, options, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.IContainer._op_getImagesByOptions.begin(self, ((options, ), _response, _ex, _sent, _ctx))

        def end_getImagesByOptions(self, _r):
            return _M_omero.api.IContainer._op_getImagesByOptions.end(self, _r)

        def getImagesByOptions_async(self, _cb, options, _ctx=None):
            return _M_omero.api.IContainer._op_getImagesByOptions.invokeAsync(self, (_cb, (options, ), _ctx))

        def getCollectionCount(self, type, property, ids, options, _ctx=None):
            return _M_omero.api.IContainer._op_getCollectionCount.invoke(self, ((type, property, ids, options), _ctx))

        def begin_getCollectionCount(self, type, property, ids, options, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.IContainer._op_getCollectionCount.begin(self, ((type, property, ids, options), _response, _ex, _sent, _ctx))

        def end_getCollectionCount(self, _r):
            return _M_omero.api.IContainer._op_getCollectionCount.end(self, _r)

        def getCollectionCount_async(self, _cb, type, property, ids, options, _ctx=None):
            return _M_omero.api.IContainer._op_getCollectionCount.invokeAsync(self, (_cb, (type, property, ids, options), _ctx))

        def retrieveCollection(self, obj, collectionName, options, _ctx=None):
            return _M_omero.api.IContainer._op_retrieveCollection.invoke(self, ((obj, collectionName, options), _ctx))

        def begin_retrieveCollection(self, obj, collectionName, options, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.IContainer._op_retrieveCollection.begin(self, ((obj, collectionName, options), _response, _ex, _sent, _ctx))

        def end_retrieveCollection(self, _r):
            return _M_omero.api.IContainer._op_retrieveCollection.end(self, _r)

        def retrieveCollection_async(self, _cb, obj, collectionName, options, _ctx=None):
            return _M_omero.api.IContainer._op_retrieveCollection.invokeAsync(self, (_cb, (obj, collectionName, options), _ctx))

        def createDataObject(self, obj, options, _ctx=None):
            return _M_omero.api.IContainer._op_createDataObject.invoke(self, ((obj, options), _ctx))

        def begin_createDataObject(self, obj, options, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.IContainer._op_createDataObject.begin(self, ((obj, options), _response, _ex, _sent, _ctx))

        def end_createDataObject(self, _r):
            return _M_omero.api.IContainer._op_createDataObject.end(self, _r)

        def createDataObject_async(self, _cb, obj, options, _ctx=None):
            return _M_omero.api.IContainer._op_createDataObject.invokeAsync(self, (_cb, (obj, options), _ctx))

        def createDataObjects(self, dataObjects, options, _ctx=None):
            return _M_omero.api.IContainer._op_createDataObjects.invoke(self, ((dataObjects, options), _ctx))

        def begin_createDataObjects(self, dataObjects, options, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.IContainer._op_createDataObjects.begin(self, ((dataObjects, options), _response, _ex, _sent, _ctx))

        def end_createDataObjects(self, _r):
            return _M_omero.api.IContainer._op_createDataObjects.end(self, _r)

        def createDataObjects_async(self, _cb, dataObjects, options, _ctx=None):
            return _M_omero.api.IContainer._op_createDataObjects.invokeAsync(self, (_cb, (dataObjects, options), _ctx))

        def unlink(self, links, options, _ctx=None):
            return _M_omero.api.IContainer._op_unlink.invoke(self, ((links, options), _ctx))

        def begin_unlink(self, links, options, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.IContainer._op_unlink.begin(self, ((links, options), _response, _ex, _sent, _ctx))

        def end_unlink(self, _r):
            return _M_omero.api.IContainer._op_unlink.end(self, _r)

        def unlink_async(self, _cb, links, options, _ctx=None):
            return _M_omero.api.IContainer._op_unlink.invokeAsync(self, (_cb, (links, options), _ctx))

        def link(self, links, options, _ctx=None):
            return _M_omero.api.IContainer._op_link.invoke(self, ((links, options), _ctx))

        def begin_link(self, links, options, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.IContainer._op_link.begin(self, ((links, options), _response, _ex, _sent, _ctx))

        def end_link(self, _r):
            return _M_omero.api.IContainer._op_link.end(self, _r)

        def link_async(self, _cb, links, options, _ctx=None):
            return _M_omero.api.IContainer._op_link.invokeAsync(self, (_cb, (links, options), _ctx))

        def updateDataObject(self, obj, options, _ctx=None):
            return _M_omero.api.IContainer._op_updateDataObject.invoke(self, ((obj, options), _ctx))

        def begin_updateDataObject(self, obj, options, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.IContainer._op_updateDataObject.begin(self, ((obj, options), _response, _ex, _sent, _ctx))

        def end_updateDataObject(self, _r):
            return _M_omero.api.IContainer._op_updateDataObject.end(self, _r)

        def updateDataObject_async(self, _cb, obj, options, _ctx=None):
            return _M_omero.api.IContainer._op_updateDataObject.invokeAsync(self, (_cb, (obj, options), _ctx))

        def updateDataObjects(self, objs, options, _ctx=None):
            return _M_omero.api.IContainer._op_updateDataObjects.invoke(self, ((objs, options), _ctx))

        def begin_updateDataObjects(self, objs, options, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.IContainer._op_updateDataObjects.begin(self, ((objs, options), _response, _ex, _sent, _ctx))

        def end_updateDataObjects(self, _r):
            return _M_omero.api.IContainer._op_updateDataObjects.end(self, _r)

        def updateDataObjects_async(self, _cb, objs, options, _ctx=None):
            return _M_omero.api.IContainer._op_updateDataObjects.invokeAsync(self, (_cb, (objs, options), _ctx))

        def deleteDataObject(self, obj, options, _ctx=None):
            return _M_omero.api.IContainer._op_deleteDataObject.invoke(self, ((obj, options), _ctx))

        def begin_deleteDataObject(self, obj, options, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.IContainer._op_deleteDataObject.begin(self, ((obj, options), _response, _ex, _sent, _ctx))

        def end_deleteDataObject(self, _r):
            return _M_omero.api.IContainer._op_deleteDataObject.end(self, _r)

        def deleteDataObject_async(self, _cb, obj, options, _ctx=None):
            return _M_omero.api.IContainer._op_deleteDataObject.invokeAsync(self, (_cb, (obj, options), _ctx))

        def deleteDataObjects(self, objs, options, _ctx=None):
            return _M_omero.api.IContainer._op_deleteDataObjects.invoke(self, ((objs, options), _ctx))

        def begin_deleteDataObjects(self, objs, options, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.IContainer._op_deleteDataObjects.begin(self, ((objs, options), _response, _ex, _sent, _ctx))

        def end_deleteDataObjects(self, _r):
            return _M_omero.api.IContainer._op_deleteDataObjects.end(self, _r)

        def deleteDataObjects_async(self, _cb, objs, options, _ctx=None):
            return _M_omero.api.IContainer._op_deleteDataObjects.invokeAsync(self, (_cb, (objs, options), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.api.IContainerPrx.ice_checkedCast(proxy, '::omero::api::IContainer', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.api.IContainerPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_omero.api._t_IContainerPrx = IcePy.defineProxy('::omero::api::IContainer', IContainerPrx)

    _M_omero.api._t_IContainer = IcePy.defineClass('::omero::api::IContainer', IContainer, (), True, None, (_M_omero.api._t_ServiceInterface,), ())
    IContainer._ice_type = _M_omero.api._t_IContainer

    IContainer._op_loadContainerHierarchy = IcePy.Operation('loadContainerHierarchy', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, True, (), (((), IcePy._t_string), ((), _M_omero.sys._t_LongList), ((), _M_omero.sys._t_Parameters)), (), _M_omero.api._t_IObjectList, (_M_omero._t_ServerError,))
    IContainer._op_findContainerHierarchies = IcePy.Operation('findContainerHierarchies', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, True, (), (((), IcePy._t_string), ((), _M_omero.sys._t_LongList), ((), _M_omero.sys._t_Parameters)), (), _M_omero.api._t_IObjectList, (_M_omero._t_ServerError,))
    IContainer._op_getImages = IcePy.Operation('getImages', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, True, (), (((), IcePy._t_string), ((), _M_omero.sys._t_LongList), ((), _M_omero.sys._t_Parameters)), (), _M_omero.api._t_ImageList, (_M_omero._t_ServerError,))
    IContainer._op_getUserImages = IcePy.Operation('getUserImages', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, True, (), (((), _M_omero.sys._t_Parameters),), (), _M_omero.api._t_ImageList, (_M_omero._t_ServerError,))
    IContainer._op_getImagesByOptions = IcePy.Operation('getImagesByOptions', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, True, (), (((), _M_omero.sys._t_Parameters),), (), _M_omero.api._t_ImageList, (_M_omero._t_ServerError,))
    IContainer._op_getCollectionCount = IcePy.Operation('getCollectionCount', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, True, (), (((), IcePy._t_string), ((), IcePy._t_string), ((), _M_omero.sys._t_LongList), ((), _M_omero.sys._t_Parameters)), (), _M_omero.sys._t_CountMap, (_M_omero._t_ServerError,))
    IContainer._op_retrieveCollection = IcePy.Operation('retrieveCollection', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, True, (), (((), _M_omero.model._t_IObject), ((), IcePy._t_string), ((), _M_omero.sys._t_Parameters)), (), _M_omero.api._t_IObjectList, (_M_omero._t_ServerError,))
    IContainer._op_createDataObject = IcePy.Operation('createDataObject', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, (), (((), _M_omero.model._t_IObject), ((), _M_omero.sys._t_Parameters)), (), _M_omero.model._t_IObject, (_M_omero._t_ServerError,))
    IContainer._op_createDataObjects = IcePy.Operation('createDataObjects', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, (), (((), _M_omero.api._t_IObjectList), ((), _M_omero.sys._t_Parameters)), (), _M_omero.api._t_IObjectList, (_M_omero._t_ServerError,))
    IContainer._op_unlink = IcePy.Operation('unlink', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, (), (((), _M_omero.api._t_IObjectList), ((), _M_omero.sys._t_Parameters)), (), None, (_M_omero._t_ServerError,))
    IContainer._op_link = IcePy.Operation('link', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, (), (((), _M_omero.api._t_IObjectList), ((), _M_omero.sys._t_Parameters)), (), _M_omero.api._t_IObjectList, (_M_omero._t_ServerError,))
    IContainer._op_updateDataObject = IcePy.Operation('updateDataObject', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, (), (((), _M_omero.model._t_IObject), ((), _M_omero.sys._t_Parameters)), (), _M_omero.model._t_IObject, (_M_omero._t_ServerError,))
    IContainer._op_updateDataObjects = IcePy.Operation('updateDataObjects', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, (), (((), _M_omero.api._t_IObjectList), ((), _M_omero.sys._t_Parameters)), (), _M_omero.api._t_IObjectList, (_M_omero._t_ServerError,))
    IContainer._op_deleteDataObject = IcePy.Operation('deleteDataObject', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, (), (((), _M_omero.model._t_IObject), ((), _M_omero.sys._t_Parameters)), (), None, (_M_omero._t_ServerError,))
    IContainer._op_deleteDataObject.deprecate(" use omero::model::IDelete::queueDelete instead")
    IContainer._op_deleteDataObjects = IcePy.Operation('deleteDataObjects', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, (), (((), _M_omero.api._t_IObjectList), ((), _M_omero.sys._t_Parameters)), (), None, (_M_omero._t_ServerError,))
    IContainer._op_deleteDataObjects.deprecate(" use omero::model::IDelete::queueDelete instead")

    _M_omero.api.IContainer = IContainer
    del IContainer

    _M_omero.api.IContainerPrx = IContainerPrx
    del IContainerPrx

# End of module omero.api

__name__ = 'omero'

# End of module omero
