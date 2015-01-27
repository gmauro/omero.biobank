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
# Generated from file `ActionOnDataSample.ice'
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
import omero_model_Action_ice

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

if not _M_omero.model.__dict__.has_key('ActionSetup'):
    _M_omero.model._t_ActionSetup = IcePy.declareClass('::omero::model::ActionSetup')
    _M_omero.model._t_ActionSetupPrx = IcePy.declareProxy('::omero::model::ActionSetup')

if not _M_omero.model.__dict__.has_key('Device'):
    _M_omero.model._t_Device = IcePy.declareClass('::omero::model::Device')
    _M_omero.model._t_DevicePrx = IcePy.declareProxy('::omero::model::Device')

if not _M_omero.model.__dict__.has_key('ActionCategory'):
    _M_omero.model._t_ActionCategory = IcePy.declareClass('::omero::model::ActionCategory')
    _M_omero.model._t_ActionCategoryPrx = IcePy.declareProxy('::omero::model::ActionCategory')

if not _M_omero.model.__dict__.has_key('Study'):
    _M_omero.model._t_Study = IcePy.declareClass('::omero::model::Study')
    _M_omero.model._t_StudyPrx = IcePy.declareProxy('::omero::model::Study')

if not _M_omero.model.__dict__.has_key('Details'):
    _M_omero.model._t_Details = IcePy.declareClass('::omero::model::Details')
    _M_omero.model._t_DetailsPrx = IcePy.declareProxy('::omero::model::Details')

if not _M_omero.model.__dict__.has_key('ActionOnDataSample'):
    _M_omero.model.ActionOnDataSample = Ice.createTempClass()
    class ActionOnDataSample(_M_omero.model.Action):
        def __init__(self, _id=None, _details=None, _loaded=False, _version=None, _vid=None, _beginTime=None, _endTime=None, _setup=None, _device=None, _actionCategory=None, _operator=None, _context=None, _description=None, _target=None):
            if __builtin__.type(self) == _M_omero.model.ActionOnDataSample:
                raise RuntimeError('omero.model.ActionOnDataSample is an abstract class')
            _M_omero.model.Action.__init__(self, _id, _details, _loaded, _version, _vid, _beginTime, _endTime, _setup, _device, _actionCategory, _operator, _context, _description)
            self._target = _target

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::model::Action', '::omero::model::ActionOnDataSample', '::omero::model::IObject')

        def ice_id(self, current=None):
            return '::omero::model::ActionOnDataSample'

        def ice_staticId():
            return '::omero::model::ActionOnDataSample'
        ice_staticId = staticmethod(ice_staticId)

        def getTarget(self, current=None):
            pass

        def setTarget(self, theTarget, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.model._t_ActionOnDataSample)

        __repr__ = __str__

    _M_omero.model.ActionOnDataSamplePrx = Ice.createTempClass()
    class ActionOnDataSamplePrx(_M_omero.model.ActionPrx):

        def getTarget(self, _ctx=None):
            return _M_omero.model.ActionOnDataSample._op_getTarget.invoke(self, ((), _ctx))

        def begin_getTarget(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ActionOnDataSample._op_getTarget.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getTarget(self, _r):
            return _M_omero.model.ActionOnDataSample._op_getTarget.end(self, _r)

        def setTarget(self, theTarget, _ctx=None):
            return _M_omero.model.ActionOnDataSample._op_setTarget.invoke(self, ((theTarget, ), _ctx))

        def begin_setTarget(self, theTarget, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ActionOnDataSample._op_setTarget.begin(self, ((theTarget, ), _response, _ex, _sent, _ctx))

        def end_setTarget(self, _r):
            return _M_omero.model.ActionOnDataSample._op_setTarget.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.model.ActionOnDataSamplePrx.ice_checkedCast(proxy, '::omero::model::ActionOnDataSample', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.model.ActionOnDataSamplePrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_omero.model._t_ActionOnDataSamplePrx = IcePy.defineProxy('::omero::model::ActionOnDataSample', ActionOnDataSamplePrx)

    _M_omero.model._t_ActionOnDataSample = IcePy.declareClass('::omero::model::ActionOnDataSample')

    _M_omero.model._t_ActionOnDataSample = IcePy.defineClass('::omero::model::ActionOnDataSample', ActionOnDataSample, (), True, _M_omero.model._t_Action, (), (('_target', (), _M_omero.model._t_DataSample),))
    ActionOnDataSample._ice_type = _M_omero.model._t_ActionOnDataSample

    ActionOnDataSample._op_getTarget = IcePy.Operation('getTarget', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero.model._t_DataSample, ())
    ActionOnDataSample._op_setTarget = IcePy.Operation('setTarget', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero.model._t_DataSample),), (), None, ())

    _M_omero.model.ActionOnDataSample = ActionOnDataSample
    del ActionOnDataSample

    _M_omero.model.ActionOnDataSamplePrx = ActionOnDataSamplePrx
    del ActionOnDataSamplePrx

# End of module omero.model

__name__ = 'omero'

# End of module omero
