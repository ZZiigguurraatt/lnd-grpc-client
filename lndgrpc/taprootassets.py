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
    def fetch_asset_meta(self, **kwargs):
        request = taprootassets.FetchAssetMetaRequest(**kwargs)
        response = self.get_taprootassets_stub().FetchAssetMeta(request)
        return response

    @handle_rpc_errors
    def list_assets(self, **kwargs):
        request = taprootassets.ListAssetRequest(**kwargs)
        response = self.get_taprootassets_stub().ListAssets(request)
        return response

    @handle_rpc_errors
    def list_groups(self, **kwargs):
        request = taprootassets.ListGroupsRequest(**kwargs)
        response = self.get_taprootassets_stub().ListGroups(request)
        return response

    @handle_rpc_errors
    def list_balances(self, **kwargs):
        request = taprootassets.ListBalancesRequest(**kwargs)
        response = self.get_taprootassets_stub().ListBalances(request)
        return response

    @handle_rpc_errors
    def send_asset(self, **kwargs):
        request = taprootassets.SendAssetRequest(**kwargs)
        response = self.get_taprootassets_stub().SendAsset(request)
        return response

    @handle_rpc_errors
    def new_addr(self, **kwargs):
        request = taprootassets.NewAddrRequest(**kwargs)
        response = self.get_taprootassets_stub().NewAddr(request)
        return response

    @handle_rpc_errors
    def get_tapd_info(self, **kwargs):
        request = taprootassets.GetInfoRequest(**kwargs)
        response = self.get_taprootassets_stub().GetInfo(request)
        return response




