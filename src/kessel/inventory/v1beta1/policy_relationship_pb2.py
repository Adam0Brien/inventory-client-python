# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kessel/inventory/v1beta1/policy_relationship.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2kessel/inventory/v1beta1/policy_relationship.proto\x12\x1c\x61pi.kessel.inventory.v1beta1\"\xa4\x02\n\x12PolicyRelationship\x12\x1c\n\x11relationship_type\x18\xe4\xe9\xd7w \x01(\t\x12\x14\n\tpolicy_id\x18\xb8\xb1\xcek \x01(\x03\x12\x15\n\ncluster_id\x18\x80\xcb\xc9r \x01(\x03\x12O\n\x06status\x18\x8f\xe0\xc8\xa9\x01 \x01(\x0e\x32;.api.kessel.inventory.v1beta1.PolicyRelationship.StatusEnum\"r\n\nStatusEnum\x12\x18\n\x14StatusEnum_COMPLIANT\x10\x00\x12\x1c\n\x18StatusEnum_NON_COMPLIANT\x10\x01\x12\x14\n\x10StatusEnum_OTHER\x10\x02\x12\x16\n\x12StatusEnum_UNKNOWN\x10\x03\x42\x46\n\x1c\x61pi.kessel.inventory.v1beta1P\x01Z$api/kessel/inventory/v1beta1;v1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'kessel.inventory.v1beta1.policy_relationship_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034api.kessel.inventory.v1beta1P\001Z$api/kessel/inventory/v1beta1;v1beta1'
  _globals['_POLICYRELATIONSHIP']._serialized_start=85
  _globals['_POLICYRELATIONSHIP']._serialized_end=377
  _globals['_POLICYRELATIONSHIP_STATUSENUM']._serialized_start=263
  _globals['_POLICYRELATIONSHIP_STATUSENUM']._serialized_end=377
# @@protoc_insertion_point(module_scope)
