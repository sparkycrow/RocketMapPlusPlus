# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/ditto/downstream_action_event_params.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/ditto/downstream_action_event_params.proto',
  package='pogoprotos.data.ditto',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n:pogoprotos/data/ditto/downstream_action_event_params.proto\x12\x15pogoprotos.data.ditto\"M\n\x1b\x44ownstreamActionEventParams\x12\x0f\n\x07methods\x18\x01 \x03(\r\x12\x10\n\x08payloads\x18\x02 \x03(\x0c\x12\x0b\n\x03ids\x18\x03 \x03(\x04\x62\x06proto3')
)




_DOWNSTREAMACTIONEVENTPARAMS = _descriptor.Descriptor(
  name='DownstreamActionEventParams',
  full_name='pogoprotos.data.ditto.DownstreamActionEventParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='methods', full_name='pogoprotos.data.ditto.DownstreamActionEventParams.methods', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payloads', full_name='pogoprotos.data.ditto.DownstreamActionEventParams.payloads', index=1,
      number=2, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ids', full_name='pogoprotos.data.ditto.DownstreamActionEventParams.ids', index=2,
      number=3, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=85,
  serialized_end=162,
)

DESCRIPTOR.message_types_by_name['DownstreamActionEventParams'] = _DOWNSTREAMACTIONEVENTPARAMS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DownstreamActionEventParams = _reflection.GeneratedProtocolMessageType('DownstreamActionEventParams', (_message.Message,), dict(
  DESCRIPTOR = _DOWNSTREAMACTIONEVENTPARAMS,
  __module__ = 'pogoprotos.data.ditto.downstream_action_event_params_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.ditto.DownstreamActionEventParams)
  ))
_sym_db.RegisterMessage(DownstreamActionEventParams)


# @@protoc_insertion_point(module_scope)
