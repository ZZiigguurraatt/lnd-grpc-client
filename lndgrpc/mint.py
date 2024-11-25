from .compiled import mint_pb2 as mint                # note: API docs call this mintrpc
from .compiled import mint_pb2_grpc as mintrpc        # note: API docs call this mintstub
from .common import BaseClient
from .errors import handle_rpc_errors




class MintRPC(BaseClient):

    def get_mint_stub(self):
        # only create a new stub if it does not already exist, otherwise re-use the existing one
        if not hasattr(self, '_mint_stub'):
            self._mint_stub = mintrpc.MintStub(self.channel)
        return self._mint_stub

    @handle_rpc_errors
    def mint_asset(self, short_response=False, **kwargs):
        asset=mint.MintAsset(**kwargs)
        request = mint.MintAssetRequest(asset=asset,short_response=short_response)
        response = self.get_mint_stub().MintAsset(request)
        return response





    def finalize_batch(self, short_response=False, **kwargs):
        request = mint.FinalizeBatchRequest(short_response=short_response, **kwargs)
        response = self.get_mint_stub().FinalizeBatch(request)
        return response


