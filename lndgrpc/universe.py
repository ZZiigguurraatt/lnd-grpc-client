from .compiled import universe_pb2 as universe                # note: API docs call this universerpc
from .compiled import universe_pb2_grpc as universerpc        # note: API docs call this universestub
from .common import BaseClient
from .errors import handle_rpc_errors




class UniverseRPC(BaseClient):

    def get_universe_stub(self):
        # only create a new stub if it does not already exist, otherwise re-use the existing one
        if not hasattr(self, '_universe_stub'):
            self._universe_stub = universerpc.UniverseStub(self.channel)
        return self._universe_stub

    @handle_rpc_errors
    def sync_universe(self, short_response=False, **kwargs):
        request = universe.SyncRequest(**kwargs)
        response = self.get_universe_stub().SyncUniverse(request)
        return response



