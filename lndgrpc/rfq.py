from .compiled import rfq_pb2 as rfq                # note: API docs call this rfqrpc
from .compiled import rfq_pb2_grpc as rfqrpc        # note: API docs call this rfqstub
from .common import BaseClient
from .errors import handle_rpc_errors




class RfqRPC(BaseClient):

    def get_rfq_stub(self):
        # only create a new stub if it does not already exist, otherwise re-use the existing one
        if not hasattr(self, '_rfq_stub'):
            self._rfq_stub = rfqrpc.RfqStub(self.channel)
        return self._rfq_stub

    @handle_rpc_errors
    def add_asset_sell_order(self, **kwargs):
        request = rfq.AddAssetSellOrderRequest(**kwargs)
        response = self.get_rfq_stub().AddAssetSellOrder(request)
        return response

