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
# Generated from file `TiterPlate.ice'
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
import omero_model_SlottedContainer_ice

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

if not _M_omero.model.__dict__.has_key('ContainerStatus'):
    _M_omero.model._t_ContainerStatus = IcePy.declareClass('::omero::model::ContainerStatus')
    _M_omero.model._t_ContainerStatusPrx = IcePy.declareProxy('::omero::model::ContainerStatus')

if not _M_omero.model.__dict__.has_key('Action'):
    _M_omero.model._t_Action = IcePy.declareClass('::omero::model::Action')
    _M_omero.model._t_ActionPrx = IcePy.declareProxy('::omero::model::Action')

if not _M_omero.model.__dict__.has_key('Details'):
    _M_omero.model._t_Details = IcePy.declareClass('::omero::model::Details')
    _M_omero.model._t_DetailsPrx = IcePy.declareProxy('::omero::model::Details')

if not _M_omero.model.__dict__.has_key('TiterPlate'):
    _M_omero.model.TiterPlate = Ice.createTempClass()
    class TiterPlate(_M_omero.model.SlottedContainer):
        def __init__(self, _id=None, _details=None, _loaded=False, _version=None, _vid=None, _label=None, _creationDate=None, _action=None, _lastUpdate=None, _barcode=None, _status=None, _numberOfSlots=None, _rows=None, _columns=None):
            if __builtin__.type(self) == _M_omero.model.TiterPlate:
                raise RuntimeError('omero.model.TiterPlate is an abstract class')
            _M_omero.model.SlottedContainer.__init__(self, _id, _details, _loaded, _version, _vid, _label, _creationDate, _action, _lastUpdate, _barcode, _status, _numberOfSlots)
            self._rows = _rows
            self._columns = _columns

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::model::Container', '::omero::model::IObject', '::omero::model::SlottedContainer', '::omero::model::TiterPlate', '::omero::model::VLCollection')

        def ice_id(self, current=None):
            return '::omero::model::TiterPlate'

        def ice_staticId():
            return '::omero::model::TiterPlate'
        ice_staticId = staticmethod(ice_staticId)

        def getRows(self, current=None):
            pass

        def setRows(self, theRows, current=None):
            pass

        def getColumns(self, current=None):
            pass

        def setColumns(self, theColumns, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.model._t_TiterPlate)

        __repr__ = __str__

    _M_omero.model.TiterPlatePrx = Ice.createTempClass()
    class TiterPlatePrx(_M_omero.model.SlottedContainerPrx):

        def getRows(self, _ctx=None):
            return _M_omero.model.TiterPlate._op_getRows.invoke(self, ((), _ctx))

        def begin_getRows(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.TiterPlate._op_getRows.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getRows(self, _r):
            return _M_omero.model.TiterPlate._op_getRows.end(self, _r)

        def setRows(self, theRows, _ctx=None):
            return _M_omero.model.TiterPlate._op_setRows.invoke(self, ((theRows, ), _ctx))

        def begin_setRows(self, theRows, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.TiterPlate._op_setRows.begin(self, ((theRows, ), _response, _ex, _sent, _ctx))

        def end_setRows(self, _r):
            return _M_omero.model.TiterPlate._op_setRows.end(self, _r)

        def getColumns(self, _ctx=None):
            return _M_omero.model.TiterPlate._op_getColumns.invoke(self, ((), _ctx))

        def begin_getColumns(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.TiterPlate._op_getColumns.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getColumns(self, _r):
            return _M_omero.model.TiterPlate._op_getColumns.end(self, _r)

        def setColumns(self, theColumns, _ctx=None):
            return _M_omero.model.TiterPlate._op_setColumns.invoke(self, ((theColumns, ), _ctx))

        def begin_setColumns(self, theColumns, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.TiterPlate._op_setColumns.begin(self, ((theColumns, ), _response, _ex, _sent, _ctx))

        def end_setColumns(self, _r):
            return _M_omero.model.TiterPlate._op_setColumns.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.model.TiterPlatePrx.ice_checkedCast(proxy, '::omero::model::TiterPlate', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.model.TiterPlatePrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_omero.model._t_TiterPlatePrx = IcePy.defineProxy('::omero::model::TiterPlate', TiterPlatePrx)

    _M_omero.model._t_TiterPlate = IcePy.declareClass('::omero::model::TiterPlate')

    _M_omero.model._t_TiterPlate = IcePy.defineClass('::omero::model::TiterPlate', TiterPlate, (), True, _M_omero.model._t_SlottedContainer, (), (
        ('_rows', (), _M_omero._t_RInt),
        ('_columns', (), _M_omero._t_RInt)
    ))
    TiterPlate._ice_type = _M_omero.model._t_TiterPlate

    TiterPlate._op_getRows = IcePy.Operation('getRows', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RInt, ())
    TiterPlate._op_setRows = IcePy.Operation('setRows', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RInt),), (), None, ())
    TiterPlate._op_getColumns = IcePy.Operation('getColumns', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RInt, ())
    TiterPlate._op_setColumns = IcePy.Operation('setColumns', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RInt),), (), None, ())

    _M_omero.model.TiterPlate = TiterPlate
    del TiterPlate

    _M_omero.model.TiterPlatePrx = TiterPlatePrx
    del TiterPlatePrx

# End of module omero.model

__name__ = 'omero'

# End of module omero
