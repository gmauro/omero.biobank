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
# Generated from file `HardwareDevice.ice'
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
import omero_model_Device_ice

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

if not _M_omero.model.__dict__.has_key('Details'):
    _M_omero.model._t_Details = IcePy.declareClass('::omero::model::Details')
    _M_omero.model._t_DetailsPrx = IcePy.declareProxy('::omero::model::Details')

if not _M_omero.model.__dict__.has_key('HardwareDevice'):
    _M_omero.model.HardwareDevice = Ice.createTempClass()
    class HardwareDevice(_M_omero.model.Device):
        def __init__(self, _id=None, _details=None, _loaded=False, _version=None, _vid=None, _label=None, _maker=None, _model=None, _release=None, _barcode=None, _physicalLocation=None):
            if __builtin__.type(self) == _M_omero.model.HardwareDevice:
                raise RuntimeError('omero.model.HardwareDevice is an abstract class')
            _M_omero.model.Device.__init__(self, _id, _details, _loaded, _version, _vid, _label, _maker, _model, _release)
            self._barcode = _barcode
            self._physicalLocation = _physicalLocation

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::model::Device', '::omero::model::HardwareDevice', '::omero::model::IObject')

        def ice_id(self, current=None):
            return '::omero::model::HardwareDevice'

        def ice_staticId():
            return '::omero::model::HardwareDevice'
        ice_staticId = staticmethod(ice_staticId)

        def getBarcode(self, current=None):
            pass

        def setBarcode(self, theBarcode, current=None):
            pass

        def getPhysicalLocation(self, current=None):
            pass

        def setPhysicalLocation(self, thePhysicalLocation, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.model._t_HardwareDevice)

        __repr__ = __str__

    _M_omero.model.HardwareDevicePrx = Ice.createTempClass()
    class HardwareDevicePrx(_M_omero.model.DevicePrx):

        def getBarcode(self, _ctx=None):
            return _M_omero.model.HardwareDevice._op_getBarcode.invoke(self, ((), _ctx))

        def begin_getBarcode(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.HardwareDevice._op_getBarcode.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getBarcode(self, _r):
            return _M_omero.model.HardwareDevice._op_getBarcode.end(self, _r)

        def setBarcode(self, theBarcode, _ctx=None):
            return _M_omero.model.HardwareDevice._op_setBarcode.invoke(self, ((theBarcode, ), _ctx))

        def begin_setBarcode(self, theBarcode, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.HardwareDevice._op_setBarcode.begin(self, ((theBarcode, ), _response, _ex, _sent, _ctx))

        def end_setBarcode(self, _r):
            return _M_omero.model.HardwareDevice._op_setBarcode.end(self, _r)

        def getPhysicalLocation(self, _ctx=None):
            return _M_omero.model.HardwareDevice._op_getPhysicalLocation.invoke(self, ((), _ctx))

        def begin_getPhysicalLocation(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.HardwareDevice._op_getPhysicalLocation.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getPhysicalLocation(self, _r):
            return _M_omero.model.HardwareDevice._op_getPhysicalLocation.end(self, _r)

        def setPhysicalLocation(self, thePhysicalLocation, _ctx=None):
            return _M_omero.model.HardwareDevice._op_setPhysicalLocation.invoke(self, ((thePhysicalLocation, ), _ctx))

        def begin_setPhysicalLocation(self, thePhysicalLocation, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.HardwareDevice._op_setPhysicalLocation.begin(self, ((thePhysicalLocation, ), _response, _ex, _sent, _ctx))

        def end_setPhysicalLocation(self, _r):
            return _M_omero.model.HardwareDevice._op_setPhysicalLocation.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.model.HardwareDevicePrx.ice_checkedCast(proxy, '::omero::model::HardwareDevice', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.model.HardwareDevicePrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_omero.model._t_HardwareDevicePrx = IcePy.defineProxy('::omero::model::HardwareDevice', HardwareDevicePrx)

    _M_omero.model._t_HardwareDevice = IcePy.declareClass('::omero::model::HardwareDevice')

    _M_omero.model._t_HardwareDevice = IcePy.defineClass('::omero::model::HardwareDevice', HardwareDevice, (), True, _M_omero.model._t_Device, (), (
        ('_barcode', (), _M_omero._t_RString),
        ('_physicalLocation', (), _M_omero._t_RString)
    ))
    HardwareDevice._ice_type = _M_omero.model._t_HardwareDevice

    HardwareDevice._op_getBarcode = IcePy.Operation('getBarcode', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RString, ())
    HardwareDevice._op_setBarcode = IcePy.Operation('setBarcode', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RString),), (), None, ())
    HardwareDevice._op_getPhysicalLocation = IcePy.Operation('getPhysicalLocation', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RString, ())
    HardwareDevice._op_setPhysicalLocation = IcePy.Operation('setPhysicalLocation', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RString),), (), None, ())

    _M_omero.model.HardwareDevice = HardwareDevice
    del HardwareDevice

    _M_omero.model.HardwareDevicePrx = HardwareDevicePrx
    del HardwareDevicePrx

# End of module omero.model

__name__ = 'omero'

# End of module omero
