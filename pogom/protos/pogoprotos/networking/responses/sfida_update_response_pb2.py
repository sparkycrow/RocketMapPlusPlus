# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/sfida_update_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import encounter_type_pb2 as pogoprotos_dot_enums_dot_encounter__type__pb2
from pogoprotos.data.sfida import sfida_nearby_pokemon_pb2 as pogoprotos_dot_data_dot_sfida_dot_sfida__nearby__pokemon__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/sfida_update_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n;pogoprotos/networking/responses/sfida_update_response.proto\x12\x1fpogoprotos.networking.responses\x1a%pogoprotos/enums/encounter_type.proto\x1a\x30pogoprotos/data/sfida/sfida_nearby_pokemon.proto\"\xb8\x03\n\x13SfidaUpdateResponse\x12K\n\x06status\x18\x01 \x01(\x0e\x32;.pogoprotos.networking.responses.SfidaUpdateResponse.Status\x12\x16\n\x0enearby_pokemon\x18\x02 \x01(\x08\x12\x18\n\x10uncaught_pokemon\x18\x03 \x01(\x08\x12\x19\n\x11legendary_pokemon\x18\x04 \x01(\x08\x12\x15\n\rspawnpoint_id\x18\x05 \x01(\t\x12\x14\n\x0c\x65ncounter_id\x18\x06 \x01(\x03\x12\x17\n\x0fnearby_pokestop\x18\x07 \x01(\x08\x12\x13\n\x0bpokestop_id\x18\x08 \x01(\t\x12\x37\n\x0e\x65ncounter_type\x18\t \x01(\x0e\x32\x1f.pogoprotos.enums.EncounterType\x12\x16\n\x0epokedex_number\x18\n \x01(\x05\x12\x39\n\x06nearby\x18\x0b \x03(\x0b\x32).pogoprotos.data.sfida.SfidaNearbyPokemon\" \n\x06Status\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_encounter__type__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_sfida_dot_sfida__nearby__pokemon__pb2.DESCRIPTOR,])



_SFIDAUPDATERESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='pogoprotos.networking.responses.SfidaUpdateResponse.Status',
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
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=594,
  serialized_end=626,
)
_sym_db.RegisterEnumDescriptor(_SFIDAUPDATERESPONSE_STATUS)


_SFIDAUPDATERESPONSE = _descriptor.Descriptor(
  name='SfidaUpdateResponse',
  full_name='pogoprotos.networking.responses.SfidaUpdateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pogoprotos.networking.responses.SfidaUpdateResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nearby_pokemon', full_name='pogoprotos.networking.responses.SfidaUpdateResponse.nearby_pokemon', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uncaught_pokemon', full_name='pogoprotos.networking.responses.SfidaUpdateResponse.uncaught_pokemon', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='legendary_pokemon', full_name='pogoprotos.networking.responses.SfidaUpdateResponse.legendary_pokemon', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spawnpoint_id', full_name='pogoprotos.networking.responses.SfidaUpdateResponse.spawnpoint_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encounter_id', full_name='pogoprotos.networking.responses.SfidaUpdateResponse.encounter_id', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nearby_pokestop', full_name='pogoprotos.networking.responses.SfidaUpdateResponse.nearby_pokestop', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pokestop_id', full_name='pogoprotos.networking.responses.SfidaUpdateResponse.pokestop_id', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encounter_type', full_name='pogoprotos.networking.responses.SfidaUpdateResponse.encounter_type', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pokedex_number', full_name='pogoprotos.networking.responses.SfidaUpdateResponse.pokedex_number', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nearby', full_name='pogoprotos.networking.responses.SfidaUpdateResponse.nearby', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SFIDAUPDATERESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=186,
  serialized_end=626,
)

_SFIDAUPDATERESPONSE.fields_by_name['status'].enum_type = _SFIDAUPDATERESPONSE_STATUS
_SFIDAUPDATERESPONSE.fields_by_name['encounter_type'].enum_type = pogoprotos_dot_enums_dot_encounter__type__pb2._ENCOUNTERTYPE
_SFIDAUPDATERESPONSE.fields_by_name['nearby'].message_type = pogoprotos_dot_data_dot_sfida_dot_sfida__nearby__pokemon__pb2._SFIDANEARBYPOKEMON
_SFIDAUPDATERESPONSE_STATUS.containing_type = _SFIDAUPDATERESPONSE
DESCRIPTOR.message_types_by_name['SfidaUpdateResponse'] = _SFIDAUPDATERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SfidaUpdateResponse = _reflection.GeneratedProtocolMessageType('SfidaUpdateResponse', (_message.Message,), dict(
  DESCRIPTOR = _SFIDAUPDATERESPONSE,
  __module__ = 'pogoprotos.networking.responses.sfida_update_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.SfidaUpdateResponse)
  ))
_sym_db.RegisterMessage(SfidaUpdateResponse)


# @@protoc_insertion_point(module_scope)
