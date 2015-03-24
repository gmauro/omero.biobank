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
# Generated from file `AnnotatedChip.ice'
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
import omero_model_Chip_ice

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

if not _M_omero.model.__dict__.has_key('OriginalFile'):
    _M_omero.model._t_OriginalFile = IcePy.declareClass('::omero::model::OriginalFile')
    _M_omero.model._t_OriginalFilePrx = IcePy.declareProxy('::omero::model::OriginalFile')

if not _M_omero.model.__dict__.has_key('Details'):
    _M_omero.model._t_Details = IcePy.declareClass('::omero::model::Details')
    _M_omero.model._t_DetailsPrx = IcePy.declareProxy('::omero::model::Details')

if not _M_omero.model.__dict__.has_key('AnnotatedChip'):
    _M_omero.model.AnnotatedChip = Ice.createTempClass()
    class AnnotatedChip(_M_omero.model.Chip):
        def __init__(self, _id=None, _details=None, _loaded=False, _version=None, _vid=None, _label=None, _maker=None, _model=None, _release=None, _barcode=None, _annotationFile=None):
            if __builtin__.type(self) == _M_omero.model.AnnotatedChip:
                raise RuntimeError('omero.model.AnnotatedChip is an abstract class')
            _M_omero.model.Chip.__init__(self, _id, _details, _loaded, _version, _vid, _label, _maker, _model, _release, _barcode)
            self._annotationFile = _annotationFile

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::model::AnnotatedChip', '::omero::model::Chip', '::omero::model::Device', '::omero::model::IObject')

        def ice_id(self, current=None):
            return '::omero::model::AnnotatedChip'

        def ice_staticId():
            return '::omero::model::AnnotatedChip'
        ice_staticId = staticmethod(ice_staticId)

        def getAnnotationFile(self, current=None):
            pass

        def setAnnotationFile(self, theAnnotationFile, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.model._t_AnnotatedChip)

        __repr__ = __str__

    _M_omero.model.AnnotatedChipPrx = Ice.createTempClass()
    class AnnotatedChipPrx(_M_omero.model.ChipPrx):

        def getAnnotationFile(self, _ctx=None):
            return _M_omero.model.AnnotatedChip._op_getAnnotationFile.invoke(self, ((), _ctx))

        def begin_getAnnotationFile(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.AnnotatedChip._op_getAnnotationFile.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getAnnotationFile(self, _r):
            return _M_omero.model.AnnotatedChip._op_getAnnotationFile.end(self, _r)

        def setAnnotationFile(self, theAnnotationFile, _ctx=None):
            return _M_omero.model.AnnotatedChip._op_setAnnotationFile.invoke(self, ((theAnnotationFile, ), _ctx))

        def begin_setAnnotationFile(self, theAnnotationFile, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.AnnotatedChip._op_setAnnotationFile.begin(self, ((theAnnotationFile, ), _response, _ex, _sent, _ctx))

        def end_setAnnotationFile(self, _r):
            return _M_omero.model.AnnotatedChip._op_setAnnotationFile.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.model.AnnotatedChipPrx.ice_checkedCast(proxy, '::omero::model::AnnotatedChip', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.model.AnnotatedChipPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_omero.model._t_AnnotatedChipPrx = IcePy.defineProxy('::omero::model::AnnotatedChip', AnnotatedChipPrx)

    _M_omero.model._t_AnnotatedChip = IcePy.declareClass('::omero::model::AnnotatedChip')

    _M_omero.model._t_AnnotatedChip = IcePy.defineClass('::omero::model::AnnotatedChip', AnnotatedChip, (), True, _M_omero.model._t_Chip, (), (('_annotationFile', (), _M_omero.model._t_OriginalFile),))
    AnnotatedChip._ice_type = _M_omero.model._t_AnnotatedChip

    AnnotatedChip._op_getAnnotationFile = IcePy.Operation('getAnnotationFile', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero.model._t_OriginalFile, ())
    AnnotatedChip._op_setAnnotationFile = IcePy.Operation('setAnnotationFile', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero.model._t_OriginalFile),), (), None, ())

    _M_omero.model.AnnotatedChip = AnnotatedChip
    del AnnotatedChip

    _M_omero.model.AnnotatedChipPrx = AnnotatedChipPrx
    del AnnotatedChipPrx

# End of module omero.model

__name__ = 'omero'

# End of module omero