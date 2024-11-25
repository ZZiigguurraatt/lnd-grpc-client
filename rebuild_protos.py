from pathlib import Path
import shutil
import sh
import sys
import re
import os

lnd_dir = Path(os.getenv("APP_DIR"))
tapd_dir = Path(os.getenv("TAPP_DIR"))
grpc_client_dir = Path(os.getenv("CLIENT_DIR"))

os.chdir(grpc_client_dir)

if not all([lnd_dir.exists(),tapd_dir.exists(), grpc_client_dir.exists()]):
    print("Error: Double check that the paths exist!")
    sys.exit(1)

for proto in list(lnd_dir.rglob("**/*.proto")):
    print(proto)
    shutil.copy(proto, grpc_client_dir.joinpath("lndgrpc/compiled/"))
    print(f"Copied: {proto.name}")

for proto in list(tapd_dir.rglob("**/*.proto")):
    print(proto)
    shutil.copy(proto, grpc_client_dir.joinpath("lndgrpc/compiled/"))
    print(f"Copied: {proto.name}")






# Modify paths so python imports work right in generated files.
for proto in list(grpc_client_dir.joinpath("lndgrpc/compiled/").rglob("*.proto")):
    with open(proto, 'r+') as f:
        text = f.read()
        text = re.sub('lightning.proto', 'lndgrpc/compiled/lightning.proto', text)
        text = re.sub('verrpc/verrpc.proto', 'lndgrpc/compiled/verrpc.proto', text)
        text = re.sub('signrpc/signer.proto', 'lndgrpc/compiled/signer.proto', text)


        # also needed for taproot assets
        text = re.sub('routerrpc/router.proto', 'lndgrpc/compiled/router.proto', text)
        text = re.sub('rfqrpc/rfq.proto', 'lndgrpc/compiled/rfq.proto', text)
        text = re.sub('taprootassets.proto', 'lndgrpc/compiled/taprootassets.proto', text)

        f.seek(0)
        f.write(text)
        f.truncate()

protos = list(Path(".").joinpath("lndgrpc/compiled/").glob("*.proto"))

args = [
    "-m",
    "grpc_tools.protoc",
    "--proto_path=.",
    "--python_out=.",
    "--grpc_python_out=.",
]

for protofile in protos:
    args.append(str(protofile) )

# Generate the compiled protofiles
sh.python3(args)