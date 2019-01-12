# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/geofence/geofence_metadata.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/geofence/geofence_metadata.proto',
  package='pogoprotos.data.geofence',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n0pogoprotos/data/geofence/geofence_metadata.proto\x12\x18pogoprotos.data.geofence\"\xc1\x01\n\x10GeofenceMetadata\x12\x14\n\x0clatitude_deg\x18\x01 \x01(\x01\x12\x15\n\rlongitude_deg\x18\x02 \x01(\x01\x12\x0e\n\x06radius\x18\x03 \x01(\x01\x12\x12\n\nidentifier\x18\x04 \x01(\t\x12\x15\n\rexpiration_ms\x18\x05 \x01(\x03\x12\x15\n\rdwell_time_ms\x18\x06 \x01(\x03\x12\x18\n\x10\x66ire_on_entrance\x18\x07 \x01(\x08\x12\x14\n\x0c\x66ire_on_exit\x18\x08 \x01(\x08\x62\x06proto3')
)




_GEOFENCEMETADATA = _descriptor.Descriptor(
  name='GeofenceMetadata',
  full_name='pogoprotos.data.geofence.GeofenceMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='latitude_deg', full_name='pogoprotos.data.geofence.GeofenceMetadata.latitude_deg', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longitude_deg', full_name='pogoprotos.data.geofence.GeofenceMetadata.longitude_deg', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='radius', full_name='pogoprotos.data.geofence.GeofenceMetadata.radius', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='identifier', full_name='pogoprotos.data.geofence.GeofenceMetadata.identifier', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expiration_ms', full_name='pogoprotos.data.geofence.GeofenceMetadata.expiration_ms', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dwell_time_ms', full_name='pogoprotos.data.geofence.GeofenceMetadata.dwell_time_ms', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fire_on_entrance', full_name='pogoprotos.data.geofence.GeofenceMetadata.fire_on_entrance', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fire_on_exit', full_name='pogoprotos.data.geofence.GeofenceMetadata.fire_on_exit', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=79,
  serialized_end=272,
)

DESCRIPTOR.message_types_by_name['GeofenceMetadata'] = _GEOFENCEMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GeofenceMetadata = _reflection.GeneratedProtocolMessageType('GeofenceMetadata', (_message.Message,), dict(
  DESCRIPTOR = _GEOFENCEMETADATA,
  __module__ = 'pogoprotos.data.geofence.geofence_metadata_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.geofence.GeofenceMetadata)
  ))
_sym_db.RegisterMessage(GeofenceMetadata)


# @@protoc_insertion_point(module_scope)
