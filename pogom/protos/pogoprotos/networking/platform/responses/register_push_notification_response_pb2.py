# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/platform/responses/register_push_notification_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/platform/responses/register_push_notification_response.proto',
  package='pogoprotos.networking.platform.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nRpogoprotos/networking/platform/responses/register_push_notification_response.proto\x12(pogoprotos.networking.platform.responses\"\xb6\x01\n RegisterPushNotificationResponse\x12\x61\n\x06result\x18\x01 \x01(\x0e\x32Q.pogoprotos.networking.platform.responses.RegisterPushNotificationResponse.Result\"/\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\r\n\tNO_CHANGE\x10\x02\x62\x06proto3')
)



_REGISTERPUSHNOTIFICATIONRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.platform.responses.RegisterPushNotificationResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_CHANGE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=264,
  serialized_end=311,
)
_sym_db.RegisterEnumDescriptor(_REGISTERPUSHNOTIFICATIONRESPONSE_RESULT)


_REGISTERPUSHNOTIFICATIONRESPONSE = _descriptor.Descriptor(
  name='RegisterPushNotificationResponse',
  full_name='pogoprotos.networking.platform.responses.RegisterPushNotificationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.platform.responses.RegisterPushNotificationResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REGISTERPUSHNOTIFICATIONRESPONSE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=129,
  serialized_end=311,
)

_REGISTERPUSHNOTIFICATIONRESPONSE.fields_by_name['result'].enum_type = _REGISTERPUSHNOTIFICATIONRESPONSE_RESULT
_REGISTERPUSHNOTIFICATIONRESPONSE_RESULT.containing_type = _REGISTERPUSHNOTIFICATIONRESPONSE
DESCRIPTOR.message_types_by_name['RegisterPushNotificationResponse'] = _REGISTERPUSHNOTIFICATIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RegisterPushNotificationResponse = _reflection.GeneratedProtocolMessageType('RegisterPushNotificationResponse', (_message.Message,), dict(
  DESCRIPTOR = _REGISTERPUSHNOTIFICATIONRESPONSE,
  __module__ = 'pogoprotos.networking.platform.responses.register_push_notification_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.platform.responses.RegisterPushNotificationResponse)
  ))
_sym_db.RegisterMessage(RegisterPushNotificationResponse)


# @@protoc_insertion_point(module_scope)
