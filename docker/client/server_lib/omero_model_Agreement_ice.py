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
# Generated from file `Agreement.ice'
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

if not _M_omero.model.__dict__.has_key('InformedConsent'):
    _M_omero.model._t_InformedConsent = IcePy.declareClass('::omero::model::InformedConsent')
    _M_omero.model._t_InformedConsentPrx = IcePy.declareProxy('::omero::model::InformedConsent')

if not _M_omero.model.__dict__.has_key('Enrollment'):
    _M_omero.model._t_Enrollment = IcePy.declareClass('::omero::model::Enrollment')
    _M_omero.model._t_EnrollmentPrx = IcePy.declareProxy('::omero::model::Enrollment')

if not _M_omero.model.__dict__.has_key('Details'):
    _M_omero.model._t_Details = IcePy.declareClass('::omero::model::Details')
    _M_omero.model._t_DetailsPrx = IcePy.declareProxy('::omero::model::Details')

if not _M_omero.model.__dict__.has_key('Agreement'):
    _M_omero.model.Agreement = Ice.createTempClass()
    class Agreement(_M_omero.model.IObject):
        def __init__(self, _id=None, _details=None, _loaded=False, _version=None, _vid=None, _refConsent=None, _enrollment=None, _submissionDate=None, _active=None):
            if __builtin__.type(self) == _M_omero.model.Agreement:
                raise RuntimeError('omero.model.Agreement is an abstract class')
            _M_omero.model.IObject.__init__(self, _id, _details, _loaded)
            self._version = _version
            self._vid = _vid
            self._refConsent = _refConsent
            self._enrollment = _enrollment
            self._submissionDate = _submissionDate
            self._active = _active

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::model::Agreement', '::omero::model::IObject')

        def ice_id(self, current=None):
            return '::omero::model::Agreement'

        def ice_staticId():
            return '::omero::model::Agreement'
        ice_staticId = staticmethod(ice_staticId)

        def getVersion(self, current=None):
            pass

        def setVersion(self, theVersion, current=None):
            pass

        def getVid(self, current=None):
            pass

        def setVid(self, theVid, current=None):
            pass

        def getRefConsent(self, current=None):
            pass

        def setRefConsent(self, theRefConsent, current=None):
            pass

        def getEnrollment(self, current=None):
            pass

        def setEnrollment(self, theEnrollment, current=None):
            pass

        def getSubmissionDate(self, current=None):
            pass

        def setSubmissionDate(self, theSubmissionDate, current=None):
            pass

        def getActive(self, current=None):
            pass

        def setActive(self, theActive, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.model._t_Agreement)

        __repr__ = __str__

    _M_omero.model.AgreementPrx = Ice.createTempClass()
    class AgreementPrx(_M_omero.model.IObjectPrx):

        def getVersion(self, _ctx=None):
            return _M_omero.model.Agreement._op_getVersion.invoke(self, ((), _ctx))

        def begin_getVersion(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Agreement._op_getVersion.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getVersion(self, _r):
            return _M_omero.model.Agreement._op_getVersion.end(self, _r)

        def setVersion(self, theVersion, _ctx=None):
            return _M_omero.model.Agreement._op_setVersion.invoke(self, ((theVersion, ), _ctx))

        def begin_setVersion(self, theVersion, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Agreement._op_setVersion.begin(self, ((theVersion, ), _response, _ex, _sent, _ctx))

        def end_setVersion(self, _r):
            return _M_omero.model.Agreement._op_setVersion.end(self, _r)

        def getVid(self, _ctx=None):
            return _M_omero.model.Agreement._op_getVid.invoke(self, ((), _ctx))

        def begin_getVid(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Agreement._op_getVid.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getVid(self, _r):
            return _M_omero.model.Agreement._op_getVid.end(self, _r)

        def setVid(self, theVid, _ctx=None):
            return _M_omero.model.Agreement._op_setVid.invoke(self, ((theVid, ), _ctx))

        def begin_setVid(self, theVid, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Agreement._op_setVid.begin(self, ((theVid, ), _response, _ex, _sent, _ctx))

        def end_setVid(self, _r):
            return _M_omero.model.Agreement._op_setVid.end(self, _r)

        def getRefConsent(self, _ctx=None):
            return _M_omero.model.Agreement._op_getRefConsent.invoke(self, ((), _ctx))

        def begin_getRefConsent(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Agreement._op_getRefConsent.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getRefConsent(self, _r):
            return _M_omero.model.Agreement._op_getRefConsent.end(self, _r)

        def setRefConsent(self, theRefConsent, _ctx=None):
            return _M_omero.model.Agreement._op_setRefConsent.invoke(self, ((theRefConsent, ), _ctx))

        def begin_setRefConsent(self, theRefConsent, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Agreement._op_setRefConsent.begin(self, ((theRefConsent, ), _response, _ex, _sent, _ctx))

        def end_setRefConsent(self, _r):
            return _M_omero.model.Agreement._op_setRefConsent.end(self, _r)

        def getEnrollment(self, _ctx=None):
            return _M_omero.model.Agreement._op_getEnrollment.invoke(self, ((), _ctx))

        def begin_getEnrollment(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Agreement._op_getEnrollment.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getEnrollment(self, _r):
            return _M_omero.model.Agreement._op_getEnrollment.end(self, _r)

        def setEnrollment(self, theEnrollment, _ctx=None):
            return _M_omero.model.Agreement._op_setEnrollment.invoke(self, ((theEnrollment, ), _ctx))

        def begin_setEnrollment(self, theEnrollment, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Agreement._op_setEnrollment.begin(self, ((theEnrollment, ), _response, _ex, _sent, _ctx))

        def end_setEnrollment(self, _r):
            return _M_omero.model.Agreement._op_setEnrollment.end(self, _r)

        def getSubmissionDate(self, _ctx=None):
            return _M_omero.model.Agreement._op_getSubmissionDate.invoke(self, ((), _ctx))

        def begin_getSubmissionDate(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Agreement._op_getSubmissionDate.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getSubmissionDate(self, _r):
            return _M_omero.model.Agreement._op_getSubmissionDate.end(self, _r)

        def setSubmissionDate(self, theSubmissionDate, _ctx=None):
            return _M_omero.model.Agreement._op_setSubmissionDate.invoke(self, ((theSubmissionDate, ), _ctx))

        def begin_setSubmissionDate(self, theSubmissionDate, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Agreement._op_setSubmissionDate.begin(self, ((theSubmissionDate, ), _response, _ex, _sent, _ctx))

        def end_setSubmissionDate(self, _r):
            return _M_omero.model.Agreement._op_setSubmissionDate.end(self, _r)

        def getActive(self, _ctx=None):
            return _M_omero.model.Agreement._op_getActive.invoke(self, ((), _ctx))

        def begin_getActive(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Agreement._op_getActive.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getActive(self, _r):
            return _M_omero.model.Agreement._op_getActive.end(self, _r)

        def setActive(self, theActive, _ctx=None):
            return _M_omero.model.Agreement._op_setActive.invoke(self, ((theActive, ), _ctx))

        def begin_setActive(self, theActive, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Agreement._op_setActive.begin(self, ((theActive, ), _response, _ex, _sent, _ctx))

        def end_setActive(self, _r):
            return _M_omero.model.Agreement._op_setActive.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.model.AgreementPrx.ice_checkedCast(proxy, '::omero::model::Agreement', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.model.AgreementPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_omero.model._t_AgreementPrx = IcePy.defineProxy('::omero::model::Agreement', AgreementPrx)

    _M_omero.model._t_Agreement = IcePy.declareClass('::omero::model::Agreement')

    _M_omero.model._t_Agreement = IcePy.defineClass('::omero::model::Agreement', Agreement, (), True, _M_omero.model._t_IObject, (), (
        ('_version', (), _M_omero._t_RInt),
        ('_vid', (), _M_omero._t_RString),
        ('_refConsent', (), _M_omero.model._t_InformedConsent),
        ('_enrollment', (), _M_omero.model._t_Enrollment),
        ('_submissionDate', (), _M_omero._t_RTime),
        ('_active', (), _M_omero._t_RBool)
    ))
    Agreement._ice_type = _M_omero.model._t_Agreement

    Agreement._op_getVersion = IcePy.Operation('getVersion', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RInt, ())
    Agreement._op_setVersion = IcePy.Operation('setVersion', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RInt),), (), None, ())
    Agreement._op_getVid = IcePy.Operation('getVid', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RString, ())
    Agreement._op_setVid = IcePy.Operation('setVid', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RString),), (), None, ())
    Agreement._op_getRefConsent = IcePy.Operation('getRefConsent', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero.model._t_InformedConsent, ())
    Agreement._op_setRefConsent = IcePy.Operation('setRefConsent', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero.model._t_InformedConsent),), (), None, ())
    Agreement._op_getEnrollment = IcePy.Operation('getEnrollment', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero.model._t_Enrollment, ())
    Agreement._op_setEnrollment = IcePy.Operation('setEnrollment', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero.model._t_Enrollment),), (), None, ())
    Agreement._op_getSubmissionDate = IcePy.Operation('getSubmissionDate', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RTime, ())
    Agreement._op_setSubmissionDate = IcePy.Operation('setSubmissionDate', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RTime),), (), None, ())
    Agreement._op_getActive = IcePy.Operation('getActive', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RBool, ())
    Agreement._op_setActive = IcePy.Operation('setActive', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RBool),), (), None, ())

    _M_omero.model.Agreement = Agreement
    del Agreement

    _M_omero.model.AgreementPrx = AgreementPrx
    del AgreementPrx

# End of module omero.model

__name__ = 'omero'

# End of module omero
