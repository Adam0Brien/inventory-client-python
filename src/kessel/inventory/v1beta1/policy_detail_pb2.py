# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kessel/inventory/v1beta1/policy_detail.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,kessel/inventory/v1beta1/policy_detail.proto\x12\x1c\x61pi.kessel.inventory.v1beta1\"\xfd\x01\n\x0cPolicyDetail\x12\x14\n\x08\x64isabled\x18\xfc\xf4\x98\x81\x01 \x01(\x08\x12M\n\x08severity\x18\xff\xa5\xf4\xc0\x01 \x01(\x0e\x32\x37.api.kessel.inventory.v1beta1.PolicyDetail.SeverityEnum\"\x87\x01\n\x0cSeverityEnum\x12\x14\n\x10SeverityEnum_LOW\x10\x00\x12\x17\n\x13SeverityEnum_MEDIUM\x10\x01\x12\x15\n\x11SeverityEnum_HIGH\x10\x02\x12\x19\n\x15SeverityEnum_CRITICAL\x10\x03\x12\x16\n\x12SeverityEnum_OTHER\x10\x04\x42\x46\n\x1c\x61pi.kessel.inventory.v1beta1P\x01Z$api/kessel/inventory/v1beta1;v1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'kessel.inventory.v1beta1.policy_detail_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034api.kessel.inventory.v1beta1P\001Z$api/kessel/inventory/v1beta1;v1beta1'
  _globals['_POLICYDETAIL']._serialized_start=79
  _globals['_POLICYDETAIL']._serialized_end=332
  _globals['_POLICYDETAIL_SEVERITYENUM']._serialized_start=197
  _globals['_POLICYDETAIL_SEVERITYENUM']._serialized_end=332
# @@protoc_insertion_point(module_scope)
