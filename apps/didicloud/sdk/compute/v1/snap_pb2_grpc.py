# coding: utf-8 
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from didicloud.sdk.compute.v1 import snap_pb2 as compute_dot_v1_dot_snap__pb2


class SnapStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ListSnapshot = channel.unary_unary(
        '/didi.cloud.compute.v1.Snap/ListSnapshot',
        request_serializer=compute_dot_v1_dot_snap__pb2.ListSnapshotRequest.SerializeToString,
        response_deserializer=compute_dot_v1_dot_snap__pb2.ListSnapshotResponse.FromString,
        )
    self.GetSnapshotTotalCnt = channel.unary_unary(
        '/didi.cloud.compute.v1.Snap/GetSnapshotTotalCnt',
        request_serializer=compute_dot_v1_dot_snap__pb2.GetSnapshotTotalCntRequest.SerializeToString,
        response_deserializer=compute_dot_v1_dot_snap__pb2.GetSnapshotTotalCntResponse.FromString,
        )
    self.CreateSnapshot = channel.unary_unary(
        '/didi.cloud.compute.v1.Snap/CreateSnapshot',
        request_serializer=compute_dot_v1_dot_snap__pb2.CreateSnapshotRequest.SerializeToString,
        response_deserializer=compute_dot_v1_dot_snap__pb2.CreateSnapshotResponse.FromString,
        )
    self.DeleteSnapshot = channel.unary_unary(
        '/didi.cloud.compute.v1.Snap/DeleteSnapshot',
        request_serializer=compute_dot_v1_dot_snap__pb2.DeleteSnapshotRequest.SerializeToString,
        response_deserializer=compute_dot_v1_dot_snap__pb2.DeleteSnapshotResponse.FromString,
        )
    self.RevertSnapshot = channel.unary_unary(
        '/didi.cloud.compute.v1.Snap/RevertSnapshot',
        request_serializer=compute_dot_v1_dot_snap__pb2.RevertSnapshotRequest.SerializeToString,
        response_deserializer=compute_dot_v1_dot_snap__pb2.RevertSnapshotResponse.FromString,
        )
    self.ChangeSnapshotName = channel.unary_unary(
        '/didi.cloud.compute.v1.Snap/ChangeSnapshotName',
        request_serializer=compute_dot_v1_dot_snap__pb2.ChangeSnapshotNameRequest.SerializeToString,
        response_deserializer=compute_dot_v1_dot_snap__pb2.ChangeSnapshotNameResponse.FromString,
        )


class SnapServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def ListSnapshot(self, request, context):
    """获取snap列表
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetSnapshotTotalCnt(self, request, context):
    """获取snap数量
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateSnapshot(self, request, context):
    """创建snap
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteSnapshot(self, request, context):
    """删除snap
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RevertSnapshot(self, request, context):
    """还原snap
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ChangeSnapshotName(self, request, context):
    """改名snap
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SnapServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ListSnapshot': grpc.unary_unary_rpc_method_handler(
          servicer.ListSnapshot,
          request_deserializer=compute_dot_v1_dot_snap__pb2.ListSnapshotRequest.FromString,
          response_serializer=compute_dot_v1_dot_snap__pb2.ListSnapshotResponse.SerializeToString,
      ),
      'GetSnapshotTotalCnt': grpc.unary_unary_rpc_method_handler(
          servicer.GetSnapshotTotalCnt,
          request_deserializer=compute_dot_v1_dot_snap__pb2.GetSnapshotTotalCntRequest.FromString,
          response_serializer=compute_dot_v1_dot_snap__pb2.GetSnapshotTotalCntResponse.SerializeToString,
      ),
      'CreateSnapshot': grpc.unary_unary_rpc_method_handler(
          servicer.CreateSnapshot,
          request_deserializer=compute_dot_v1_dot_snap__pb2.CreateSnapshotRequest.FromString,
          response_serializer=compute_dot_v1_dot_snap__pb2.CreateSnapshotResponse.SerializeToString,
      ),
      'DeleteSnapshot': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteSnapshot,
          request_deserializer=compute_dot_v1_dot_snap__pb2.DeleteSnapshotRequest.FromString,
          response_serializer=compute_dot_v1_dot_snap__pb2.DeleteSnapshotResponse.SerializeToString,
      ),
      'RevertSnapshot': grpc.unary_unary_rpc_method_handler(
          servicer.RevertSnapshot,
          request_deserializer=compute_dot_v1_dot_snap__pb2.RevertSnapshotRequest.FromString,
          response_serializer=compute_dot_v1_dot_snap__pb2.RevertSnapshotResponse.SerializeToString,
      ),
      'ChangeSnapshotName': grpc.unary_unary_rpc_method_handler(
          servicer.ChangeSnapshotName,
          request_deserializer=compute_dot_v1_dot_snap__pb2.ChangeSnapshotNameRequest.FromString,
          response_serializer=compute_dot_v1_dot_snap__pb2.ChangeSnapshotNameResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'didi.cloud.compute.v1.Snap', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
