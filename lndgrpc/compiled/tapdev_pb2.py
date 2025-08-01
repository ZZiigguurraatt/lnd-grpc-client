# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lndgrpc/compiled/tapdev.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from lndgrpc.compiled import taprootassets_pb2 as lndgrpc_dot_compiled_dot_taprootassets__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dlndgrpc/compiled/tapdev.proto\x12\ttapdevrpc\x1a$lndgrpc/compiled/taprootassets.proto\"?\n\x12ImportProofRequest\x12\x12\n\nproof_file\x18\x01 \x01(\x0c\x12\x15\n\rgenesis_point\x18\x02 \x01(\t\"\x15\n\x13ImportProofResponse\"%\n#SubscribeSendAssetEventNtfnsRequest\"\xb6\x01\n\x0eSendAssetEvent\x12\x44\n\x18\x65xecute_send_state_event\x18\x01 \x01(\x0b\x32 .tapdevrpc.ExecuteSendStateEventH\x00\x12U\n!proof_transfer_backoff_wait_event\x18\x02 \x01(\x0b\x32(.tapdevrpc.ProofTransferBackoffWaitEventH\x00\x42\x07\n\x05\x65vent\">\n\x15\x45xecuteSendStateEvent\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12\x12\n\nsend_state\x18\x02 \x01(\t\"\x8f\x01\n\x1dProofTransferBackoffWaitEvent\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12\x0f\n\x07\x62\x61\x63koff\x18\x02 \x01(\x03\x12\x15\n\rtries_counter\x18\x03 \x01(\x03\x12\x33\n\rtransfer_type\x18\x04 \x01(\x0e\x32\x1c.tapdevrpc.ProofTransferType\"(\n&SubscribeReceiveAssetEventNtfnsRequest\"_\n\x19\x41ssetReceiveCompleteEvent\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12\x1d\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x0c.taprpc.Addr\x12\x10\n\x08outpoint\x18\x03 \x01(\t\"\xc1\x01\n\x11ReceiveAssetEvent\x12U\n!proof_transfer_backoff_wait_event\x18\x01 \x01(\x0b\x32(.tapdevrpc.ProofTransferBackoffWaitEventH\x00\x12L\n\x1c\x61sset_receive_complete_event\x18\x02 \x01(\x0b\x32$.tapdevrpc.AssetReceiveCompleteEventH\x00\x42\x07\n\x05\x65vent*R\n\x11ProofTransferType\x12\x1c\n\x18PROOF_TRANSFER_TYPE_SEND\x10\x00\x12\x1f\n\x1bPROOF_TRANSFER_TYPE_RECEIVE\x10\x01\x32\xbe\x02\n\x06TapDev\x12Q\n\x0bImportProof\x12\x1d.tapdevrpc.ImportProofRequest\x1a\x1e.tapdevrpc.ImportProofResponse\"\x03\x88\x02\x01\x12k\n\x1cSubscribeSendAssetEventNtfns\x12..tapdevrpc.SubscribeSendAssetEventNtfnsRequest\x1a\x19.tapdevrpc.SendAssetEvent0\x01\x12t\n\x1fSubscribeReceiveAssetEventNtfns\x12\x31.tapdevrpc.SubscribeReceiveAssetEventNtfnsRequest\x1a\x1c.tapdevrpc.ReceiveAssetEvent0\x01\x42:Z8github.com/lightninglabs/taproot-assets/taprpc/tapdevrpcb\x06proto3')

_PROOFTRANSFERTYPE = DESCRIPTOR.enum_types_by_name['ProofTransferType']
ProofTransferType = enum_type_wrapper.EnumTypeWrapper(_PROOFTRANSFERTYPE)
PROOF_TRANSFER_TYPE_SEND = 0
PROOF_TRANSFER_TYPE_RECEIVE = 1


_IMPORTPROOFREQUEST = DESCRIPTOR.message_types_by_name['ImportProofRequest']
_IMPORTPROOFRESPONSE = DESCRIPTOR.message_types_by_name['ImportProofResponse']
_SUBSCRIBESENDASSETEVENTNTFNSREQUEST = DESCRIPTOR.message_types_by_name['SubscribeSendAssetEventNtfnsRequest']
_SENDASSETEVENT = DESCRIPTOR.message_types_by_name['SendAssetEvent']
_EXECUTESENDSTATEEVENT = DESCRIPTOR.message_types_by_name['ExecuteSendStateEvent']
_PROOFTRANSFERBACKOFFWAITEVENT = DESCRIPTOR.message_types_by_name['ProofTransferBackoffWaitEvent']
_SUBSCRIBERECEIVEASSETEVENTNTFNSREQUEST = DESCRIPTOR.message_types_by_name['SubscribeReceiveAssetEventNtfnsRequest']
_ASSETRECEIVECOMPLETEEVENT = DESCRIPTOR.message_types_by_name['AssetReceiveCompleteEvent']
_RECEIVEASSETEVENT = DESCRIPTOR.message_types_by_name['ReceiveAssetEvent']
ImportProofRequest = _reflection.GeneratedProtocolMessageType('ImportProofRequest', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTPROOFREQUEST,
  '__module__' : 'lndgrpc.compiled.tapdev_pb2'
  # @@protoc_insertion_point(class_scope:tapdevrpc.ImportProofRequest)
  })
_sym_db.RegisterMessage(ImportProofRequest)

ImportProofResponse = _reflection.GeneratedProtocolMessageType('ImportProofResponse', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTPROOFRESPONSE,
  '__module__' : 'lndgrpc.compiled.tapdev_pb2'
  # @@protoc_insertion_point(class_scope:tapdevrpc.ImportProofResponse)
  })
_sym_db.RegisterMessage(ImportProofResponse)

SubscribeSendAssetEventNtfnsRequest = _reflection.GeneratedProtocolMessageType('SubscribeSendAssetEventNtfnsRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBESENDASSETEVENTNTFNSREQUEST,
  '__module__' : 'lndgrpc.compiled.tapdev_pb2'
  # @@protoc_insertion_point(class_scope:tapdevrpc.SubscribeSendAssetEventNtfnsRequest)
  })
_sym_db.RegisterMessage(SubscribeSendAssetEventNtfnsRequest)

SendAssetEvent = _reflection.GeneratedProtocolMessageType('SendAssetEvent', (_message.Message,), {
  'DESCRIPTOR' : _SENDASSETEVENT,
  '__module__' : 'lndgrpc.compiled.tapdev_pb2'
  # @@protoc_insertion_point(class_scope:tapdevrpc.SendAssetEvent)
  })
_sym_db.RegisterMessage(SendAssetEvent)

ExecuteSendStateEvent = _reflection.GeneratedProtocolMessageType('ExecuteSendStateEvent', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTESENDSTATEEVENT,
  '__module__' : 'lndgrpc.compiled.tapdev_pb2'
  # @@protoc_insertion_point(class_scope:tapdevrpc.ExecuteSendStateEvent)
  })
_sym_db.RegisterMessage(ExecuteSendStateEvent)

ProofTransferBackoffWaitEvent = _reflection.GeneratedProtocolMessageType('ProofTransferBackoffWaitEvent', (_message.Message,), {
  'DESCRIPTOR' : _PROOFTRANSFERBACKOFFWAITEVENT,
  '__module__' : 'lndgrpc.compiled.tapdev_pb2'
  # @@protoc_insertion_point(class_scope:tapdevrpc.ProofTransferBackoffWaitEvent)
  })
_sym_db.RegisterMessage(ProofTransferBackoffWaitEvent)

SubscribeReceiveAssetEventNtfnsRequest = _reflection.GeneratedProtocolMessageType('SubscribeReceiveAssetEventNtfnsRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBERECEIVEASSETEVENTNTFNSREQUEST,
  '__module__' : 'lndgrpc.compiled.tapdev_pb2'
  # @@protoc_insertion_point(class_scope:tapdevrpc.SubscribeReceiveAssetEventNtfnsRequest)
  })
_sym_db.RegisterMessage(SubscribeReceiveAssetEventNtfnsRequest)

AssetReceiveCompleteEvent = _reflection.GeneratedProtocolMessageType('AssetReceiveCompleteEvent', (_message.Message,), {
  'DESCRIPTOR' : _ASSETRECEIVECOMPLETEEVENT,
  '__module__' : 'lndgrpc.compiled.tapdev_pb2'
  # @@protoc_insertion_point(class_scope:tapdevrpc.AssetReceiveCompleteEvent)
  })
_sym_db.RegisterMessage(AssetReceiveCompleteEvent)

ReceiveAssetEvent = _reflection.GeneratedProtocolMessageType('ReceiveAssetEvent', (_message.Message,), {
  'DESCRIPTOR' : _RECEIVEASSETEVENT,
  '__module__' : 'lndgrpc.compiled.tapdev_pb2'
  # @@protoc_insertion_point(class_scope:tapdevrpc.ReceiveAssetEvent)
  })
_sym_db.RegisterMessage(ReceiveAssetEvent)

_TAPDEV = DESCRIPTOR.services_by_name['TapDev']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z8github.com/lightninglabs/taproot-assets/taprpc/tapdevrpc'
  _TAPDEV.methods_by_name['ImportProof']._options = None
  _TAPDEV.methods_by_name['ImportProof']._serialized_options = b'\210\002\001'
  _PROOFTRANSFERTYPE._serialized_start=939
  _PROOFTRANSFERTYPE._serialized_end=1021
  _IMPORTPROOFREQUEST._serialized_start=82
  _IMPORTPROOFREQUEST._serialized_end=145
  _IMPORTPROOFRESPONSE._serialized_start=147
  _IMPORTPROOFRESPONSE._serialized_end=168
  _SUBSCRIBESENDASSETEVENTNTFNSREQUEST._serialized_start=170
  _SUBSCRIBESENDASSETEVENTNTFNSREQUEST._serialized_end=207
  _SENDASSETEVENT._serialized_start=210
  _SENDASSETEVENT._serialized_end=392
  _EXECUTESENDSTATEEVENT._serialized_start=394
  _EXECUTESENDSTATEEVENT._serialized_end=456
  _PROOFTRANSFERBACKOFFWAITEVENT._serialized_start=459
  _PROOFTRANSFERBACKOFFWAITEVENT._serialized_end=602
  _SUBSCRIBERECEIVEASSETEVENTNTFNSREQUEST._serialized_start=604
  _SUBSCRIBERECEIVEASSETEVENTNTFNSREQUEST._serialized_end=644
  _ASSETRECEIVECOMPLETEEVENT._serialized_start=646
  _ASSETRECEIVECOMPLETEEVENT._serialized_end=741
  _RECEIVEASSETEVENT._serialized_start=744
  _RECEIVEASSETEVENT._serialized_end=937
  _TAPDEV._serialized_start=1024
  _TAPDEV._serialized_end=1342
# @@protoc_insertion_point(module_scope)
