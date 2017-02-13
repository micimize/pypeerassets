# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: 0001-peerassets-transaction-specification.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='0001-peerassets-transaction-specification.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n/0001-peerassets-transaction-specification.proto\"\xb7\x01\n\tDeckSpawn\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x1a\n\x12number_of_decimals\x18\x03 \x01(\r\x12\x12\n\nissue_mode\x18\x04 \x01(\r\x12\x1b\n\x13\x61sset_specific_data\x18\x05 \x01(\x0c\">\n\x04MODE\x12\x08\n\x04NONE\x10\x00\x12\n\n\x06\x43USTOM\x10\x01\x12\x08\n\x04ONCE\x10\x02\x12\t\n\x05MULTI\x10\x04\x12\x0b\n\x07SINGLET\x10\x08\"i\n\x0c\x43\x61rdTransfer\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\x0f\n\x07\x61mounts\x18\x02 \x03(\x04\x12\x1a\n\x12number_of_decimals\x18\x03 \x01(\r\x12\x1b\n\x13\x61sset_specific_data\x18\x04 \x01(\x0c\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_DECKSPAWN_MODE = _descriptor.EnumDescriptor(
  name='MODE',
  full_name='DeckSpawn.MODE',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUSTOM', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ONCE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MULTI', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SINGLET', index=4, number=8,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=173,
  serialized_end=235,
)
_sym_db.RegisterEnumDescriptor(_DECKSPAWN_MODE)


_DECKSPAWN = _descriptor.Descriptor(
  name='DeckSpawn',
  full_name='DeckSpawn',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='DeckSpawn.version', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='DeckSpawn.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='number_of_decimals', full_name='DeckSpawn.number_of_decimals', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='issue_mode', full_name='DeckSpawn.issue_mode', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='asset_specific_data', full_name='DeckSpawn.asset_specific_data', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DECKSPAWN_MODE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=52,
  serialized_end=235,
)


_CARDTRANSFER = _descriptor.Descriptor(
  name='CardTransfer',
  full_name='CardTransfer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='CardTransfer.version', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='amounts', full_name='CardTransfer.amounts', index=1,
      number=2, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='number_of_decimals', full_name='CardTransfer.number_of_decimals', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='asset_specific_data', full_name='CardTransfer.asset_specific_data', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=237,
  serialized_end=342,
)

_DECKSPAWN_MODE.containing_type = _DECKSPAWN
DESCRIPTOR.message_types_by_name['DeckSpawn'] = _DECKSPAWN
DESCRIPTOR.message_types_by_name['CardTransfer'] = _CARDTRANSFER

DeckSpawn = _reflection.GeneratedProtocolMessageType('DeckSpawn', (_message.Message,), dict(
  DESCRIPTOR = _DECKSPAWN,
  __module__ = '0001_peerassets_transaction_specification_pb2'
  # @@protoc_insertion_point(class_scope:DeckSpawn)
  ))
_sym_db.RegisterMessage(DeckSpawn)

CardTransfer = _reflection.GeneratedProtocolMessageType('CardTransfer', (_message.Message,), dict(
  DESCRIPTOR = _CARDTRANSFER,
  __module__ = '0001_peerassets_transaction_specification_pb2'
  # @@protoc_insertion_point(class_scope:CardTransfer)
  ))
_sym_db.RegisterMessage(CardTransfer)


# @@protoc_insertion_point(module_scope)
