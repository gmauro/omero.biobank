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
# Generated from file `DataCollectionItem.ice'
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

if not _M_omero.model.__dict__.has_key('DataSample'):
    _M_omero.model._t_DataSample = IcePy.declareClass('::omero::model::DataSample')
    _M_omero.model._t_DataSamplePrx = IcePy.declareProxy('::omero::model::DataSample')

if not _M_omero.model.__dict__.has_key('DataCollection'):
    _M_omero.model._t_DataCollection = IcePy.declareClass('::omero::model::DataCollection')
    _M_omero.model._t_DataCollectionPrx = IcePy.declareProxy('::omero::model::DataCollection')

if not _M_omero.model.__dict__.has_key('Details'):
    _M_omero.model._t_Details = IcePy.declareClass('::omero::model::Details')
    _M_omero.model._t_DetailsPrx = IcePy.declareProxy('::omero::model::Details')

if not _M_omero.model.__dict__.has_key('DataCollectionItem'):
    _M_omero.model.DataCollectionItem = Ice.createTempClass()
    class DataCollectionItem(_M_omero.model.IObject):
        def __init__(self, _id=None, _details=None, _loaded=False, _version=None, _vid=None, _dataSample=None, _dataCollection=None, _dataCollectionItemUK=None):
            if __builtin__.type(self) == _M_omero.model.DataCollectionItem:
                raise RuntimeError('omero.model.DataCollectionItem is an abstract class')
            _M_omero.model.IObject.__init__(self, _id, _details, _loaded)
            self._version = _version
            self._vid = _vid
            self._dataSample = _dataSample
            self._dataCollection = _dataCollection
            self._dataCollectionItemUK = _dataCollectionItemUK

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::model::DataCollectionItem', '::omero::model::IObject')

        def ice_id(self, current=None):
            return '::omero::model::DataCollectionItem'

        def ice_staticId():
            return '::omero::model::DataCollectionItem'
        ice_staticId = staticmethod(ice_staticId)

        def getVersion(self, current=None):
            pass

        def setVersion(self, theVersion, current=None):
            pass

        def getVid(self, current=None):
            pass

        def setVid(self, theVid, current=None):
            pass

        def getDataSample(self, current=None):
            pass

        def setDataSample(self, theDataSample, current=None):
            pass

        def getDataCollection(self, current=None):
            pass

        def setDataCollection(self, theDataCollection, current=None):
            pass

        def getDataCollectionItemUK(self, current=None):
            pass

        def setDataCollectionItemUK(self, theDataCollectionItemUK, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.model._t_DataCollectionItem)

        __repr__ = __str__

    _M_omero.model.DataCollectionItemPrx = Ice.createTempClass()
    class DataCollectionItemPrx(_M_omero.model.IObjectPrx):

        def getVersion(self, _ctx=None):
            return _M_omero.model.DataCollectionItem._op_getVersion.invoke(self, ((), _ctx))

        def begin_getVersion(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.DataCollectionItem._op_getVersion.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getVersion(self, _r):
            return _M_omero.model.DataCollectionItem._op_getVersion.end(self, _r)

        def setVersion(self, theVersion, _ctx=None):
            return _M_omero.model.DataCollectionItem._op_setVersion.invoke(self, ((theVersion, ), _ctx))

        def begin_setVersion(self, theVersion, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.DataCollectionItem._op_setVersion.begin(self, ((theVersion, ), _response, _ex, _sent, _ctx))

        def end_setVersion(self, _r):
            return _M_omero.model.DataCollectionItem._op_setVersion.end(self, _r)

        def getVid(self, _ctx=None):
            return _M_omero.model.DataCollectionItem._op_getVid.invoke(self, ((), _ctx))

        def begin_getVid(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.DataCollectionItem._op_getVid.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getVid(self, _r):
            return _M_omero.model.DataCollectionItem._op_getVid.end(self, _r)

        def setVid(self, theVid, _ctx=None):
            return _M_omero.model.DataCollectionItem._op_setVid.invoke(self, ((theVid, ), _ctx))

        def begin_setVid(self, theVid, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.DataCollectionItem._op_setVid.begin(self, ((theVid, ), _response, _ex, _sent, _ctx))

        def end_setVid(self, _r):
            return _M_omero.model.DataCollectionItem._op_setVid.end(self, _r)

        def getDataSample(self, _ctx=None):
            return _M_omero.model.DataCollectionItem._op_getDataSample.invoke(self, ((), _ctx))

        def begin_getDataSample(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.DataCollectionItem._op_getDataSample.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getDataSample(self, _r):
            return _M_omero.model.DataCollectionItem._op_getDataSample.end(self, _r)

        def setDataSample(self, theDataSample, _ctx=None):
            return _M_omero.model.DataCollectionItem._op_setDataSample.invoke(self, ((theDataSample, ), _ctx))

        def begin_setDataSample(self, theDataSample, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.DataCollectionItem._op_setDataSample.begin(self, ((theDataSample, ), _response, _ex, _sent, _ctx))

        def end_setDataSample(self, _r):
            return _M_omero.model.DataCollectionItem._op_setDataSample.end(self, _r)

        def getDataCollection(self, _ctx=None):
            return _M_omero.model.DataCollectionItem._op_getDataCollection.invoke(self, ((), _ctx))

        def begin_getDataCollection(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.DataCollectionItem._op_getDataCollection.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getDataCollection(self, _r):
            return _M_omero.model.DataCollectionItem._op_getDataCollection.end(self, _r)

        def setDataCollection(self, theDataCollection, _ctx=None):
            return _M_omero.model.DataCollectionItem._op_setDataCollection.invoke(self, ((theDataCollection, ), _ctx))

        def begin_setDataCollection(self, theDataCollection, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.DataCollectionItem._op_setDataCollection.begin(self, ((theDataCollection, ), _response, _ex, _sent, _ctx))

        def end_setDataCollection(self, _r):
            return _M_omero.model.DataCollectionItem._op_setDataCollection.end(self, _r)

        def getDataCollectionItemUK(self, _ctx=None):
            return _M_omero.model.DataCollectionItem._op_getDataCollectionItemUK.invoke(self, ((), _ctx))

        def begin_getDataCollectionItemUK(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.DataCollectionItem._op_getDataCollectionItemUK.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getDataCollectionItemUK(self, _r):
            return _M_omero.model.DataCollectionItem._op_getDataCollectionItemUK.end(self, _r)

        def setDataCollectionItemUK(self, theDataCollectionItemUK, _ctx=None):
            return _M_omero.model.DataCollectionItem._op_setDataCollectionItemUK.invoke(self, ((theDataCollectionItemUK, ), _ctx))

        def begin_setDataCollectionItemUK(self, theDataCollectionItemUK, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.DataCollectionItem._op_setDataCollectionItemUK.begin(self, ((theDataCollectionItemUK, ), _response, _ex, _sent, _ctx))

        def end_setDataCollectionItemUK(self, _r):
            return _M_omero.model.DataCollectionItem._op_setDataCollectionItemUK.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.model.DataCollectionItemPrx.ice_checkedCast(proxy, '::omero::model::DataCollectionItem', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.model.DataCollectionItemPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_omero.model._t_DataCollectionItemPrx = IcePy.defineProxy('::omero::model::DataCollectionItem', DataCollectionItemPrx)

    _M_omero.model._t_DataCollectionItem = IcePy.declareClass('::omero::model::DataCollectionItem')

    _M_omero.model._t_DataCollectionItem = IcePy.defineClass('::omero::model::DataCollectionItem', DataCollectionItem, (), True, _M_omero.model._t_IObject, (), (
        ('_version', (), _M_omero._t_RInt),
        ('_vid', (), _M_omero._t_RString),
        ('_dataSample', (), _M_omero.model._t_DataSample),
        ('_dataCollection', (), _M_omero.model._t_DataCollection),
        ('_dataCollectionItemUK', (), _M_omero._t_RString)
    ))
    DataCollectionItem._ice_type = _M_omero.model._t_DataCollectionItem

    DataCollectionItem._op_getVersion = IcePy.Operation('getVersion', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RInt, ())
    DataCollectionItem._op_setVersion = IcePy.Operation('setVersion', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RInt),), (), None, ())
    DataCollectionItem._op_getVid = IcePy.Operation('getVid', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RString, ())
    DataCollectionItem._op_setVid = IcePy.Operation('setVid', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RString),), (), None, ())
    DataCollectionItem._op_getDataSample = IcePy.Operation('getDataSample', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero.model._t_DataSample, ())
    DataCollectionItem._op_setDataSample = IcePy.Operation('setDataSample', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero.model._t_DataSample),), (), None, ())
    DataCollectionItem._op_getDataCollection = IcePy.Operation('getDataCollection', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero.model._t_DataCollection, ())
    DataCollectionItem._op_setDataCollection = IcePy.Operation('setDataCollection', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero.model._t_DataCollection),), (), None, ())
    DataCollectionItem._op_getDataCollectionItemUK = IcePy.Operation('getDataCollectionItemUK', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RString, ())
    DataCollectionItem._op_setDataCollectionItemUK = IcePy.Operation('setDataCollectionItemUK', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RString),), (), None, ())

    _M_omero.model.DataCollectionItem = DataCollectionItem
    del DataCollectionItem

    _M_omero.model.DataCollectionItemPrx = DataCollectionItemPrx
    del DataCollectionItemPrx

# End of module omero.model

__name__ = 'omero'

# End of module omero
