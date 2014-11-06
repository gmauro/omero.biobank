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
# Generated from file `Vessel.ice'
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

if not _M_omero.model.__dict__.has_key('VesselContent'):
    _M_omero.model._t_VesselContent = IcePy.declareClass('::omero::model::VesselContent')
    _M_omero.model._t_VesselContentPrx = IcePy.declareProxy('::omero::model::VesselContent')

if not _M_omero.model.__dict__.has_key('VesselStatus'):
    _M_omero.model._t_VesselStatus = IcePy.declareClass('::omero::model::VesselStatus')
    _M_omero.model._t_VesselStatusPrx = IcePy.declareProxy('::omero::model::VesselStatus')

if not _M_omero.model.__dict__.has_key('Action'):
    _M_omero.model._t_Action = IcePy.declareClass('::omero::model::Action')
    _M_omero.model._t_ActionPrx = IcePy.declareProxy('::omero::model::Action')

if not _M_omero.model.__dict__.has_key('Details'):
    _M_omero.model._t_Details = IcePy.declareClass('::omero::model::Details')
    _M_omero.model._t_DetailsPrx = IcePy.declareProxy('::omero::model::Details')

if not _M_omero.model.__dict__.has_key('Vessel'):
    _M_omero.model.Vessel = Ice.createTempClass()
    class Vessel(_M_omero.model.IObject):
        def __init__(self, _id=None, _details=None, _loaded=False, _version=None, _vid=None, _activationDate=None, _destructionDate=None, _currentVolume=None, _initialVolume=None, _content=None, _status=None, _action=None, _lastUpdate=None):
            if __builtin__.type(self) == _M_omero.model.Vessel:
                raise RuntimeError('omero.model.Vessel is an abstract class')
            _M_omero.model.IObject.__init__(self, _id, _details, _loaded)
            self._version = _version
            self._vid = _vid
            self._activationDate = _activationDate
            self._destructionDate = _destructionDate
            self._currentVolume = _currentVolume
            self._initialVolume = _initialVolume
            self._content = _content
            self._status = _status
            self._action = _action
            self._lastUpdate = _lastUpdate

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::model::IObject', '::omero::model::Vessel')

        def ice_id(self, current=None):
            return '::omero::model::Vessel'

        def ice_staticId():
            return '::omero::model::Vessel'
        ice_staticId = staticmethod(ice_staticId)

        def getVersion(self, current=None):
            pass

        def setVersion(self, theVersion, current=None):
            pass

        def getVid(self, current=None):
            pass

        def setVid(self, theVid, current=None):
            pass

        def getActivationDate(self, current=None):
            pass

        def setActivationDate(self, theActivationDate, current=None):
            pass

        def getDestructionDate(self, current=None):
            pass

        def setDestructionDate(self, theDestructionDate, current=None):
            pass

        def getCurrentVolume(self, current=None):
            pass

        def setCurrentVolume(self, theCurrentVolume, current=None):
            pass

        def getInitialVolume(self, current=None):
            pass

        def setInitialVolume(self, theInitialVolume, current=None):
            pass

        def getContent(self, current=None):
            pass

        def setContent(self, theContent, current=None):
            pass

        def getStatus(self, current=None):
            pass

        def setStatus(self, theStatus, current=None):
            pass

        def getAction(self, current=None):
            pass

        def setAction(self, theAction, current=None):
            pass

        def getLastUpdate(self, current=None):
            pass

        def setLastUpdate(self, theLastUpdate, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.model._t_Vessel)

        __repr__ = __str__

    _M_omero.model.VesselPrx = Ice.createTempClass()
    class VesselPrx(_M_omero.model.IObjectPrx):

        def getVersion(self, _ctx=None):
            return _M_omero.model.Vessel._op_getVersion.invoke(self, ((), _ctx))

        def begin_getVersion(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Vessel._op_getVersion.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getVersion(self, _r):
            return _M_omero.model.Vessel._op_getVersion.end(self, _r)

        def setVersion(self, theVersion, _ctx=None):
            return _M_omero.model.Vessel._op_setVersion.invoke(self, ((theVersion, ), _ctx))

        def begin_setVersion(self, theVersion, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Vessel._op_setVersion.begin(self, ((theVersion, ), _response, _ex, _sent, _ctx))

        def end_setVersion(self, _r):
            return _M_omero.model.Vessel._op_setVersion.end(self, _r)

        def getVid(self, _ctx=None):
            return _M_omero.model.Vessel._op_getVid.invoke(self, ((), _ctx))

        def begin_getVid(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Vessel._op_getVid.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getVid(self, _r):
            return _M_omero.model.Vessel._op_getVid.end(self, _r)

        def setVid(self, theVid, _ctx=None):
            return _M_omero.model.Vessel._op_setVid.invoke(self, ((theVid, ), _ctx))

        def begin_setVid(self, theVid, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Vessel._op_setVid.begin(self, ((theVid, ), _response, _ex, _sent, _ctx))

        def end_setVid(self, _r):
            return _M_omero.model.Vessel._op_setVid.end(self, _r)

        def getActivationDate(self, _ctx=None):
            return _M_omero.model.Vessel._op_getActivationDate.invoke(self, ((), _ctx))

        def begin_getActivationDate(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Vessel._op_getActivationDate.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getActivationDate(self, _r):
            return _M_omero.model.Vessel._op_getActivationDate.end(self, _r)

        def setActivationDate(self, theActivationDate, _ctx=None):
            return _M_omero.model.Vessel._op_setActivationDate.invoke(self, ((theActivationDate, ), _ctx))

        def begin_setActivationDate(self, theActivationDate, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Vessel._op_setActivationDate.begin(self, ((theActivationDate, ), _response, _ex, _sent, _ctx))

        def end_setActivationDate(self, _r):
            return _M_omero.model.Vessel._op_setActivationDate.end(self, _r)

        def getDestructionDate(self, _ctx=None):
            return _M_omero.model.Vessel._op_getDestructionDate.invoke(self, ((), _ctx))

        def begin_getDestructionDate(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Vessel._op_getDestructionDate.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getDestructionDate(self, _r):
            return _M_omero.model.Vessel._op_getDestructionDate.end(self, _r)

        def setDestructionDate(self, theDestructionDate, _ctx=None):
            return _M_omero.model.Vessel._op_setDestructionDate.invoke(self, ((theDestructionDate, ), _ctx))

        def begin_setDestructionDate(self, theDestructionDate, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Vessel._op_setDestructionDate.begin(self, ((theDestructionDate, ), _response, _ex, _sent, _ctx))

        def end_setDestructionDate(self, _r):
            return _M_omero.model.Vessel._op_setDestructionDate.end(self, _r)

        def getCurrentVolume(self, _ctx=None):
            return _M_omero.model.Vessel._op_getCurrentVolume.invoke(self, ((), _ctx))

        def begin_getCurrentVolume(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Vessel._op_getCurrentVolume.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getCurrentVolume(self, _r):
            return _M_omero.model.Vessel._op_getCurrentVolume.end(self, _r)

        def setCurrentVolume(self, theCurrentVolume, _ctx=None):
            return _M_omero.model.Vessel._op_setCurrentVolume.invoke(self, ((theCurrentVolume, ), _ctx))

        def begin_setCurrentVolume(self, theCurrentVolume, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Vessel._op_setCurrentVolume.begin(self, ((theCurrentVolume, ), _response, _ex, _sent, _ctx))

        def end_setCurrentVolume(self, _r):
            return _M_omero.model.Vessel._op_setCurrentVolume.end(self, _r)

        def getInitialVolume(self, _ctx=None):
            return _M_omero.model.Vessel._op_getInitialVolume.invoke(self, ((), _ctx))

        def begin_getInitialVolume(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Vessel._op_getInitialVolume.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getInitialVolume(self, _r):
            return _M_omero.model.Vessel._op_getInitialVolume.end(self, _r)

        def setInitialVolume(self, theInitialVolume, _ctx=None):
            return _M_omero.model.Vessel._op_setInitialVolume.invoke(self, ((theInitialVolume, ), _ctx))

        def begin_setInitialVolume(self, theInitialVolume, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Vessel._op_setInitialVolume.begin(self, ((theInitialVolume, ), _response, _ex, _sent, _ctx))

        def end_setInitialVolume(self, _r):
            return _M_omero.model.Vessel._op_setInitialVolume.end(self, _r)

        def getContent(self, _ctx=None):
            return _M_omero.model.Vessel._op_getContent.invoke(self, ((), _ctx))

        def begin_getContent(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Vessel._op_getContent.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getContent(self, _r):
            return _M_omero.model.Vessel._op_getContent.end(self, _r)

        def setContent(self, theContent, _ctx=None):
            return _M_omero.model.Vessel._op_setContent.invoke(self, ((theContent, ), _ctx))

        def begin_setContent(self, theContent, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Vessel._op_setContent.begin(self, ((theContent, ), _response, _ex, _sent, _ctx))

        def end_setContent(self, _r):
            return _M_omero.model.Vessel._op_setContent.end(self, _r)

        def getStatus(self, _ctx=None):
            return _M_omero.model.Vessel._op_getStatus.invoke(self, ((), _ctx))

        def begin_getStatus(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Vessel._op_getStatus.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getStatus(self, _r):
            return _M_omero.model.Vessel._op_getStatus.end(self, _r)

        def setStatus(self, theStatus, _ctx=None):
            return _M_omero.model.Vessel._op_setStatus.invoke(self, ((theStatus, ), _ctx))

        def begin_setStatus(self, theStatus, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Vessel._op_setStatus.begin(self, ((theStatus, ), _response, _ex, _sent, _ctx))

        def end_setStatus(self, _r):
            return _M_omero.model.Vessel._op_setStatus.end(self, _r)

        def getAction(self, _ctx=None):
            return _M_omero.model.Vessel._op_getAction.invoke(self, ((), _ctx))

        def begin_getAction(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Vessel._op_getAction.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getAction(self, _r):
            return _M_omero.model.Vessel._op_getAction.end(self, _r)

        def setAction(self, theAction, _ctx=None):
            return _M_omero.model.Vessel._op_setAction.invoke(self, ((theAction, ), _ctx))

        def begin_setAction(self, theAction, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Vessel._op_setAction.begin(self, ((theAction, ), _response, _ex, _sent, _ctx))

        def end_setAction(self, _r):
            return _M_omero.model.Vessel._op_setAction.end(self, _r)

        def getLastUpdate(self, _ctx=None):
            return _M_omero.model.Vessel._op_getLastUpdate.invoke(self, ((), _ctx))

        def begin_getLastUpdate(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Vessel._op_getLastUpdate.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getLastUpdate(self, _r):
            return _M_omero.model.Vessel._op_getLastUpdate.end(self, _r)

        def setLastUpdate(self, theLastUpdate, _ctx=None):
            return _M_omero.model.Vessel._op_setLastUpdate.invoke(self, ((theLastUpdate, ), _ctx))

        def begin_setLastUpdate(self, theLastUpdate, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Vessel._op_setLastUpdate.begin(self, ((theLastUpdate, ), _response, _ex, _sent, _ctx))

        def end_setLastUpdate(self, _r):
            return _M_omero.model.Vessel._op_setLastUpdate.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.model.VesselPrx.ice_checkedCast(proxy, '::omero::model::Vessel', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.model.VesselPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_omero.model._t_VesselPrx = IcePy.defineProxy('::omero::model::Vessel', VesselPrx)

    _M_omero.model._t_Vessel = IcePy.declareClass('::omero::model::Vessel')

    _M_omero.model._t_Vessel = IcePy.defineClass('::omero::model::Vessel', Vessel, (), True, _M_omero.model._t_IObject, (), (
        ('_version', (), _M_omero._t_RInt),
        ('_vid', (), _M_omero._t_RString),
        ('_activationDate', (), _M_omero._t_RTime),
        ('_destructionDate', (), _M_omero._t_RTime),
        ('_currentVolume', (), _M_omero._t_RFloat),
        ('_initialVolume', (), _M_omero._t_RFloat),
        ('_content', (), _M_omero.model._t_VesselContent),
        ('_status', (), _M_omero.model._t_VesselStatus),
        ('_action', (), _M_omero.model._t_Action),
        ('_lastUpdate', (), _M_omero.model._t_Action)
    ))
    Vessel._ice_type = _M_omero.model._t_Vessel

    Vessel._op_getVersion = IcePy.Operation('getVersion', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RInt, ())
    Vessel._op_setVersion = IcePy.Operation('setVersion', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RInt),), (), None, ())
    Vessel._op_getVid = IcePy.Operation('getVid', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RString, ())
    Vessel._op_setVid = IcePy.Operation('setVid', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RString),), (), None, ())
    Vessel._op_getActivationDate = IcePy.Operation('getActivationDate', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RTime, ())
    Vessel._op_setActivationDate = IcePy.Operation('setActivationDate', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RTime),), (), None, ())
    Vessel._op_getDestructionDate = IcePy.Operation('getDestructionDate', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RTime, ())
    Vessel._op_setDestructionDate = IcePy.Operation('setDestructionDate', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RTime),), (), None, ())
    Vessel._op_getCurrentVolume = IcePy.Operation('getCurrentVolume', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RFloat, ())
    Vessel._op_setCurrentVolume = IcePy.Operation('setCurrentVolume', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RFloat),), (), None, ())
    Vessel._op_getInitialVolume = IcePy.Operation('getInitialVolume', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RFloat, ())
    Vessel._op_setInitialVolume = IcePy.Operation('setInitialVolume', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RFloat),), (), None, ())
    Vessel._op_getContent = IcePy.Operation('getContent', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero.model._t_VesselContent, ())
    Vessel._op_setContent = IcePy.Operation('setContent', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero.model._t_VesselContent),), (), None, ())
    Vessel._op_getStatus = IcePy.Operation('getStatus', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero.model._t_VesselStatus, ())
    Vessel._op_setStatus = IcePy.Operation('setStatus', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero.model._t_VesselStatus),), (), None, ())
    Vessel._op_getAction = IcePy.Operation('getAction', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero.model._t_Action, ())
    Vessel._op_setAction = IcePy.Operation('setAction', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero.model._t_Action),), (), None, ())
    Vessel._op_getLastUpdate = IcePy.Operation('getLastUpdate', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero.model._t_Action, ())
    Vessel._op_setLastUpdate = IcePy.Operation('setLastUpdate', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero.model._t_Action),), (), None, ())

    _M_omero.model.Vessel = Vessel
    del Vessel

    _M_omero.model.VesselPrx = VesselPrx
    del VesselPrx

# End of module omero.model

__name__ = 'omero'

# End of module omero
