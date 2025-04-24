import grpc
from functools import wraps


HideErrors=False

def printMessage(str):
    if not HideErrors:
        print(str)


class WalletEncryptedError(Exception):

    def __init__(self, message=None):
        message = message or 'Wallet is encrypted. Please unlock or set ' \
                             'password if this is the first time starting lnd. '
        super().__init__(message)


def handle_rpc_errors(fnc):
    """Decorator to add more context to RPC errors"""

    @wraps(fnc)
    def wrapper(*args, **kwargs):
        try:
            return fnc(*args, **kwargs)
        except grpc.RpcError as exc:
            # lnd might be active, but not possible to contact
            # using RPC if the wallet is encrypted. If we get
            # an rpc error code Unimplemented, it means that lnd is
            # running, but the RPC server is not active yet (only
            # WalletUnlocker server active) and most likely this
            # is because of an encrypted wallet.
            exc.code().value
            exc.details()
            if exc.code() == grpc.StatusCode.UNIMPLEMENTED:
                # raise WalletEncryptedError from None
                printMessage("unimplemented")
                raise exc
            elif exc.code() == grpc.StatusCode.UNAVAILABLE:
                printMessage("UNAVAILABLE")
                printMessage(f"ERROR MESSAGE: {exc.details()}")
                raise exc
            elif exc.code() == grpc.StatusCode.UNKNOWN and exc.details() == "wallet locked, unlock it to enable full RPC access":
                printMessage("WALLET IS LOCKED!")
                raise exc
            elif exc.code() == grpc.StatusCode.UNKNOWN:
                printMessage("unknown")
                printMessage(f"ERROR MESSAGE: {exc.details()}")
                raise exc
            elif exc.code() == grpc.StatusCode.NOT_FOUND:
                printMessage("NOT FOUND")
                printMessage(f"ERROR MESSAGE: {exc.details()}")
                raise exc
            elif exc.code() == grpc.StatusCode.PERMISSION_DENIED:
                printMessage("PERMISSION_DENIED")
                printMessage(f"ERROR MESSAGE: {exc.details()}")
                raise exc
            else:
                raise exc
                return exc
        except Exception as exc:
            printMessage("unknown exception")
            printMessage(exc)
            raise exc

    return wrapper
