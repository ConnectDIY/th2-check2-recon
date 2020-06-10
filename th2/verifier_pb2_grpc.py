# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from th2 import verifier_pb2 as th2_dot_verifier__pb2


class VerifierStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.createCheckpoint = channel.unary_unary(
                '/th2.Verifier/createCheckpoint',
                request_serializer=th2_dot_verifier__pb2.CheckpointRequest.SerializeToString,
                response_deserializer=th2_dot_verifier__pb2.CheckpointResponse.FromString,
                )
        self.submitCheckRule = channel.unary_unary(
                '/th2.Verifier/submitCheckRule',
                request_serializer=th2_dot_verifier__pb2.CheckRuleRequest.SerializeToString,
                response_deserializer=th2_dot_verifier__pb2.CheckRuleResponse.FromString,
                )
        self.submitCheckSequenceRule = channel.unary_unary(
                '/th2.Verifier/submitCheckSequenceRule',
                request_serializer=th2_dot_verifier__pb2.CheckSequenceRuleRequest.SerializeToString,
                response_deserializer=th2_dot_verifier__pb2.CheckSequenceRuleResponse.FromString,
                )


class VerifierServicer(object):
    """Missing associated documentation comment in .proto file"""

    def createCheckpoint(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def submitCheckRule(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def submitCheckSequenceRule(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_VerifierServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'createCheckpoint': grpc.unary_unary_rpc_method_handler(
                    servicer.createCheckpoint,
                    request_deserializer=th2_dot_verifier__pb2.CheckpointRequest.FromString,
                    response_serializer=th2_dot_verifier__pb2.CheckpointResponse.SerializeToString,
            ),
            'submitCheckRule': grpc.unary_unary_rpc_method_handler(
                    servicer.submitCheckRule,
                    request_deserializer=th2_dot_verifier__pb2.CheckRuleRequest.FromString,
                    response_serializer=th2_dot_verifier__pb2.CheckRuleResponse.SerializeToString,
            ),
            'submitCheckSequenceRule': grpc.unary_unary_rpc_method_handler(
                    servicer.submitCheckSequenceRule,
                    request_deserializer=th2_dot_verifier__pb2.CheckSequenceRuleRequest.FromString,
                    response_serializer=th2_dot_verifier__pb2.CheckSequenceRuleResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'th2.Verifier', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Verifier(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def createCheckpoint(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/th2.Verifier/createCheckpoint',
            th2_dot_verifier__pb2.CheckpointRequest.SerializeToString,
            th2_dot_verifier__pb2.CheckpointResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def submitCheckRule(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/th2.Verifier/submitCheckRule',
            th2_dot_verifier__pb2.CheckRuleRequest.SerializeToString,
            th2_dot_verifier__pb2.CheckRuleResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def submitCheckSequenceRule(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/th2.Verifier/submitCheckSequenceRule',
            th2_dot_verifier__pb2.CheckSequenceRuleRequest.SerializeToString,
            th2_dot_verifier__pb2.CheckSequenceRuleResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
