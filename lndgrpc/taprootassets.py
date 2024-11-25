from .compiled import taprootassets_pb2 as taprootassets                # note: API docs call this taprpc
from .compiled import taprootassets_pb2_grpc as taprootassetsrpc        # note: API docs call this taprootassetsstub
from .common import BaseClient
from .errors import handle_rpc_errors




class TaprootAssetsRPC(BaseClient):

    def get_taprootassets_stub(self):
        # only create a new stub if it does not already exist, otherwise re-use the existing one
        if not hasattr(self, '_taprootassets_stub'):
            self._taprootassets_stub = taprootassetsrpc.TaprootAssetsStub(self.channel)
        return self._taprootassets_stub

    @handle_rpc_errors
    def list_assets(self, **kwargs):
        request = taprootassets.ListAssetRequest(**kwargs)
        response = self.get_taprootassets_stub().ListAssets(request)
        return response




