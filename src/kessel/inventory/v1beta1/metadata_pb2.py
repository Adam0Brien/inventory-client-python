# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kessel/inventory/v1beta1/metadata.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from kessel.inventory.v1beta1 import resource_tag_pb2 as kessel_dot_inventory_dot_v1beta1_dot_resource__tag__pb2

from kessel.inventory.v1beta1.resource_tag_pb2 import *

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'kessel/inventory/v1beta1/metadata.proto\x12\x1c\x61pi.kessel.inventory.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a+kessel/inventory/v1beta1/resource_tag.proto\"\xcc\x02\n\x08Metadata\x12\x11\n\x02id\x18\x9b\x1a \x01(\x03\x42\x04\xe2\x41\x01\x03\x12\x19\n\rresource_type\x18\xcc\xb9\x8f\xd3\x01 \x01(\t\x12;\n\x0e\x66irst_reported\x18\x80\xed\xce\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03\x12;\n\rlast_reported\x18\x8b\x9d\x90\xd0\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03\x12\"\n\x11\x66irst_reported_by\x18\xb4\xc0\xfe\x15 \x01(\tB\x04\xe2\x41\x01\x03\x12\"\n\x10last_reported_by\x18\x8e\xa5\xe7\xf0\x01 \x01(\tB\x04\xe2\x41\x01\x03\x12\x14\n\tworkspace\x18\x97\xd9\xdf\x10 \x01(\t\x12:\n\x04tags\x18\x99\xe8\xd8\x01 \x03(\x0b\x32).api.kessel.inventory.v1beta1.ResourceTagBF\n\x1c\x61pi.kessel.inventory.v1beta1P\x01Z$api/kessel/inventory/v1beta1;v1beta1P\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'kessel.inventory.v1beta1.metadata_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034api.kessel.inventory.v1beta1P\001Z$api/kessel/inventory/v1beta1;v1beta1'
  _globals['_METADATA'].fields_by_name['id']._loaded_options = None
  _globals['_METADATA'].fields_by_name['id']._serialized_options = b'\342A\001\003'
  _globals['_METADATA'].fields_by_name['first_reported']._loaded_options = None
  _globals['_METADATA'].fields_by_name['first_reported']._serialized_options = b'\342A\001\003'
  _globals['_METADATA'].fields_by_name['last_reported']._loaded_options = None
  _globals['_METADATA'].fields_by_name['last_reported']._serialized_options = b'\342A\001\003'
  _globals['_METADATA'].fields_by_name['first_reported_by']._loaded_options = None
  _globals['_METADATA'].fields_by_name['first_reported_by']._serialized_options = b'\342A\001\003'
  _globals['_METADATA'].fields_by_name['last_reported_by']._loaded_options = None
  _globals['_METADATA'].fields_by_name['last_reported_by']._serialized_options = b'\342A\001\003'
  _globals['_METADATA']._serialized_start=185
  _globals['_METADATA']._serialized_end=517
# @@protoc_insertion_point(module_scope)
