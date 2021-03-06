# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ssigmaapi/type/orderbook.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ssigmaapi/type/orderbook.proto',
  package='ssigmaapi.type',
  syntax='proto3',
  serialized_options=_b('Z8github.com/sansigma/ssigmaapigo/type/orderbook;orderbook'),
  serialized_pb=_b('\n\x1essigmaapi/type/orderbook.proto\x12\x0essigmaapi.type\"\'\n\x06\x42idAsk\x12\r\n\x05price\x18\x01 \x01(\x01\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x01\"\xa9\x01\n\tOrderBook\x12\x10\n\x08\x65xchange\x18\x01 \x01(\t\x12\x0c\n\x04\x62\x61se\x18\x02 \x01(\t\x12\r\n\x05quote\x18\x03 \x01(\t\x12\x0e\n\x06symbol\x18\x04 \x01(\t\x12$\n\x04\x62ids\x18\x05 \x03(\x0b\x32\x16.ssigmaapi.type.BidAsk\x12$\n\x04\x61sks\x18\x06 \x03(\x0b\x32\x16.ssigmaapi.type.BidAsk\x12\x11\n\ttimestamp\x18\x07 \x01(\x03\x42:Z8github.com/sansigma/ssigmaapigo/type/orderbook;orderbookb\x06proto3')
)




_BIDASK = _descriptor.Descriptor(
  name='BidAsk',
  full_name='ssigmaapi.type.BidAsk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='price', full_name='ssigmaapi.type.BidAsk.price', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='ssigmaapi.type.BidAsk.amount', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=50,
  serialized_end=89,
)


_ORDERBOOK = _descriptor.Descriptor(
  name='OrderBook',
  full_name='ssigmaapi.type.OrderBook',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='exchange', full_name='ssigmaapi.type.OrderBook.exchange', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='base', full_name='ssigmaapi.type.OrderBook.base', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quote', full_name='ssigmaapi.type.OrderBook.quote', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='symbol', full_name='ssigmaapi.type.OrderBook.symbol', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bids', full_name='ssigmaapi.type.OrderBook.bids', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='asks', full_name='ssigmaapi.type.OrderBook.asks', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='ssigmaapi.type.OrderBook.timestamp', index=6,
      number=7, type=3, cpp_type=2, label=1,
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
  serialized_start=92,
  serialized_end=261,
)

_ORDERBOOK.fields_by_name['bids'].message_type = _BIDASK
_ORDERBOOK.fields_by_name['asks'].message_type = _BIDASK
DESCRIPTOR.message_types_by_name['BidAsk'] = _BIDASK
DESCRIPTOR.message_types_by_name['OrderBook'] = _ORDERBOOK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BidAsk = _reflection.GeneratedProtocolMessageType('BidAsk', (_message.Message,), dict(
  DESCRIPTOR = _BIDASK,
  __module__ = 'ssigmaapi.type.orderbook_pb2'
  # @@protoc_insertion_point(class_scope:ssigmaapi.type.BidAsk)
  ))
_sym_db.RegisterMessage(BidAsk)

OrderBook = _reflection.GeneratedProtocolMessageType('OrderBook', (_message.Message,), dict(
  DESCRIPTOR = _ORDERBOOK,
  __module__ = 'ssigmaapi.type.orderbook_pb2'
  # @@protoc_insertion_point(class_scope:ssigmaapi.type.OrderBook)
  ))
_sym_db.RegisterMessage(OrderBook)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
