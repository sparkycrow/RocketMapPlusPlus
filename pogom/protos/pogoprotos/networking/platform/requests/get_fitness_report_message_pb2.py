# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/platform/requests/get_fitness_report_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/platform/requests/get_fitness_report_message.proto',
  package='pogoprotos.networking.platform.requests',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nHpogoprotos/networking/platform/requests/get_fitness_report_message.proto\x12\'pogoprotos.networking.platform.requests\"D\n\x17GetFitnessReportMessage\x12\x13\n\x0bnum_of_days\x18\x01 \x01(\x05\x12\x14\n\x0cnum_of_weeks\x18\x02 \x01(\x05\x62\x06proto3')
)




_GETFITNESSREPORTMESSAGE = _descriptor.Descriptor(
  name='GetFitnessReportMessage',
  full_name='pogoprotos.networking.platform.requests.GetFitnessReportMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_of_days', full_name='pogoprotos.networking.platform.requests.GetFitnessReportMessage.num_of_days', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_of_weeks', full_name='pogoprotos.networking.platform.requests.GetFitnessReportMessage.num_of_weeks', index=1,
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
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=117,
  serialized_end=185,
)

DESCRIPTOR.message_types_by_name['GetFitnessReportMessage'] = _GETFITNESSREPORTMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetFitnessReportMessage = _reflection.GeneratedProtocolMessageType('GetFitnessReportMessage', (_message.Message,), dict(
  DESCRIPTOR = _GETFITNESSREPORTMESSAGE,
  __module__ = 'pogoprotos.networking.platform.requests.get_fitness_report_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.platform.requests.GetFitnessReportMessage)
  ))
_sym_db.RegisterMessage(GetFitnessReportMessage)


# @@protoc_insertion_point(module_scope)
