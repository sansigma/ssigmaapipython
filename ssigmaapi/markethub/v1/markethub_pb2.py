# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ssigmaapi/markethub/v1/markethub.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ssigmaapi.type import market_pb2 as ssigmaapi_dot_type_dot_market__pb2
from ssigmaapi.type import trade_pb2 as ssigmaapi_dot_type_dot_trade__pb2
from ssigmaapi.type import orderbook_pb2 as ssigmaapi_dot_type_dot_orderbook__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ssigmaapi/markethub/v1/markethub.proto',
  package='ssigmaapi.markethub.v1',
  syntax='proto3',
  serialized_options=_b('Z4github.com/kaito2/ssigmaapigo/markethub/v1;markethub'),
  serialized_pb=_b('\n&ssigmaapi/markethub/v1/markethub.proto\x12\x16ssigmaapi.markethub.v1\x1a\x1bssigmaapi/type/market.proto\x1a\x1assigmaapi/type/trade.proto\x1a\x1essigmaapi/type/orderbook.proto\x1a\x1cgoogle/api/annotations.proto\"\x9e\x01\n\x10GetTradesRequest\x12\'\n\x07markets\x18\x01 \x03(\x0b\x32\x16.ssigmaapi.type.Market\x12\x1f\n\x17velocity_windowing_size\x18\x02 \x01(\x03\x12!\n\x19volatility_windowing_size\x18\x03 \x01(\x03\x12\x1d\n\x15volume_windowing_size\x18\x04 \x01(\x03\"\x9a\x01\n\x11GetTradesResponse\x12\x44\n\x12trades_with_market\x18\x01 \x03(\x0b\x32(.ssigmaapi.markethub.v1.TradesWithMarket\x12?\n\x0f\x65xchange_status\x18\x02 \x03(\x0b\x32&.ssigmaapi.markethub.v1.ExchangeStatus\">\n\x14GetOrderBooksRequest\x12&\n\x06market\x18\x01 \x03(\x0b\x32\x16.ssigmaapi.type.Market\"\x93\x01\n\x15GetOrderBooksResponse\x12&\n\x03\x61ll\x18\x01 \x03(\x0b\x32\x19.ssigmaapi.type.OrderBook\x12\x11\n\ttimestamp\x18\x02 \x01(\x03\x12?\n\x0f\x65xchange_status\x18\x03 \x03(\x0b\x32&.ssigmaapi.markethub.v1.ExchangeStatus\"\xa3\x01\n\x1dGetTradesAndOrderBooksRequest\x12<\n\ntrades_req\x18\x01 \x01(\x0b\x32(.ssigmaapi.markethub.v1.GetTradesRequest\x12\x44\n\x0eorderbooks_req\x18\x02 \x01(\x0b\x32,.ssigmaapi.markethub.v1.GetOrderBooksRequest\"\xe7\x01\n\x1eGetTradesAndOrderBooksResponse\x12=\n\ntrades_res\x18\x01 \x01(\x0b\x32).ssigmaapi.markethub.v1.GetTradesResponse\x12\x45\n\x0eorderbooks_res\x18\x02 \x01(\x0b\x32-.ssigmaapi.markethub.v1.GetOrderBooksResponse\x12?\n\x0f\x65xchange_status\x18\x03 \x03(\x0b\x32&.ssigmaapi.markethub.v1.ExchangeStatus\"\xa0\x02\n\x17TradeWithAdditionalInfo\x12$\n\x05trade\x18\x01 \x01(\x0b\x32\x15.ssigmaapi.type.Trade\x12\x10\n\x08velocity\x18\x02 \x01(\x01\x12\x14\n\x0c\x61\x63\x63\x65leration\x18\x03 \x01(\x01\x12\x12\n\nvolatility\x18\x04 \x01(\x01\x12\x13\n\x0bvolume_base\x18\x05 \x01(\x01\x12\x14\n\x0cvolume_quote\x18\x06 \x01(\x01\x12\x15\n\rmomentum_rate\x18\x07 \x01(\x01\x12\x1f\n\x17velocity_windowing_size\x18\x08 \x01(\x03\x12!\n\x19volatility_windowing_size\x18\t \x01(\x03\x12\x1d\n\x15volume_windowing_size\x18\n \x01(\x03\"{\n\x10TradesWithMarket\x12&\n\x06market\x18\x01 \x01(\x0b\x32\x16.ssigmaapi.type.Market\x12?\n\x06trades\x18\x02 \x03(\x0b\x32/.ssigmaapi.markethub.v1.TradeWithAdditionalInfo\"0\n\x0e\x45xchangeStatus\x12\x10\n\x08\x65xchange\x18\x01 \x01(\t\x12\x0c\n\x04open\x18\x02 \x01(\x08\x32\xcb\x04\n\x12MarketHubServiceV1\x12\xd6\x01\n\tGetTrades\x12(.ssigmaapi.markethub.v1.GetTradesRequest\x1a).ssigmaapi.markethub.v1.GetTradesResponse\"r\x82\xd3\xe4\x93\x02l\"g/v1/market-hub/get-trades/{velocity_windowing_size}/{volatility_windowing_size}/{volume_windowing_size}:\x01*0\x01\x12\x99\x01\n\rGetOrderBooks\x12,.ssigmaapi.markethub.v1.GetOrderBooksRequest\x1a-.ssigmaapi.markethub.v1.GetOrderBooksResponse\")\x82\xd3\xe4\x93\x02#\"\x1e/v1/market-hub/get-order-books:\x01*0\x01\x12\xbf\x01\n\x16GetTradesAndOrderBooks\x12\x35.ssigmaapi.markethub.v1.GetTradesAndOrderBooksRequest\x1a\x36.ssigmaapi.markethub.v1.GetTradesAndOrderBooksResponse\"4\x82\xd3\xe4\x93\x02.\")/v1/market-hub/get-trades-and-order-books:\x01*0\x01\x42\x36Z4github.com/kaito2/ssigmaapigo/markethub/v1;markethubb\x06proto3')
  ,
  dependencies=[ssigmaapi_dot_type_dot_market__pb2.DESCRIPTOR,ssigmaapi_dot_type_dot_trade__pb2.DESCRIPTOR,ssigmaapi_dot_type_dot_orderbook__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_GETTRADESREQUEST = _descriptor.Descriptor(
  name='GetTradesRequest',
  full_name='ssigmaapi.markethub.v1.GetTradesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='markets', full_name='ssigmaapi.markethub.v1.GetTradesRequest.markets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='velocity_windowing_size', full_name='ssigmaapi.markethub.v1.GetTradesRequest.velocity_windowing_size', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='volatility_windowing_size', full_name='ssigmaapi.markethub.v1.GetTradesRequest.volatility_windowing_size', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='volume_windowing_size', full_name='ssigmaapi.markethub.v1.GetTradesRequest.volume_windowing_size', index=3,
      number=4, type=3, cpp_type=2, label=1,
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
  serialized_start=186,
  serialized_end=344,
)


_GETTRADESRESPONSE = _descriptor.Descriptor(
  name='GetTradesResponse',
  full_name='ssigmaapi.markethub.v1.GetTradesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trades_with_market', full_name='ssigmaapi.markethub.v1.GetTradesResponse.trades_with_market', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exchange_status', full_name='ssigmaapi.markethub.v1.GetTradesResponse.exchange_status', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=347,
  serialized_end=501,
)


_GETORDERBOOKSREQUEST = _descriptor.Descriptor(
  name='GetOrderBooksRequest',
  full_name='ssigmaapi.markethub.v1.GetOrderBooksRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='market', full_name='ssigmaapi.markethub.v1.GetOrderBooksRequest.market', index=0,
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
  serialized_start=503,
  serialized_end=565,
)


_GETORDERBOOKSRESPONSE = _descriptor.Descriptor(
  name='GetOrderBooksResponse',
  full_name='ssigmaapi.markethub.v1.GetOrderBooksResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='all', full_name='ssigmaapi.markethub.v1.GetOrderBooksResponse.all', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='ssigmaapi.markethub.v1.GetOrderBooksResponse.timestamp', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exchange_status', full_name='ssigmaapi.markethub.v1.GetOrderBooksResponse.exchange_status', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=568,
  serialized_end=715,
)


_GETTRADESANDORDERBOOKSREQUEST = _descriptor.Descriptor(
  name='GetTradesAndOrderBooksRequest',
  full_name='ssigmaapi.markethub.v1.GetTradesAndOrderBooksRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trades_req', full_name='ssigmaapi.markethub.v1.GetTradesAndOrderBooksRequest.trades_req', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orderbooks_req', full_name='ssigmaapi.markethub.v1.GetTradesAndOrderBooksRequest.orderbooks_req', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=718,
  serialized_end=881,
)


_GETTRADESANDORDERBOOKSRESPONSE = _descriptor.Descriptor(
  name='GetTradesAndOrderBooksResponse',
  full_name='ssigmaapi.markethub.v1.GetTradesAndOrderBooksResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trades_res', full_name='ssigmaapi.markethub.v1.GetTradesAndOrderBooksResponse.trades_res', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orderbooks_res', full_name='ssigmaapi.markethub.v1.GetTradesAndOrderBooksResponse.orderbooks_res', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exchange_status', full_name='ssigmaapi.markethub.v1.GetTradesAndOrderBooksResponse.exchange_status', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=884,
  serialized_end=1115,
)


_TRADEWITHADDITIONALINFO = _descriptor.Descriptor(
  name='TradeWithAdditionalInfo',
  full_name='ssigmaapi.markethub.v1.TradeWithAdditionalInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trade', full_name='ssigmaapi.markethub.v1.TradeWithAdditionalInfo.trade', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='velocity', full_name='ssigmaapi.markethub.v1.TradeWithAdditionalInfo.velocity', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acceleration', full_name='ssigmaapi.markethub.v1.TradeWithAdditionalInfo.acceleration', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='volatility', full_name='ssigmaapi.markethub.v1.TradeWithAdditionalInfo.volatility', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='volume_base', full_name='ssigmaapi.markethub.v1.TradeWithAdditionalInfo.volume_base', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='volume_quote', full_name='ssigmaapi.markethub.v1.TradeWithAdditionalInfo.volume_quote', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='momentum_rate', full_name='ssigmaapi.markethub.v1.TradeWithAdditionalInfo.momentum_rate', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='velocity_windowing_size', full_name='ssigmaapi.markethub.v1.TradeWithAdditionalInfo.velocity_windowing_size', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='volatility_windowing_size', full_name='ssigmaapi.markethub.v1.TradeWithAdditionalInfo.volatility_windowing_size', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='volume_windowing_size', full_name='ssigmaapi.markethub.v1.TradeWithAdditionalInfo.volume_windowing_size', index=9,
      number=10, type=3, cpp_type=2, label=1,
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
  serialized_start=1118,
  serialized_end=1406,
)


_TRADESWITHMARKET = _descriptor.Descriptor(
  name='TradesWithMarket',
  full_name='ssigmaapi.markethub.v1.TradesWithMarket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='market', full_name='ssigmaapi.markethub.v1.TradesWithMarket.market', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trades', full_name='ssigmaapi.markethub.v1.TradesWithMarket.trades', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=1408,
  serialized_end=1531,
)


_EXCHANGESTATUS = _descriptor.Descriptor(
  name='ExchangeStatus',
  full_name='ssigmaapi.markethub.v1.ExchangeStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='exchange', full_name='ssigmaapi.markethub.v1.ExchangeStatus.exchange', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='open', full_name='ssigmaapi.markethub.v1.ExchangeStatus.open', index=1,
      number=2, type=8, cpp_type=7, label=1,
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
  serialized_start=1533,
  serialized_end=1581,
)

_GETTRADESREQUEST.fields_by_name['markets'].message_type = ssigmaapi_dot_type_dot_market__pb2._MARKET
_GETTRADESRESPONSE.fields_by_name['trades_with_market'].message_type = _TRADESWITHMARKET
_GETTRADESRESPONSE.fields_by_name['exchange_status'].message_type = _EXCHANGESTATUS
_GETORDERBOOKSREQUEST.fields_by_name['market'].message_type = ssigmaapi_dot_type_dot_market__pb2._MARKET
_GETORDERBOOKSRESPONSE.fields_by_name['all'].message_type = ssigmaapi_dot_type_dot_orderbook__pb2._ORDERBOOK
_GETORDERBOOKSRESPONSE.fields_by_name['exchange_status'].message_type = _EXCHANGESTATUS
_GETTRADESANDORDERBOOKSREQUEST.fields_by_name['trades_req'].message_type = _GETTRADESREQUEST
_GETTRADESANDORDERBOOKSREQUEST.fields_by_name['orderbooks_req'].message_type = _GETORDERBOOKSREQUEST
_GETTRADESANDORDERBOOKSRESPONSE.fields_by_name['trades_res'].message_type = _GETTRADESRESPONSE
_GETTRADESANDORDERBOOKSRESPONSE.fields_by_name['orderbooks_res'].message_type = _GETORDERBOOKSRESPONSE
_GETTRADESANDORDERBOOKSRESPONSE.fields_by_name['exchange_status'].message_type = _EXCHANGESTATUS
_TRADEWITHADDITIONALINFO.fields_by_name['trade'].message_type = ssigmaapi_dot_type_dot_trade__pb2._TRADE
_TRADESWITHMARKET.fields_by_name['market'].message_type = ssigmaapi_dot_type_dot_market__pb2._MARKET
_TRADESWITHMARKET.fields_by_name['trades'].message_type = _TRADEWITHADDITIONALINFO
DESCRIPTOR.message_types_by_name['GetTradesRequest'] = _GETTRADESREQUEST
DESCRIPTOR.message_types_by_name['GetTradesResponse'] = _GETTRADESRESPONSE
DESCRIPTOR.message_types_by_name['GetOrderBooksRequest'] = _GETORDERBOOKSREQUEST
DESCRIPTOR.message_types_by_name['GetOrderBooksResponse'] = _GETORDERBOOKSRESPONSE
DESCRIPTOR.message_types_by_name['GetTradesAndOrderBooksRequest'] = _GETTRADESANDORDERBOOKSREQUEST
DESCRIPTOR.message_types_by_name['GetTradesAndOrderBooksResponse'] = _GETTRADESANDORDERBOOKSRESPONSE
DESCRIPTOR.message_types_by_name['TradeWithAdditionalInfo'] = _TRADEWITHADDITIONALINFO
DESCRIPTOR.message_types_by_name['TradesWithMarket'] = _TRADESWITHMARKET
DESCRIPTOR.message_types_by_name['ExchangeStatus'] = _EXCHANGESTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetTradesRequest = _reflection.GeneratedProtocolMessageType('GetTradesRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETTRADESREQUEST,
  __module__ = 'ssigmaapi.markethub.v1.markethub_pb2'
  # @@protoc_insertion_point(class_scope:ssigmaapi.markethub.v1.GetTradesRequest)
  ))
_sym_db.RegisterMessage(GetTradesRequest)

GetTradesResponse = _reflection.GeneratedProtocolMessageType('GetTradesResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETTRADESRESPONSE,
  __module__ = 'ssigmaapi.markethub.v1.markethub_pb2'
  # @@protoc_insertion_point(class_scope:ssigmaapi.markethub.v1.GetTradesResponse)
  ))
_sym_db.RegisterMessage(GetTradesResponse)

GetOrderBooksRequest = _reflection.GeneratedProtocolMessageType('GetOrderBooksRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETORDERBOOKSREQUEST,
  __module__ = 'ssigmaapi.markethub.v1.markethub_pb2'
  # @@protoc_insertion_point(class_scope:ssigmaapi.markethub.v1.GetOrderBooksRequest)
  ))
_sym_db.RegisterMessage(GetOrderBooksRequest)

GetOrderBooksResponse = _reflection.GeneratedProtocolMessageType('GetOrderBooksResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETORDERBOOKSRESPONSE,
  __module__ = 'ssigmaapi.markethub.v1.markethub_pb2'
  # @@protoc_insertion_point(class_scope:ssigmaapi.markethub.v1.GetOrderBooksResponse)
  ))
_sym_db.RegisterMessage(GetOrderBooksResponse)

GetTradesAndOrderBooksRequest = _reflection.GeneratedProtocolMessageType('GetTradesAndOrderBooksRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETTRADESANDORDERBOOKSREQUEST,
  __module__ = 'ssigmaapi.markethub.v1.markethub_pb2'
  # @@protoc_insertion_point(class_scope:ssigmaapi.markethub.v1.GetTradesAndOrderBooksRequest)
  ))
_sym_db.RegisterMessage(GetTradesAndOrderBooksRequest)

GetTradesAndOrderBooksResponse = _reflection.GeneratedProtocolMessageType('GetTradesAndOrderBooksResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETTRADESANDORDERBOOKSRESPONSE,
  __module__ = 'ssigmaapi.markethub.v1.markethub_pb2'
  # @@protoc_insertion_point(class_scope:ssigmaapi.markethub.v1.GetTradesAndOrderBooksResponse)
  ))
_sym_db.RegisterMessage(GetTradesAndOrderBooksResponse)

TradeWithAdditionalInfo = _reflection.GeneratedProtocolMessageType('TradeWithAdditionalInfo', (_message.Message,), dict(
  DESCRIPTOR = _TRADEWITHADDITIONALINFO,
  __module__ = 'ssigmaapi.markethub.v1.markethub_pb2'
  # @@protoc_insertion_point(class_scope:ssigmaapi.markethub.v1.TradeWithAdditionalInfo)
  ))
_sym_db.RegisterMessage(TradeWithAdditionalInfo)

TradesWithMarket = _reflection.GeneratedProtocolMessageType('TradesWithMarket', (_message.Message,), dict(
  DESCRIPTOR = _TRADESWITHMARKET,
  __module__ = 'ssigmaapi.markethub.v1.markethub_pb2'
  # @@protoc_insertion_point(class_scope:ssigmaapi.markethub.v1.TradesWithMarket)
  ))
_sym_db.RegisterMessage(TradesWithMarket)

ExchangeStatus = _reflection.GeneratedProtocolMessageType('ExchangeStatus', (_message.Message,), dict(
  DESCRIPTOR = _EXCHANGESTATUS,
  __module__ = 'ssigmaapi.markethub.v1.markethub_pb2'
  # @@protoc_insertion_point(class_scope:ssigmaapi.markethub.v1.ExchangeStatus)
  ))
_sym_db.RegisterMessage(ExchangeStatus)


DESCRIPTOR._options = None

_MARKETHUBSERVICEV1 = _descriptor.ServiceDescriptor(
  name='MarketHubServiceV1',
  full_name='ssigmaapi.markethub.v1.MarketHubServiceV1',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1584,
  serialized_end=2171,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetTrades',
    full_name='ssigmaapi.markethub.v1.MarketHubServiceV1.GetTrades',
    index=0,
    containing_service=None,
    input_type=_GETTRADESREQUEST,
    output_type=_GETTRADESRESPONSE,
    serialized_options=_b('\202\323\344\223\002l\"g/v1/market-hub/get-trades/{velocity_windowing_size}/{volatility_windowing_size}/{volume_windowing_size}:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='GetOrderBooks',
    full_name='ssigmaapi.markethub.v1.MarketHubServiceV1.GetOrderBooks',
    index=1,
    containing_service=None,
    input_type=_GETORDERBOOKSREQUEST,
    output_type=_GETORDERBOOKSRESPONSE,
    serialized_options=_b('\202\323\344\223\002#\"\036/v1/market-hub/get-order-books:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='GetTradesAndOrderBooks',
    full_name='ssigmaapi.markethub.v1.MarketHubServiceV1.GetTradesAndOrderBooks',
    index=2,
    containing_service=None,
    input_type=_GETTRADESANDORDERBOOKSREQUEST,
    output_type=_GETTRADESANDORDERBOOKSRESPONSE,
    serialized_options=_b('\202\323\344\223\002.\")/v1/market-hub/get-trades-and-order-books:\001*'),
  ),
])
_sym_db.RegisterServiceDescriptor(_MARKETHUBSERVICEV1)

DESCRIPTOR.services_by_name['MarketHubServiceV1'] = _MARKETHUBSERVICEV1

# @@protoc_insertion_point(module_scope)