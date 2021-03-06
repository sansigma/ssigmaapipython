# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from ssigmaapi.type import market_pb2 as ssigmaapi_dot_type_dot_market__pb2
from ssigmaapi.type import orderbook_pb2 as ssigmaapi_dot_type_dot_orderbook__pb2


class PashiriRestServiceV1Stub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetOrderBook = channel.unary_stream(
        '/ssigmaapi.pashirirest.v1.PashiriRestServiceV1/GetOrderBook',
        request_serializer=ssigmaapi_dot_type_dot_market__pb2.Market.SerializeToString,
        response_deserializer=ssigmaapi_dot_type_dot_orderbook__pb2.OrderBook.FromString,
        )


class PashiriRestServiceV1Servicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetOrderBook(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PashiriRestServiceV1Servicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetOrderBook': grpc.unary_stream_rpc_method_handler(
          servicer.GetOrderBook,
          request_deserializer=ssigmaapi_dot_type_dot_market__pb2.Market.FromString,
          response_serializer=ssigmaapi_dot_type_dot_orderbook__pb2.OrderBook.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ssigmaapi.pashirirest.v1.PashiriRestServiceV1', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
