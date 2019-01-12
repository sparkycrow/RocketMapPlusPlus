# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/sfida_dowser_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/sfida_dowser_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n;pogoprotos/networking/responses/sfida_dowser_response.proto\x12\x1fpogoprotos.networking.responses\"\xf1\x01\n\x13SfidaDowserResponse\x12K\n\x06result\x18\x01 \x01(\x0e\x32;.pogoprotos.networking.responses.SfidaDowserResponse.Result\x12\x11\n\tproximity\x18\x02 \x01(\x05\x12\x15\n\rspawnpoint_id\x18\x03 \x01(\t\"c\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\t\n\x05\x46OUND\x10\x01\x12\n\n\x06NEARBY\x10\x02\x12\x10\n\x0cOUT_OF_RANGE\x10\x03\x12\x12\n\x0e\x41LREADY_CAUGHT\x10\x04\x12\x11\n\rNOT_AVAILABLE\x10\x05\x62\x06proto3')
)



_SFIDADOWSERRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.SfidaDowserResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FOUND', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEARBY', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OUT_OF_RANGE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALREADY_CAUGHT', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_AVAILABLE', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=239,
  serialized_end=338,
)
_sym_db.RegisterEnumDescriptor(_SFIDADOWSERRESPONSE_RESULT)


_SFIDADOWSERRESPONSE = _descriptor.Descriptor(
  name='SfidaDowserResponse',
  full_name='pogoprotos.networking.responses.SfidaDowserResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.SfidaDowserResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proximity', full_name='pogoprotos.networking.responses.SfidaDowserResponse.proximity', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spawnpoint_id', full_name='pogoprotos.networking.responses.SfidaDowserResponse.spawnpoint_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SFIDADOWSERRESPONSE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=97,
  serialized_end=338,
)

_SFIDADOWSERRESPONSE.fields_by_name['result'].enum_type = _SFIDADOWSERRESPONSE_RESULT
_SFIDADOWSERRESPONSE_RESULT.containing_type = _SFIDADOWSERRESPONSE
DESCRIPTOR.message_types_by_name['SfidaDowserResponse'] = _SFIDADOWSERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SfidaDowserResponse = _reflection.GeneratedProtocolMessageType('SfidaDowserResponse', (_message.Message,), dict(
  DESCRIPTOR = _SFIDADOWSERRESPONSE,
  __module__ = 'pogoprotos.networking.responses.sfida_dowser_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.SfidaDowserResponse)
  ))
_sym_db.RegisterMessage(SfidaDowserResponse)


# @@protoc_insertion_point(module_scope)
