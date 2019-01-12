# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/sfida_capture_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/sfida_capture_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n<pogoprotos/networking/responses/sfida_capture_response.proto\x12\x1fpogoprotos.networking.responses\"\xa7\x02\n\x14SfidaCaptureResponse\x12L\n\x06result\x18\x01 \x01(\x0e\x32<.pogoprotos.networking.responses.SfidaCaptureResponse.Result\x12\x0f\n\x07xp_gain\x18\x02 \x01(\x05\"\xaf\x01\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x14\n\x10POKEMON_CAPTURED\x10\x01\x12\x10\n\x0cPOKEMON_FLED\x10\x02\x12\r\n\tNOT_FOUND\x10\x03\x12\x15\n\x11NO_MORE_POKEBALLS\x10\x04\x12\x1a\n\x16POKEMON_INVENTORY_FULL\x10\x05\x12\x10\n\x0cNOT_IN_RANGE\x10\x06\x12\x1e\n\x1a\x45NCOUNTER_ALREADY_FINISHED\x10\x07\x62\x06proto3')
)



_SFIDACAPTURERESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.SfidaCaptureResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_CAPTURED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_FLED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_FOUND', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_MORE_POKEBALLS', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_INVENTORY_FULL', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_IN_RANGE', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENCOUNTER_ALREADY_FINISHED', index=7, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=218,
  serialized_end=393,
)
_sym_db.RegisterEnumDescriptor(_SFIDACAPTURERESPONSE_RESULT)


_SFIDACAPTURERESPONSE = _descriptor.Descriptor(
  name='SfidaCaptureResponse',
  full_name='pogoprotos.networking.responses.SfidaCaptureResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.SfidaCaptureResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='xp_gain', full_name='pogoprotos.networking.responses.SfidaCaptureResponse.xp_gain', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SFIDACAPTURERESPONSE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=98,
  serialized_end=393,
)

_SFIDACAPTURERESPONSE.fields_by_name['result'].enum_type = _SFIDACAPTURERESPONSE_RESULT
_SFIDACAPTURERESPONSE_RESULT.containing_type = _SFIDACAPTURERESPONSE
DESCRIPTOR.message_types_by_name['SfidaCaptureResponse'] = _SFIDACAPTURERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SfidaCaptureResponse = _reflection.GeneratedProtocolMessageType('SfidaCaptureResponse', (_message.Message,), dict(
  DESCRIPTOR = _SFIDACAPTURERESPONSE,
  __module__ = 'pogoprotos.networking.responses.sfida_capture_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.SfidaCaptureResponse)
  ))
_sym_db.RegisterMessage(SfidaCaptureResponse)


# @@protoc_insertion_point(module_scope)
