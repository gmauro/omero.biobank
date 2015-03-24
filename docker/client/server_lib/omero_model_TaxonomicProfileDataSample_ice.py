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
# Generated from file `TaxonomicProfileDataSample.ice'
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

if not _M_omero.model.__dict__.has_key('DataSampleStatus'):
    _M_omero.model._t_DataSampleStatus = IcePy.declareClass('::omero::model::DataSampleStatus')
    _M_omero.model._t_DataSampleStatusPrx = IcePy.declareProxy('::omero::model::DataSampleStatus')

if not _M_omero.model.__dict__.has_key('Action'):
    _M_omero.model._t_Action = IcePy.declareClass('::omero::model::Action')
    _M_omero.model._t_ActionPrx = IcePy.declareProxy('::omero::model::Action')

if not _M_omero.model.__dict__.has_key('Details'):
    _M_omero.model._t_Details = IcePy.declareClass('::omero::model::Details')
    _M_omero.model._t_DetailsPrx = IcePy.declareProxy('::omero::model::Details')

if not _M_omero.model.__dict__.has_key('TaxonomicProfileDataSample'):
    _M_omero.model.TaxonomicProfileDataSample = Ice.createTempClass()
    class TaxonomicProfileDataSample(_M_omero.model.DataSample):
        def __init__(self, _id=None, _details=None, _loaded=False, _version=None, _vid=None, _label=None, _creationDate=None, _status=None, _action=None):
            if __builtin__.type(self) == _M_omero.model.TaxonomicProfileDataSample:
                raise RuntimeError('omero.model.TaxonomicProfileDataSample is an abstract class')
            _M_omero.model.DataSample.__init__(self, _id, _details, _loaded, _version, _vid, _label, _creationDate, _status, _action)

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::model::DataSample', '::omero::model::IObject', '::omero::model::TaxonomicProfileDataSample')

        def ice_id(self, current=None):
            return '::omero::model::TaxonomicProfileDataSample'

        def ice_staticId():
            return '::omero::model::TaxonomicProfileDataSample'
        ice_staticId = staticmethod(ice_staticId)

        def __str__(self):
            return IcePy.stringify(self, _M_omero.model._t_TaxonomicProfileDataSample)

        __repr__ = __str__

    _M_omero.model.TaxonomicProfileDataSamplePrx = Ice.createTempClass()
    class TaxonomicProfileDataSamplePrx(_M_omero.model.DataSamplePrx):

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.model.TaxonomicProfileDataSamplePrx.ice_checkedCast(proxy, '::omero::model::TaxonomicProfileDataSample', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.model.TaxonomicProfileDataSamplePrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_omero.model._t_TaxonomicProfileDataSamplePrx = IcePy.defineProxy('::omero::model::TaxonomicProfileDataSample', TaxonomicProfileDataSamplePrx)

    _M_omero.model._t_TaxonomicProfileDataSample = IcePy.declareClass('::omero::model::TaxonomicProfileDataSample')

    _M_omero.model._t_TaxonomicProfileDataSample = IcePy.defineClass('::omero::model::TaxonomicProfileDataSample', TaxonomicProfileDataSample, (), True, _M_omero.model._t_DataSample, (), ())
    TaxonomicProfileDataSample._ice_type = _M_omero.model._t_TaxonomicProfileDataSample

    _M_omero.model.TaxonomicProfileDataSample = TaxonomicProfileDataSample
    del TaxonomicProfileDataSample

    _M_omero.model.TaxonomicProfileDataSamplePrx = TaxonomicProfileDataSamplePrx
    del TaxonomicProfileDataSamplePrx

# End of module omero.model

__name__ = 'omero'

# End of module omero