# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/telemetry/platform_server_data.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/telemetry/platform_server_data.proto',
  package='pogoprotos.data.telemetry',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n4pogoprotos/data/telemetry/platform_server_data.proto\x12\x19pogoprotos.data.telemetry\"\x9e\x01\n\x12PlatformServerData\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x14\n\x0ctelemetry_id\x18\x02 \x01(\t\x12\x12\n\nsession_id\x18\x03 \x01(\t\x12\x16\n\x0e\x65xperiment_ids\x18\x04 \x03(\x05\x12\x18\n\x10\x65vent_request_id\x18\x05 \x01(\t\x12\x1b\n\x13server_timestamp_ms\x18\x06 \x01(\x03\x62\x06proto3')
)




_PLATFORMSERVERDATA = _descriptor.Descriptor(
  name='PlatformServerData',
  full_name='pogoprotos.data.telemetry.PlatformServerData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='pogoprotos.data.telemetry.PlatformServerData.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='telemetry_id', full_name='pogoprotos.data.telemetry.PlatformServerData.telemetry_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='session_id', full_name='pogoprotos.data.telemetry.PlatformServerData.session_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='experiment_ids', full_name='pogoprotos.data.telemetry.PlatformServerData.experiment_ids', index=3,
      number=4, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event_request_id', full_name='pogoprotos.data.telemetry.PlatformServerData.event_request_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='server_timestamp_ms', full_name='pogoprotos.data.telemetry.PlatformServerData.server_timestamp_ms', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=84,
  serialized_end=242,
)

DESCRIPTOR.message_types_by_name['PlatformServerData'] = _PLATFORMSERVERDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PlatformServerData = _reflection.GeneratedProtocolMessageType('PlatformServerData', (_message.Message,), dict(
  DESCRIPTOR = _PLATFORMSERVERDATA,
  __module__ = 'pogoprotos.data.telemetry.platform_server_data_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.PlatformServerData)
  ))
_sym_db.RegisterMessage(PlatformServerData)


# @@protoc_insertion_point(module_scope)
