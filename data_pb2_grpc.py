# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import data_pb2 as data__pb2


class DataHashStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.greeting = channel.unary_unary(
                '/DataHash/greeting',
                request_serializer=data__pb2.Text.SerializeToString,
                response_deserializer=data__pb2.Text.FromString,
                )


class DataHashServicer(object):
    """Missing associated documentation comment in .proto file."""

    def greeting(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DataHashServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'greeting': grpc.unary_unary_rpc_method_handler(
                    servicer.greeting,
                    request_deserializer=data__pb2.Text.FromString,
                    response_serializer=data__pb2.Text.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'DataHash', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DataHash(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def greeting(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DataHash/greeting',
            data__pb2.Text.SerializeToString,
            data__pb2.Text.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)