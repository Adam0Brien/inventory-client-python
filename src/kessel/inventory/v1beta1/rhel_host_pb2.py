# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kessel/inventory/v1beta1/rhel_host.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from kessel.inventory.v1beta1 import common_attributes_reporters_inner_pb2 as kessel_dot_inventory_dot_v1beta1_dot_common__attributes__reporters__inner__pb2
from kessel.inventory.v1beta1 import reporter_data_pb2 as kessel_dot_inventory_dot_v1beta1_dot_reporter__data__pb2
from kessel.inventory.v1beta1 import resource_tag_pb2 as kessel_dot_inventory_dot_v1beta1_dot_resource__tag__pb2

from kessel.inventory.v1beta1.common_attributes_reporters_inner_pb2 import *
from kessel.inventory.v1beta1.reporter_data_pb2 import *
from kessel.inventory.v1beta1.resource_tag_pb2 import *

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(kessel/inventory/v1beta1/rhel_host.proto\x12\x1c\x61pi.kessel.inventory.v1beta1\x1a@kessel/inventory/v1beta1/common_attributes_reporters_inner.proto\x1a,kessel/inventory/v1beta1/reporter_data.proto\x1a+kessel/inventory/v1beta1/resource_tag.proto\"\x95\x03\n\x08RHELHost\x12\x0b\n\x02id\x18\x9b\x1a \x01(\t\x12\x19\n\rresource_type\x18\xcc\xb9\x8f\xd3\x01 \x01(\t\x12\x19\n\x0e\x66irst_reported\x18\x80\xed\xce\x06 \x01(\t\x12\x1c\n\x11\x66irst_reported_by\x18\xb4\xc0\xfe\x15 \x01(\t\x12\x1b\n\x0flatest_reported\x18\x8b\x9d\x90\xd0\x01 \x01(\t\x12\x1e\n\x12latest_reported_by\x18\x8e\xa5\xe7\xf0\x01 \x01(\t\x12\x14\n\tworkspace\x18\x97\xd9\xdf\x10 \x01(\t\x12\x44\n\rreporter_data\x18\xc8\xd0\xfat \x01(\x0b\x32*.api.kessel.inventory.v1beta1.ReporterData\x12S\n\treporters\x18\xce\x90\xbd\xa8\x01 \x03(\x0b\x32<.api.kessel.inventory.v1beta1.CommonAttributesReportersInner\x12:\n\x04tags\x18\x99\xe8\xd8\x01 \x03(\x0b\x32).api.kessel.inventory.v1beta1.ResourceTagBF\n\x1c\x61pi.kessel.inventory.v1beta1P\x01Z$api/kessel/inventory/v1beta1;v1beta1P\x00P\x01P\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'kessel.inventory.v1beta1.rhel_host_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034api.kessel.inventory.v1beta1P\001Z$api/kessel/inventory/v1beta1;v1beta1'
  _globals['_RHELHOST']._serialized_start=232
  _globals['_RHELHOST']._serialized_end=637
# @@protoc_insertion_point(module_scope)
