# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ssigmaapi/type/trade.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ssigmaapi/type/trade.proto',
  package='ssigmaapi.type',
  syntax='proto3',
  serialized_options=_b('Z0github.com/sansigma/ssigmaapigo/type/trade;trade'),
  serialized_pb=_b('\n\x1assigmaapi/type/trade.proto\x12\x0essigmaapi.type\"/\n\x06Trades\x12%\n\x06trades\x18\x01 \x03(\x0b\x32\x15.ssigmaapi.type.Trade\"\x98\x01\n\x05Trade\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x10\n\x08trade_id\x18\x02 \x01(\t\x12\x10\n\x08\x65xchange\x18\x03 \x01(\t\x12\x0c\n\x04\x62\x61se\x18\x04 \x01(\t\x12\r\n\x05quote\x18\x05 \x01(\t\x12\r\n\x05price\x18\x06 \x01(\x01\x12\x0e\n\x06\x61mount\x18\x07 \x01(\x01\x12\x11\n\ttimestamp\x18\x08 \x01(\x03\x12\x0c\n\x04side\x18\t \x01(\tB2Z0github.com/sansigma/ssigmaapigo/type/trade;tradeb\x06proto3')
)




_TRADES = _descriptor.Descriptor(
  name='Trades',
  full_name='ssigmaapi.type.Trades',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trades', full_name='ssigmaapi.type.Trades.trades', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=46,
  serialized_end=93,
)


_TRADE = _descriptor.Descriptor(
  name='Trade',
  full_name='ssigmaapi.type.Trade',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='symbol', full_name='ssigmaapi.type.Trade.symbol', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trade_id', full_name='ssigmaapi.type.Trade.trade_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exchange', full_name='ssigmaapi.type.Trade.exchange', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='base', full_name='ssigmaapi.type.Trade.base', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quote', full_name='ssigmaapi.type.Trade.quote', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price', full_name='ssigmaapi.type.Trade.price', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='ssigmaapi.type.Trade.amount', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='ssigmaapi.type.Trade.timestamp', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='side', full_name='ssigmaapi.type.Trade.side', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=96,
  serialized_end=248,
)

_TRADES.fields_by_name['trades'].message_type = _TRADE
DESCRIPTOR.message_types_by_name['Trades'] = _TRADES
DESCRIPTOR.message_types_by_name['Trade'] = _TRADE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Trades = _reflection.GeneratedProtocolMessageType('Trades', (_message.Message,), dict(
  DESCRIPTOR = _TRADES,
  __module__ = 'ssigmaapi.type.trade_pb2'
  # @@protoc_insertion_point(class_scope:ssigmaapi.type.Trades)
  ))
_sym_db.RegisterMessage(Trades)

Trade = _reflection.GeneratedProtocolMessageType('Trade', (_message.Message,), dict(
  DESCRIPTOR = _TRADE,
  __module__ = 'ssigmaapi.type.trade_pb2'
  # @@protoc_insertion_point(class_scope:ssigmaapi.type.Trade)
  ))
_sym_db.RegisterMessage(Trade)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
