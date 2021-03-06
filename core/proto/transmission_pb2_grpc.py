# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
try:
    import transmission_pb2 as transmission__pb2
except ImportError:
    from core.proto import transmission_pb2 as transmission__pb2


class TransmissionStub(object):
    """RPC transmission service for all algorithms between clients and master.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.comm = channel.unary_unary(
                '/transmission.Transmission/comm',
                request_serializer=transmission__pb2.ReqResMessage.SerializeToString,
                response_deserializer=transmission__pb2.ReqResMessage.FromString,
                )


class TransmissionServicer(object):
    """RPC transmission service for all algorithms between clients and master.
    """

    def comm(self, request, context):
        """refactored universal rpc service interface, unary
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TransmissionServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'comm': grpc.unary_unary_rpc_method_handler(
                    servicer.comm,
                    request_deserializer=transmission__pb2.ReqResMessage.FromString,
                    response_serializer=transmission__pb2.ReqResMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'transmission.Transmission', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Transmission(object):
    """RPC transmission service for all algorithms between clients and master.
    """

    @staticmethod
    def comm(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/transmission.Transmission/comm',
            transmission__pb2.ReqResMessage.SerializeToString,
            transmission__pb2.ReqResMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
