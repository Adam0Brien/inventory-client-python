# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kessel/inventory/v1beta1/notifications_integrations_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from kessel.inventory.v1beta1 import notifications_integration_pb2 as kessel_dot_inventory_dot_v1beta1_dot_notifications__integration__pb2
try:
  kessel_dot_inventory_dot_v1beta1_dot_metadata__pb2 = kessel_dot_inventory_dot_v1beta1_dot_notifications__integration__pb2.kessel_dot_inventory_dot_v1beta1_dot_metadata__pb2
except AttributeError:
  kessel_dot_inventory_dot_v1beta1_dot_metadata__pb2 = kessel_dot_inventory_dot_v1beta1_dot_notifications__integration__pb2.kessel.inventory.v1beta1.metadata_pb2
try:
  kessel_dot_inventory_dot_v1beta1_dot_resource__tag__pb2 = kessel_dot_inventory_dot_v1beta1_dot_notifications__integration__pb2.kessel_dot_inventory_dot_v1beta1_dot_resource__tag__pb2
except AttributeError:
  kessel_dot_inventory_dot_v1beta1_dot_resource__tag__pb2 = kessel_dot_inventory_dot_v1beta1_dot_notifications__integration__pb2.kessel.inventory.v1beta1.resource_tag_pb2
try:
  kessel_dot_inventory_dot_v1beta1_dot_reporter__data__pb2 = kessel_dot_inventory_dot_v1beta1_dot_notifications__integration__pb2.kessel_dot_inventory_dot_v1beta1_dot_reporter__data__pb2
except AttributeError:
  kessel_dot_inventory_dot_v1beta1_dot_reporter__data__pb2 = kessel_dot_inventory_dot_v1beta1_dot_notifications__integration__pb2.kessel.inventory.v1beta1.reporter_data_pb2

from kessel.inventory.v1beta1.notifications_integration_pb2 import *

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAkessel/inventory/v1beta1/notifications_integrations_service.proto\x12\x1c\x61pi.kessel.inventory.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x38kessel/inventory/v1beta1/notifications_integration.proto\"z\n%CreateNotificationsIntegrationRequest\x12Q\n\x0bintegration\x18\x01 \x01(\x0b\x32\x36.api.kessel.inventory.v1beta1.NotificationsIntegrationB\x04\xe2\x41\x01\x02\"{\n&CreateNotificationsIntegrationResponse\x12Q\n\x0bintegration\x18\x01 \x01(\x0b\x32\x36.api.kessel.inventory.v1beta1.NotificationsIntegrationB\x04\xe2\x41\x01\x02\"\x92\x01\n%UpdateNotificationsIntegrationRequest\x12\x16\n\x08resource\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\x12Q\n\x0bintegration\x18\x02 \x01(\x0b\x32\x36.api.kessel.inventory.v1beta1.NotificationsIntegrationB\x04\xe2\x41\x01\x02\"(\n&UpdateNotificationsIntegrationResponse\"?\n%DeleteNotificationsIntegrationRequest\x12\x16\n\x08resource\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\"(\n&DeleteNotificationsIntegrationResponse2\x8a\x06\n NotificationsIntegrationsService\x12\xf2\x01\n\x1e\x43reateNotificationsIntegration\x12\x43.api.kessel.inventory.v1beta1.CreateNotificationsIntegrationRequest\x1a\x44.api.kessel.inventory.v1beta1.CreateNotificationsIntegrationResponse\"E\x82\xd3\xe4\x93\x02?\"0/api/inventory/v1beta1/notificationsintegrations:\x0bintegration\x12\xfd\x01\n\x1eUpdateNotificationsIntegration\x12\x43.api.kessel.inventory.v1beta1.UpdateNotificationsIntegrationRequest\x1a\x44.api.kessel.inventory.v1beta1.UpdateNotificationsIntegrationResponse\"P\x82\xd3\xe4\x93\x02J\x1a;/api/inventory/v1beta1/notificationsintegrations/{resource}:\x0bintegration\x12\xf0\x01\n\x1e\x44\x65leteNotificationsIntegration\x12\x43.api.kessel.inventory.v1beta1.DeleteNotificationsIntegrationRequest\x1a\x44.api.kessel.inventory.v1beta1.DeleteNotificationsIntegrationResponse\"C\x82\xd3\xe4\x93\x02=*;/api/inventory/v1beta1/notificationsintegrations/{resource}BF\n\x1c\x61pi.kessel.inventory.v1beta1P\x01Z$api/kessel/inventory/v1beta1;v1beta1P\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'kessel.inventory.v1beta1.notifications_integrations_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034api.kessel.inventory.v1beta1P\001Z$api/kessel/inventory/v1beta1;v1beta1'
  _globals['_CREATENOTIFICATIONSINTEGRATIONREQUEST'].fields_by_name['integration']._loaded_options = None
  _globals['_CREATENOTIFICATIONSINTEGRATIONREQUEST'].fields_by_name['integration']._serialized_options = b'\342A\001\002'
  _globals['_CREATENOTIFICATIONSINTEGRATIONRESPONSE'].fields_by_name['integration']._loaded_options = None
  _globals['_CREATENOTIFICATIONSINTEGRATIONRESPONSE'].fields_by_name['integration']._serialized_options = b'\342A\001\002'
  _globals['_UPDATENOTIFICATIONSINTEGRATIONREQUEST'].fields_by_name['resource']._loaded_options = None
  _globals['_UPDATENOTIFICATIONSINTEGRATIONREQUEST'].fields_by_name['resource']._serialized_options = b'\342A\001\002'
  _globals['_UPDATENOTIFICATIONSINTEGRATIONREQUEST'].fields_by_name['integration']._loaded_options = None
  _globals['_UPDATENOTIFICATIONSINTEGRATIONREQUEST'].fields_by_name['integration']._serialized_options = b'\342A\001\002'
  _globals['_DELETENOTIFICATIONSINTEGRATIONREQUEST'].fields_by_name['resource']._loaded_options = None
  _globals['_DELETENOTIFICATIONSINTEGRATIONREQUEST'].fields_by_name['resource']._serialized_options = b'\342A\001\002'
  _globals['_NOTIFICATIONSINTEGRATIONSSERVICE'].methods_by_name['CreateNotificationsIntegration']._loaded_options = None
  _globals['_NOTIFICATIONSINTEGRATIONSSERVICE'].methods_by_name['CreateNotificationsIntegration']._serialized_options = b'\202\323\344\223\002?\"0/api/inventory/v1beta1/notificationsintegrations:\013integration'
  _globals['_NOTIFICATIONSINTEGRATIONSSERVICE'].methods_by_name['UpdateNotificationsIntegration']._loaded_options = None
  _globals['_NOTIFICATIONSINTEGRATIONSSERVICE'].methods_by_name['UpdateNotificationsIntegration']._serialized_options = b'\202\323\344\223\002J\032;/api/inventory/v1beta1/notificationsintegrations/{resource}:\013integration'
  _globals['_NOTIFICATIONSINTEGRATIONSSERVICE'].methods_by_name['DeleteNotificationsIntegration']._loaded_options = None
  _globals['_NOTIFICATIONSINTEGRATIONSSERVICE'].methods_by_name['DeleteNotificationsIntegration']._serialized_options = b'\202\323\344\223\002=*;/api/inventory/v1beta1/notificationsintegrations/{resource}'
  _globals['_CREATENOTIFICATIONSINTEGRATIONREQUEST']._serialized_start=220
  _globals['_CREATENOTIFICATIONSINTEGRATIONREQUEST']._serialized_end=342
  _globals['_CREATENOTIFICATIONSINTEGRATIONRESPONSE']._serialized_start=344
  _globals['_CREATENOTIFICATIONSINTEGRATIONRESPONSE']._serialized_end=467
  _globals['_UPDATENOTIFICATIONSINTEGRATIONREQUEST']._serialized_start=470
  _globals['_UPDATENOTIFICATIONSINTEGRATIONREQUEST']._serialized_end=616
  _globals['_UPDATENOTIFICATIONSINTEGRATIONRESPONSE']._serialized_start=618
  _globals['_UPDATENOTIFICATIONSINTEGRATIONRESPONSE']._serialized_end=658
  _globals['_DELETENOTIFICATIONSINTEGRATIONREQUEST']._serialized_start=660
  _globals['_DELETENOTIFICATIONSINTEGRATIONREQUEST']._serialized_end=723
  _globals['_DELETENOTIFICATIONSINTEGRATIONRESPONSE']._serialized_start=725
  _globals['_DELETENOTIFICATIONSINTEGRATIONRESPONSE']._serialized_end=765
  _globals['_NOTIFICATIONSINTEGRATIONSSERVICE']._serialized_start=768
  _globals['_NOTIFICATIONSINTEGRATIONSSERVICE']._serialized_end=1546
# @@protoc_insertion_point(module_scope)
