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
# Generated from file `GenomeVariationsDataSample.ice'
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
import omero_model_DataSample_ice

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

if not _M_omero.model.__dict__.has_key('ReferenceGenome'):
    _M_omero.model._t_ReferenceGenome = IcePy.declareClass('::omero::model::ReferenceGenome')
    _M_omero.model._t_ReferenceGenomePrx = IcePy.declareProxy('::omero::model::ReferenceGenome')

if not _M_omero.model.__dict__.has_key('DataSampleStatus'):
    _M_omero.model._t_DataSampleStatus = IcePy.declareClass('::omero::model::DataSampleStatus')
    _M_omero.model._t_DataSampleStatusPrx = IcePy.declareProxy('::omero::model::DataSampleStatus')

if not _M_omero.model.__dict__.has_key('Action'):
    _M_omero.model._t_Action = IcePy.declareClass('::omero::model::Action')
    _M_omero.model._t_ActionPrx = IcePy.declareProxy('::omero::model::Action')

if not _M_omero.model.__dict__.has_key('Details'):
    _M_omero.model._t_Details = IcePy.declareClass('::omero::model::Details')
    _M_omero.model._t_DetailsPrx = IcePy.declareProxy('::omero::model::Details')

if not _M_omero.model.__dict__.has_key('GenomeVariationsDataSample'):
    _M_omero.model.GenomeVariationsDataSample = Ice.createTempClass()
    class GenomeVariationsDataSample(_M_omero.model.DataSample):
        def __init__(self, _id=None, _details=None, _loaded=False, _version=None, _vid=None, _label=None, _creationDate=None, _status=None, _action=None, _referenceGenome=None):
            if __builtin__.type(self) == _M_omero.model.GenomeVariationsDataSample:
                raise RuntimeError('omero.model.GenomeVariationsDataSample is an abstract class')
            _M_omero.model.DataSample.__init__(self, _id, _details, _loaded, _version, _vid, _label, _creationDate, _status, _action)
            self._referenceGenome = _referenceGenome

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::model::DataSample', '::omero::model::GenomeVariationsDataSample', '::omero::model::IObject')

        def ice_id(self, current=None):
            return '::omero::model::GenomeVariationsDataSample'

        def ice_staticId():
            return '::omero::model::GenomeVariationsDataSample'
        ice_staticId = staticmethod(ice_staticId)

        def getReferenceGenome(self, current=None):
            pass

        def setReferenceGenome(self, theReferenceGenome, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.model._t_GenomeVariationsDataSample)

        __repr__ = __str__

    _M_omero.model.GenomeVariationsDataSamplePrx = Ice.createTempClass()
    class GenomeVariationsDataSamplePrx(_M_omero.model.DataSamplePrx):

        def getReferenceGenome(self, _ctx=None):
            return _M_omero.model.GenomeVariationsDataSample._op_getReferenceGenome.invoke(self, ((), _ctx))

        def begin_getReferenceGenome(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.GenomeVariationsDataSample._op_getReferenceGenome.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getReferenceGenome(self, _r):
            return _M_omero.model.GenomeVariationsDataSample._op_getReferenceGenome.end(self, _r)

        def setReferenceGenome(self, theReferenceGenome, _ctx=None):
            return _M_omero.model.GenomeVariationsDataSample._op_setReferenceGenome.invoke(self, ((theReferenceGenome, ), _ctx))

        def begin_setReferenceGenome(self, theReferenceGenome, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.GenomeVariationsDataSample._op_setReferenceGenome.begin(self, ((theReferenceGenome, ), _response, _ex, _sent, _ctx))

        def end_setReferenceGenome(self, _r):
            return _M_omero.model.GenomeVariationsDataSample._op_setReferenceGenome.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.model.GenomeVariationsDataSamplePrx.ice_checkedCast(proxy, '::omero::model::GenomeVariationsDataSample', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.model.GenomeVariationsDataSamplePrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_omero.model._t_GenomeVariationsDataSamplePrx = IcePy.defineProxy('::omero::model::GenomeVariationsDataSample', GenomeVariationsDataSamplePrx)

    _M_omero.model._t_GenomeVariationsDataSample = IcePy.declareClass('::omero::model::GenomeVariationsDataSample')

    _M_omero.model._t_GenomeVariationsDataSample = IcePy.defineClass('::omero::model::GenomeVariationsDataSample', GenomeVariationsDataSample, (), True, _M_omero.model._t_DataSample, (), (('_referenceGenome', (), _M_omero.model._t_ReferenceGenome),))
    GenomeVariationsDataSample._ice_type = _M_omero.model._t_GenomeVariationsDataSample

    GenomeVariationsDataSample._op_getReferenceGenome = IcePy.Operation('getReferenceGenome', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero.model._t_ReferenceGenome, ())
    GenomeVariationsDataSample._op_setReferenceGenome = IcePy.Operation('setReferenceGenome', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero.model._t_ReferenceGenome),), (), None, ())

    _M_omero.model.GenomeVariationsDataSample = GenomeVariationsDataSample
    del GenomeVariationsDataSample

    _M_omero.model.GenomeVariationsDataSamplePrx = GenomeVariationsDataSamplePrx
    del GenomeVariationsDataSamplePrx

# End of module omero.model

__name__ = 'omero'

# End of module omero
