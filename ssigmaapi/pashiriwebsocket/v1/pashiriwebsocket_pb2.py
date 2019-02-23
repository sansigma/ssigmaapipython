# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ssigmaapi/pashiriwebsocket/v1/pashiriwebsocket.proto

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


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ssigmaapi/pashiriwebsocket/v1/pashiriwebsocket.proto',
  package='ssigmaapi.pashiriwebsocket.v1',
  syntax='proto3',
  serialized_options=_b('ZBgithub.com/kaito2/ssigmaapigo/pashiriwebsocket/v1;pashiriwebsocket'),
  serialized_pb=_b('\n4ssigmaapi/pashiriwebsocket/v1/pashiriwebsocket.proto\x12\x1dssigmaapi.pashiriwebsocket.v1\x1a\x1bssigmaapi/type/market.proto\x1a\x1assigmaapi/type/trade.proto2\\\n\x19PashiriWebsocketServiceV1\x12?\n\tGetTrades\x12\x16.ssigmaapi.type.Market\x1a\x16.ssigmaapi.type.Trades\"\x00\x30\x01\x42\x44ZBgithub.com/kaito2/ssigmaapigo/pashiriwebsocket/v1;pashiriwebsocketb\x06proto3')
  ,
  dependencies=[ssigmaapi_dot_type_dot_market__pb2.DESCRIPTOR,ssigmaapi_dot_type_dot_trade__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_PASHIRIWEBSOCKETSERVICEV1 = _descriptor.ServiceDescriptor(
  name='PashiriWebsocketServiceV1',
  full_name='ssigmaapi.pashiriwebsocket.v1.PashiriWebsocketServiceV1',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=144,
  serialized_end=236,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetTrades',
    full_name='ssigmaapi.pashiriwebsocket.v1.PashiriWebsocketServiceV1.GetTrades',
    index=0,
    containing_service=None,
    input_type=ssigmaapi_dot_type_dot_market__pb2._MARKET,
    output_type=ssigmaapi_dot_type_dot_trade__pb2._TRADES,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PASHIRIWEBSOCKETSERVICEV1)

DESCRIPTOR.services_by_name['PashiriWebsocketServiceV1'] = _PASHIRIWEBSOCKETSERVICEV1

# @@protoc_insertion_point(module_scope)
