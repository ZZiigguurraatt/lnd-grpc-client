from .compiled import tapchannel_pb2 as tapchannel                # note: API docs call this tapchannelrpc
from .compiled import tapchannel_pb2_grpc as tapchannelrpc        # note: API docs call this tapchannelstub

from .compiled import lightning_pb2 as lightning                  # note: API docs call this lnrpc
from .compiled import router_pb2 as router                        # note: API docs call this routerrpc


from .common import BaseClient
from .errors import handle_rpc_errors




class TaprootAssetChannelsRPC(BaseClient):

    def get_tapchannel_stub(self):
        # only create a new stub if it does not already exist, otherwise re-use the existing one
        if not hasattr(self, '_tapchannel_stub'):
            self._tapchannel_stub = tapchannelrpc.TaprootAssetChannelsStub(self.channel)
        return self._tapchannel_stub

    @handle_rpc_errors
    def add_taprootasset_invoice(self, asset_id=None,  group_key=None, asset_amount=0, peer_pubkey=None, hodl_invoice=None, **kwargs):
        request = tapchannel.AddInvoiceRequest(asset_id=asset_id, group_key=group_key, asset_amount=asset_amount, peer_pubkey=peer_pubkey, hodl_invoice=hodl_invoice, invoice_request=lightning.Invoice(**kwargs))
        response = self.get_tapchannel_stub().AddInvoice(request)
        return response

    @handle_rpc_errors
    def decode_asset_pay_req(self, **kwargs):
        request = tapchannel.AssetPayReq(**kwargs)
        response = self.get_tapchannel_stub().DecodeAssetPayReq(request)
        return response

    @handle_rpc_errors
    def fund_taprootasset_channel(self, **kwargs):
        request = tapchannel.FundChannelRequest(**kwargs)
        response = self.get_tapchannel_stub().FundChannel(request)
        return response

    @handle_rpc_errors
    def send_taprootasset_payment(self, asset_id=None, group_key=None, asset_amount=0, peer_pubkey=None, **kwargs):
        request = tapchannel.SendPaymentRequest(asset_id=asset_id, group_key=group_key, asset_amount=asset_amount, peer_pubkey=peer_pubkey, payment_request=router.SendPaymentRequest(**kwargs))
        response = self.get_tapchannel_stub().SendPayment(request)
        return response


