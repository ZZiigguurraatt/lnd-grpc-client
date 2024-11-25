# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from lndgrpc.compiled import tapdev_pb2 as lndgrpc_dot_compiled_dot_tapdev__pb2


class TapDevStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ImportProof = channel.unary_unary(
                '/tapdevrpc.TapDev/ImportProof',
                request_serializer=lndgrpc_dot_compiled_dot_tapdev__pb2.ImportProofRequest.SerializeToString,
                response_deserializer=lndgrpc_dot_compiled_dot_tapdev__pb2.ImportProofResponse.FromString,
                )
        self.SubscribeSendAssetEventNtfns = channel.unary_stream(
                '/tapdevrpc.TapDev/SubscribeSendAssetEventNtfns',
                request_serializer=lndgrpc_dot_compiled_dot_tapdev__pb2.SubscribeSendAssetEventNtfnsRequest.SerializeToString,
                response_deserializer=lndgrpc_dot_compiled_dot_tapdev__pb2.SendAssetEvent.FromString,
                )
        self.SubscribeReceiveAssetEventNtfns = channel.unary_stream(
                '/tapdevrpc.TapDev/SubscribeReceiveAssetEventNtfns',
                request_serializer=lndgrpc_dot_compiled_dot_tapdev__pb2.SubscribeReceiveAssetEventNtfnsRequest.SerializeToString,
                response_deserializer=lndgrpc_dot_compiled_dot_tapdev__pb2.ReceiveAssetEvent.FromString,
                )


class TapDevServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ImportProof(self, request, context):
        """tapcli: `dev importproof`
        ImportProof attempts to import a proof file into the daemon. If successful,
        a new asset will be inserted on disk, spendable using the specified target
        script key, and internal key.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeSendAssetEventNtfns(self, request, context):
        """
        SubscribeSendAssetEventNtfns registers a subscription to the event
        notification stream which relates to the asset sending process.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeReceiveAssetEventNtfns(self, request, context):
        """
        SubscribeReceiveAssetEventNtfns registers a subscription to the event
        notification stream which relates to the asset receive process.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TapDevServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ImportProof': grpc.unary_unary_rpc_method_handler(
                    servicer.ImportProof,
                    request_deserializer=lndgrpc_dot_compiled_dot_tapdev__pb2.ImportProofRequest.FromString,
                    response_serializer=lndgrpc_dot_compiled_dot_tapdev__pb2.ImportProofResponse.SerializeToString,
            ),
            'SubscribeSendAssetEventNtfns': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeSendAssetEventNtfns,
                    request_deserializer=lndgrpc_dot_compiled_dot_tapdev__pb2.SubscribeSendAssetEventNtfnsRequest.FromString,
                    response_serializer=lndgrpc_dot_compiled_dot_tapdev__pb2.SendAssetEvent.SerializeToString,
            ),
            'SubscribeReceiveAssetEventNtfns': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeReceiveAssetEventNtfns,
                    request_deserializer=lndgrpc_dot_compiled_dot_tapdev__pb2.SubscribeReceiveAssetEventNtfnsRequest.FromString,
                    response_serializer=lndgrpc_dot_compiled_dot_tapdev__pb2.ReceiveAssetEvent.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'tapdevrpc.TapDev', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TapDev(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ImportProof(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tapdevrpc.TapDev/ImportProof',
            lndgrpc_dot_compiled_dot_tapdev__pb2.ImportProofRequest.SerializeToString,
            lndgrpc_dot_compiled_dot_tapdev__pb2.ImportProofResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeSendAssetEventNtfns(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/tapdevrpc.TapDev/SubscribeSendAssetEventNtfns',
            lndgrpc_dot_compiled_dot_tapdev__pb2.SubscribeSendAssetEventNtfnsRequest.SerializeToString,
            lndgrpc_dot_compiled_dot_tapdev__pb2.SendAssetEvent.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeReceiveAssetEventNtfns(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/tapdevrpc.TapDev/SubscribeReceiveAssetEventNtfns',
            lndgrpc_dot_compiled_dot_tapdev__pb2.SubscribeReceiveAssetEventNtfnsRequest.SerializeToString,
            lndgrpc_dot_compiled_dot_tapdev__pb2.ReceiveAssetEvent.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
