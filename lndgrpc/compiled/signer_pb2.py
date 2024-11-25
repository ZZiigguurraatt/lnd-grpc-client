# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lndgrpc/compiled/signer.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dlndgrpc/compiled/signer.proto\x12\x07signrpc\"3\n\nKeyLocator\x12\x12\n\nkey_family\x18\x01 \x01(\x05\x12\x11\n\tkey_index\x18\x02 \x01(\x05\"L\n\rKeyDescriptor\x12\x15\n\rraw_key_bytes\x18\x01 \x01(\x0c\x12$\n\x07key_loc\x18\x02 \x01(\x0b\x32\x13.signrpc.KeyLocator\")\n\x05TxOut\x12\r\n\x05value\x18\x01 \x01(\x03\x12\x11\n\tpk_script\x18\x02 \x01(\x0c\"\x81\x02\n\x0eSignDescriptor\x12(\n\x08key_desc\x18\x01 \x01(\x0b\x32\x16.signrpc.KeyDescriptor\x12\x14\n\x0csingle_tweak\x18\x02 \x01(\x0c\x12\x14\n\x0c\x64ouble_tweak\x18\x03 \x01(\x0c\x12\x11\n\ttap_tweak\x18\n \x01(\x0c\x12\x16\n\x0ewitness_script\x18\x04 \x01(\x0c\x12\x1e\n\x06output\x18\x05 \x01(\x0b\x32\x0e.signrpc.TxOut\x12\x0f\n\x07sighash\x18\x07 \x01(\r\x12\x13\n\x0binput_index\x18\x08 \x01(\x05\x12(\n\x0bsign_method\x18\t \x01(\x0e\x32\x13.signrpc.SignMethod\"r\n\x07SignReq\x12\x14\n\x0craw_tx_bytes\x18\x01 \x01(\x0c\x12+\n\nsign_descs\x18\x02 \x03(\x0b\x32\x17.signrpc.SignDescriptor\x12$\n\x0cprev_outputs\x18\x03 \x03(\x0b\x32\x0e.signrpc.TxOut\"\x1c\n\x08SignResp\x12\x10\n\x08raw_sigs\x18\x01 \x03(\x0c\"2\n\x0bInputScript\x12\x0f\n\x07witness\x18\x01 \x03(\x0c\x12\x12\n\nsig_script\x18\x02 \x01(\x0c\">\n\x0fInputScriptResp\x12+\n\rinput_scripts\x18\x01 \x03(\x0b\x32\x14.signrpc.InputScript\"\xae\x01\n\x0eSignMessageReq\x12\x0b\n\x03msg\x18\x01 \x01(\x0c\x12$\n\x07key_loc\x18\x02 \x01(\x0b\x32\x13.signrpc.KeyLocator\x12\x13\n\x0b\x64ouble_hash\x18\x03 \x01(\x08\x12\x13\n\x0b\x63ompact_sig\x18\x04 \x01(\x08\x12\x13\n\x0bschnorr_sig\x18\x05 \x01(\x08\x12\x1d\n\x15schnorr_sig_tap_tweak\x18\x06 \x01(\x0c\x12\x0b\n\x03tag\x18\x07 \x01(\x0c\"$\n\x0fSignMessageResp\x12\x11\n\tsignature\x18\x01 \x01(\x0c\"g\n\x10VerifyMessageReq\x12\x0b\n\x03msg\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c\x12\x0e\n\x06pubkey\x18\x03 \x01(\x0c\x12\x16\n\x0eis_schnorr_sig\x18\x04 \x01(\x08\x12\x0b\n\x03tag\x18\x05 \x01(\x0c\"\"\n\x11VerifyMessageResp\x12\r\n\x05valid\x18\x01 \x01(\x08\"\x80\x01\n\x10SharedKeyRequest\x12\x18\n\x10\x65phemeral_pubkey\x18\x01 \x01(\x0c\x12(\n\x07key_loc\x18\x02 \x01(\x0b\x32\x13.signrpc.KeyLocatorB\x02\x18\x01\x12(\n\x08key_desc\x18\x03 \x01(\x0b\x32\x16.signrpc.KeyDescriptor\"\'\n\x11SharedKeyResponse\x12\x12\n\nshared_key\x18\x01 \x01(\x0c\"-\n\tTweakDesc\x12\r\n\x05tweak\x18\x01 \x01(\x0c\x12\x11\n\tis_x_only\x18\x02 \x01(\x08\"?\n\x10TaprootTweakDesc\x12\x13\n\x0bscript_root\x18\x01 \x01(\x0c\x12\x16\n\x0ekey_spend_only\x18\x02 \x01(\x08\"\xb5\x01\n\x18MuSig2CombineKeysRequest\x12\x1a\n\x12\x61ll_signer_pubkeys\x18\x01 \x03(\x0c\x12\"\n\x06tweaks\x18\x02 \x03(\x0b\x32\x12.signrpc.TweakDesc\x12\x30\n\rtaproot_tweak\x18\x03 \x01(\x0b\x32\x19.signrpc.TaprootTweakDesc\x12\'\n\x07version\x18\x04 \x01(\x0e\x32\x16.signrpc.MuSig2Version\"x\n\x19MuSig2CombineKeysResponse\x12\x14\n\x0c\x63ombined_key\x18\x01 \x01(\x0c\x12\x1c\n\x14taproot_internal_key\x18\x02 \x01(\x0c\x12\'\n\x07version\x18\x04 \x01(\x0e\x32\x16.signrpc.MuSig2Version\"\x9d\x02\n\x14MuSig2SessionRequest\x12$\n\x07key_loc\x18\x01 \x01(\x0b\x32\x13.signrpc.KeyLocator\x12\x1a\n\x12\x61ll_signer_pubkeys\x18\x02 \x03(\x0c\x12\"\n\x1aother_signer_public_nonces\x18\x03 \x03(\x0c\x12\"\n\x06tweaks\x18\x04 \x03(\x0b\x32\x12.signrpc.TweakDesc\x12\x30\n\rtaproot_tweak\x18\x05 \x01(\x0b\x32\x19.signrpc.TaprootTweakDesc\x12\'\n\x07version\x18\x06 \x01(\x0e\x32\x16.signrpc.MuSig2Version\x12 \n\x18pregenerated_local_nonce\x18\x07 \x01(\x0c\"\xbe\x01\n\x15MuSig2SessionResponse\x12\x12\n\nsession_id\x18\x01 \x01(\x0c\x12\x14\n\x0c\x63ombined_key\x18\x02 \x01(\x0c\x12\x1c\n\x14taproot_internal_key\x18\x03 \x01(\x0c\x12\x1b\n\x13local_public_nonces\x18\x04 \x01(\x0c\x12\x17\n\x0fhave_all_nonces\x18\x05 \x01(\x08\x12\'\n\x07version\x18\x06 \x01(\x0e\x32\x16.signrpc.MuSig2Version\"U\n\x1bMuSig2RegisterNoncesRequest\x12\x12\n\nsession_id\x18\x01 \x01(\x0c\x12\"\n\x1aother_signer_public_nonces\x18\x03 \x03(\x0c\"7\n\x1cMuSig2RegisterNoncesResponse\x12\x17\n\x0fhave_all_nonces\x18\x01 \x01(\x08\"P\n\x11MuSig2SignRequest\x12\x12\n\nsession_id\x18\x01 \x01(\x0c\x12\x16\n\x0emessage_digest\x18\x02 \x01(\x0c\x12\x0f\n\x07\x63leanup\x18\x03 \x01(\x08\"5\n\x12MuSig2SignResponse\x12\x1f\n\x17local_partial_signature\x18\x01 \x01(\x0c\"O\n\x17MuSig2CombineSigRequest\x12\x12\n\nsession_id\x18\x01 \x01(\x0c\x12 \n\x18other_partial_signatures\x18\x02 \x03(\x0c\"P\n\x18MuSig2CombineSigResponse\x12\x1b\n\x13have_all_signatures\x18\x01 \x01(\x08\x12\x17\n\x0f\x66inal_signature\x18\x02 \x01(\x0c\"*\n\x14MuSig2CleanupRequest\x12\x12\n\nsession_id\x18\x01 \x01(\x0c\"\x17\n\x15MuSig2CleanupResponse*\x9c\x01\n\nSignMethod\x12\x1a\n\x16SIGN_METHOD_WITNESS_V0\x10\x00\x12)\n%SIGN_METHOD_TAPROOT_KEY_SPEND_BIP0086\x10\x01\x12!\n\x1dSIGN_METHOD_TAPROOT_KEY_SPEND\x10\x02\x12$\n SIGN_METHOD_TAPROOT_SCRIPT_SPEND\x10\x03*b\n\rMuSig2Version\x12\x1c\n\x18MUSIG2_VERSION_UNDEFINED\x10\x00\x12\x17\n\x13MUSIG2_VERSION_V040\x10\x01\x12\x1a\n\x16MUSIG2_VERSION_V100RC2\x10\x02\x32\xdb\x06\n\x06Signer\x12\x34\n\rSignOutputRaw\x12\x10.signrpc.SignReq\x1a\x11.signrpc.SignResp\x12@\n\x12\x43omputeInputScript\x12\x10.signrpc.SignReq\x1a\x18.signrpc.InputScriptResp\x12@\n\x0bSignMessage\x12\x17.signrpc.SignMessageReq\x1a\x18.signrpc.SignMessageResp\x12\x46\n\rVerifyMessage\x12\x19.signrpc.VerifyMessageReq\x1a\x1a.signrpc.VerifyMessageResp\x12H\n\x0f\x44\x65riveSharedKey\x12\x19.signrpc.SharedKeyRequest\x1a\x1a.signrpc.SharedKeyResponse\x12Z\n\x11MuSig2CombineKeys\x12!.signrpc.MuSig2CombineKeysRequest\x1a\".signrpc.MuSig2CombineKeysResponse\x12T\n\x13MuSig2CreateSession\x12\x1d.signrpc.MuSig2SessionRequest\x1a\x1e.signrpc.MuSig2SessionResponse\x12\x63\n\x14MuSig2RegisterNonces\x12$.signrpc.MuSig2RegisterNoncesRequest\x1a%.signrpc.MuSig2RegisterNoncesResponse\x12\x45\n\nMuSig2Sign\x12\x1a.signrpc.MuSig2SignRequest\x1a\x1b.signrpc.MuSig2SignResponse\x12W\n\x10MuSig2CombineSig\x12 .signrpc.MuSig2CombineSigRequest\x1a!.signrpc.MuSig2CombineSigResponse\x12N\n\rMuSig2Cleanup\x12\x1d.signrpc.MuSig2CleanupRequest\x1a\x1e.signrpc.MuSig2CleanupResponseB/Z-github.com/lightningnetwork/lnd/lnrpc/signrpcb\x06proto3')

_SIGNMETHOD = DESCRIPTOR.enum_types_by_name['SignMethod']
SignMethod = enum_type_wrapper.EnumTypeWrapper(_SIGNMETHOD)
_MUSIG2VERSION = DESCRIPTOR.enum_types_by_name['MuSig2Version']
MuSig2Version = enum_type_wrapper.EnumTypeWrapper(_MUSIG2VERSION)
SIGN_METHOD_WITNESS_V0 = 0
SIGN_METHOD_TAPROOT_KEY_SPEND_BIP0086 = 1
SIGN_METHOD_TAPROOT_KEY_SPEND = 2
SIGN_METHOD_TAPROOT_SCRIPT_SPEND = 3
MUSIG2_VERSION_UNDEFINED = 0
MUSIG2_VERSION_V040 = 1
MUSIG2_VERSION_V100RC2 = 2


_KEYLOCATOR = DESCRIPTOR.message_types_by_name['KeyLocator']
_KEYDESCRIPTOR = DESCRIPTOR.message_types_by_name['KeyDescriptor']
_TXOUT = DESCRIPTOR.message_types_by_name['TxOut']
_SIGNDESCRIPTOR = DESCRIPTOR.message_types_by_name['SignDescriptor']
_SIGNREQ = DESCRIPTOR.message_types_by_name['SignReq']
_SIGNRESP = DESCRIPTOR.message_types_by_name['SignResp']
_INPUTSCRIPT = DESCRIPTOR.message_types_by_name['InputScript']
_INPUTSCRIPTRESP = DESCRIPTOR.message_types_by_name['InputScriptResp']
_SIGNMESSAGEREQ = DESCRIPTOR.message_types_by_name['SignMessageReq']
_SIGNMESSAGERESP = DESCRIPTOR.message_types_by_name['SignMessageResp']
_VERIFYMESSAGEREQ = DESCRIPTOR.message_types_by_name['VerifyMessageReq']
_VERIFYMESSAGERESP = DESCRIPTOR.message_types_by_name['VerifyMessageResp']
_SHAREDKEYREQUEST = DESCRIPTOR.message_types_by_name['SharedKeyRequest']
_SHAREDKEYRESPONSE = DESCRIPTOR.message_types_by_name['SharedKeyResponse']
_TWEAKDESC = DESCRIPTOR.message_types_by_name['TweakDesc']
_TAPROOTTWEAKDESC = DESCRIPTOR.message_types_by_name['TaprootTweakDesc']
_MUSIG2COMBINEKEYSREQUEST = DESCRIPTOR.message_types_by_name['MuSig2CombineKeysRequest']
_MUSIG2COMBINEKEYSRESPONSE = DESCRIPTOR.message_types_by_name['MuSig2CombineKeysResponse']
_MUSIG2SESSIONREQUEST = DESCRIPTOR.message_types_by_name['MuSig2SessionRequest']
_MUSIG2SESSIONRESPONSE = DESCRIPTOR.message_types_by_name['MuSig2SessionResponse']
_MUSIG2REGISTERNONCESREQUEST = DESCRIPTOR.message_types_by_name['MuSig2RegisterNoncesRequest']
_MUSIG2REGISTERNONCESRESPONSE = DESCRIPTOR.message_types_by_name['MuSig2RegisterNoncesResponse']
_MUSIG2SIGNREQUEST = DESCRIPTOR.message_types_by_name['MuSig2SignRequest']
_MUSIG2SIGNRESPONSE = DESCRIPTOR.message_types_by_name['MuSig2SignResponse']
_MUSIG2COMBINESIGREQUEST = DESCRIPTOR.message_types_by_name['MuSig2CombineSigRequest']
_MUSIG2COMBINESIGRESPONSE = DESCRIPTOR.message_types_by_name['MuSig2CombineSigResponse']
_MUSIG2CLEANUPREQUEST = DESCRIPTOR.message_types_by_name['MuSig2CleanupRequest']
_MUSIG2CLEANUPRESPONSE = DESCRIPTOR.message_types_by_name['MuSig2CleanupResponse']
KeyLocator = _reflection.GeneratedProtocolMessageType('KeyLocator', (_message.Message,), {
  'DESCRIPTOR' : _KEYLOCATOR,
  '__module__' : 'lndgrpc.compiled.signer_pb2'
  # @@protoc_insertion_point(class_scope:signrpc.KeyLocator)
  })
_sym_db.RegisterMessage(KeyLocator)

KeyDescriptor = _reflection.GeneratedProtocolMessageType('KeyDescriptor', (_message.Message,), {
  'DESCRIPTOR' : _KEYDESCRIPTOR,
  '__module__' : 'lndgrpc.compiled.signer_pb2'
  # @@protoc_insertion_point(class_scope:signrpc.KeyDescriptor)
  })
_sym_db.RegisterMessage(KeyDescriptor)

TxOut = _reflection.GeneratedProtocolMessageType('TxOut', (_message.Message,), {
  'DESCRIPTOR' : _TXOUT,
  '__module__' : 'lndgrpc.compiled.signer_pb2'
  # @@protoc_insertion_point(class_scope:signrpc.TxOut)
  })
_sym_db.RegisterMessage(TxOut)

SignDescriptor = _reflection.GeneratedProtocolMessageType('SignDescriptor', (_message.Message,), {
  'DESCRIPTOR' : _SIGNDESCRIPTOR,
  '__module__' : 'lndgrpc.compiled.signer_pb2'
  # @@protoc_insertion_point(class_scope:signrpc.SignDescriptor)
  })
_sym_db.RegisterMessage(SignDescriptor)

SignReq = _reflection.GeneratedProtocolMessageType('SignReq', (_message.Message,), {
  'DESCRIPTOR' : _SIGNREQ,
  '__module__' : 'lndgrpc.compiled.signer_pb2'
  # @@protoc_insertion_point(class_scope:signrpc.SignReq)
  })
_sym_db.RegisterMessage(SignReq)

SignResp = _reflection.GeneratedProtocolMessageType('SignResp', (_message.Message,), {
  'DESCRIPTOR' : _SIGNRESP,
  '__module__' : 'lndgrpc.compiled.signer_pb2'
  # @@protoc_insertion_point(class_scope:signrpc.SignResp)
  })
_sym_db.RegisterMessage(SignResp)

InputScript = _reflection.GeneratedProtocolMessageType('InputScript', (_message.Message,), {
  'DESCRIPTOR' : _INPUTSCRIPT,
  '__module__' : 'lndgrpc.compiled.signer_pb2'
  # @@protoc_insertion_point(class_scope:signrpc.InputScript)
  })
_sym_db.RegisterMessage(InputScript)

InputScriptResp = _reflection.GeneratedProtocolMessageType('InputScriptResp', (_message.Message,), {
  'DESCRIPTOR' : _INPUTSCRIPTRESP,
  '__module__' : 'lndgrpc.compiled.signer_pb2'
  # @@protoc_insertion_point(class_scope:signrpc.InputScriptResp)
  })
_sym_db.RegisterMessage(InputScriptResp)

SignMessageReq = _reflection.GeneratedProtocolMessageType('SignMessageReq', (_message.Message,), {
  'DESCRIPTOR' : _SIGNMESSAGEREQ,
  '__module__' : 'lndgrpc.compiled.signer_pb2'
  # @@protoc_insertion_point(class_scope:signrpc.SignMessageReq)
  })
_sym_db.RegisterMessage(SignMessageReq)

SignMessageResp = _reflection.GeneratedProtocolMessageType('SignMessageResp', (_message.Message,), {
  'DESCRIPTOR' : _SIGNMESSAGERESP,
  '__module__' : 'lndgrpc.compiled.signer_pb2'
  # @@protoc_insertion_point(class_scope:signrpc.SignMessageResp)
  })
_sym_db.RegisterMessage(SignMessageResp)

VerifyMessageReq = _reflection.GeneratedProtocolMessageType('VerifyMessageReq', (_message.Message,), {
  'DESCRIPTOR' : _VERIFYMESSAGEREQ,
  '__module__' : 'lndgrpc.compiled.signer_pb2'
  # @@protoc_insertion_point(class_scope:signrpc.VerifyMessageReq)
  })
_sym_db.RegisterMessage(VerifyMessageReq)

VerifyMessageResp = _reflection.GeneratedProtocolMessageType('VerifyMessageResp', (_message.Message,), {
  'DESCRIPTOR' : _VERIFYMESSAGERESP,
  '__module__' : 'lndgrpc.compiled.signer_pb2'
  # @@protoc_insertion_point(class_scope:signrpc.VerifyMessageResp)
  })
_sym_db.RegisterMessage(VerifyMessageResp)

SharedKeyRequest = _reflection.GeneratedProtocolMessageType('SharedKeyRequest', (_message.Message,), {
  'DESCRIPTOR' : _SHAREDKEYREQUEST,
  '__module__' : 'lndgrpc.compiled.signer_pb2'
  # @@protoc_insertion_point(class_scope:signrpc.SharedKeyRequest)
  })
_sym_db.RegisterMessage(SharedKeyRequest)

SharedKeyResponse = _reflection.GeneratedProtocolMessageType('SharedKeyResponse', (_message.Message,), {
  'DESCRIPTOR' : _SHAREDKEYRESPONSE,
  '__module__' : 'lndgrpc.compiled.signer_pb2'
  # @@protoc_insertion_point(class_scope:signrpc.SharedKeyResponse)
  })
_sym_db.RegisterMessage(SharedKeyResponse)

TweakDesc = _reflection.GeneratedProtocolMessageType('TweakDesc', (_message.Message,), {
  'DESCRIPTOR' : _TWEAKDESC,
  '__module__' : 'lndgrpc.compiled.signer_pb2'
  # @@protoc_insertion_point(class_scope:signrpc.TweakDesc)
  })
_sym_db.RegisterMessage(TweakDesc)

TaprootTweakDesc = _reflection.GeneratedProtocolMessageType('TaprootTweakDesc', (_message.Message,), {
  'DESCRIPTOR' : _TAPROOTTWEAKDESC,
  '__module__' : 'lndgrpc.compiled.signer_pb2'
  # @@protoc_insertion_point(class_scope:signrpc.TaprootTweakDesc)
  })
_sym_db.RegisterMessage(TaprootTweakDesc)

MuSig2CombineKeysRequest = _reflection.GeneratedProtocolMessageType('MuSig2CombineKeysRequest', (_message.Message,), {
  'DESCRIPTOR' : _MUSIG2COMBINEKEYSREQUEST,
  '__module__' : 'lndgrpc.compiled.signer_pb2'
  # @@protoc_insertion_point(class_scope:signrpc.MuSig2CombineKeysRequest)
  })
_sym_db.RegisterMessage(MuSig2CombineKeysRequest)

MuSig2CombineKeysResponse = _reflection.GeneratedProtocolMessageType('MuSig2CombineKeysResponse', (_message.Message,), {
  'DESCRIPTOR' : _MUSIG2COMBINEKEYSRESPONSE,
  '__module__' : 'lndgrpc.compiled.signer_pb2'
  # @@protoc_insertion_point(class_scope:signrpc.MuSig2CombineKeysResponse)
  })
_sym_db.RegisterMessage(MuSig2CombineKeysResponse)

MuSig2SessionRequest = _reflection.GeneratedProtocolMessageType('MuSig2SessionRequest', (_message.Message,), {
  'DESCRIPTOR' : _MUSIG2SESSIONREQUEST,
  '__module__' : 'lndgrpc.compiled.signer_pb2'
  # @@protoc_insertion_point(class_scope:signrpc.MuSig2SessionRequest)
  })
_sym_db.RegisterMessage(MuSig2SessionRequest)

MuSig2SessionResponse = _reflection.GeneratedProtocolMessageType('MuSig2SessionResponse', (_message.Message,), {
  'DESCRIPTOR' : _MUSIG2SESSIONRESPONSE,
  '__module__' : 'lndgrpc.compiled.signer_pb2'
  # @@protoc_insertion_point(class_scope:signrpc.MuSig2SessionResponse)
  })
_sym_db.RegisterMessage(MuSig2SessionResponse)

MuSig2RegisterNoncesRequest = _reflection.GeneratedProtocolMessageType('MuSig2RegisterNoncesRequest', (_message.Message,), {
  'DESCRIPTOR' : _MUSIG2REGISTERNONCESREQUEST,
  '__module__' : 'lndgrpc.compiled.signer_pb2'
  # @@protoc_insertion_point(class_scope:signrpc.MuSig2RegisterNoncesRequest)
  })
_sym_db.RegisterMessage(MuSig2RegisterNoncesRequest)

MuSig2RegisterNoncesResponse = _reflection.GeneratedProtocolMessageType('MuSig2RegisterNoncesResponse', (_message.Message,), {
  'DESCRIPTOR' : _MUSIG2REGISTERNONCESRESPONSE,
  '__module__' : 'lndgrpc.compiled.signer_pb2'
  # @@protoc_insertion_point(class_scope:signrpc.MuSig2RegisterNoncesResponse)
  })
_sym_db.RegisterMessage(MuSig2RegisterNoncesResponse)

MuSig2SignRequest = _reflection.GeneratedProtocolMessageType('MuSig2SignRequest', (_message.Message,), {
  'DESCRIPTOR' : _MUSIG2SIGNREQUEST,
  '__module__' : 'lndgrpc.compiled.signer_pb2'
  # @@protoc_insertion_point(class_scope:signrpc.MuSig2SignRequest)
  })
_sym_db.RegisterMessage(MuSig2SignRequest)

MuSig2SignResponse = _reflection.GeneratedProtocolMessageType('MuSig2SignResponse', (_message.Message,), {
  'DESCRIPTOR' : _MUSIG2SIGNRESPONSE,
  '__module__' : 'lndgrpc.compiled.signer_pb2'
  # @@protoc_insertion_point(class_scope:signrpc.MuSig2SignResponse)
  })
_sym_db.RegisterMessage(MuSig2SignResponse)

MuSig2CombineSigRequest = _reflection.GeneratedProtocolMessageType('MuSig2CombineSigRequest', (_message.Message,), {
  'DESCRIPTOR' : _MUSIG2COMBINESIGREQUEST,
  '__module__' : 'lndgrpc.compiled.signer_pb2'
  # @@protoc_insertion_point(class_scope:signrpc.MuSig2CombineSigRequest)
  })
_sym_db.RegisterMessage(MuSig2CombineSigRequest)

MuSig2CombineSigResponse = _reflection.GeneratedProtocolMessageType('MuSig2CombineSigResponse', (_message.Message,), {
  'DESCRIPTOR' : _MUSIG2COMBINESIGRESPONSE,
  '__module__' : 'lndgrpc.compiled.signer_pb2'
  # @@protoc_insertion_point(class_scope:signrpc.MuSig2CombineSigResponse)
  })
_sym_db.RegisterMessage(MuSig2CombineSigResponse)

MuSig2CleanupRequest = _reflection.GeneratedProtocolMessageType('MuSig2CleanupRequest', (_message.Message,), {
  'DESCRIPTOR' : _MUSIG2CLEANUPREQUEST,
  '__module__' : 'lndgrpc.compiled.signer_pb2'
  # @@protoc_insertion_point(class_scope:signrpc.MuSig2CleanupRequest)
  })
_sym_db.RegisterMessage(MuSig2CleanupRequest)

MuSig2CleanupResponse = _reflection.GeneratedProtocolMessageType('MuSig2CleanupResponse', (_message.Message,), {
  'DESCRIPTOR' : _MUSIG2CLEANUPRESPONSE,
  '__module__' : 'lndgrpc.compiled.signer_pb2'
  # @@protoc_insertion_point(class_scope:signrpc.MuSig2CleanupResponse)
  })
_sym_db.RegisterMessage(MuSig2CleanupResponse)

_SIGNER = DESCRIPTOR.services_by_name['Signer']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z-github.com/lightningnetwork/lnd/lnrpc/signrpc'
  _SHAREDKEYREQUEST.fields_by_name['key_loc']._options = None
  _SHAREDKEYREQUEST.fields_by_name['key_loc']._serialized_options = b'\030\001'
  _SIGNMETHOD._serialized_start=2679
  _SIGNMETHOD._serialized_end=2835
  _MUSIG2VERSION._serialized_start=2837
  _MUSIG2VERSION._serialized_end=2935
  _KEYLOCATOR._serialized_start=42
  _KEYLOCATOR._serialized_end=93
  _KEYDESCRIPTOR._serialized_start=95
  _KEYDESCRIPTOR._serialized_end=171
  _TXOUT._serialized_start=173
  _TXOUT._serialized_end=214
  _SIGNDESCRIPTOR._serialized_start=217
  _SIGNDESCRIPTOR._serialized_end=474
  _SIGNREQ._serialized_start=476
  _SIGNREQ._serialized_end=590
  _SIGNRESP._serialized_start=592
  _SIGNRESP._serialized_end=620
  _INPUTSCRIPT._serialized_start=622
  _INPUTSCRIPT._serialized_end=672
  _INPUTSCRIPTRESP._serialized_start=674
  _INPUTSCRIPTRESP._serialized_end=736
  _SIGNMESSAGEREQ._serialized_start=739
  _SIGNMESSAGEREQ._serialized_end=913
  _SIGNMESSAGERESP._serialized_start=915
  _SIGNMESSAGERESP._serialized_end=951
  _VERIFYMESSAGEREQ._serialized_start=953
  _VERIFYMESSAGEREQ._serialized_end=1056
  _VERIFYMESSAGERESP._serialized_start=1058
  _VERIFYMESSAGERESP._serialized_end=1092
  _SHAREDKEYREQUEST._serialized_start=1095
  _SHAREDKEYREQUEST._serialized_end=1223
  _SHAREDKEYRESPONSE._serialized_start=1225
  _SHAREDKEYRESPONSE._serialized_end=1264
  _TWEAKDESC._serialized_start=1266
  _TWEAKDESC._serialized_end=1311
  _TAPROOTTWEAKDESC._serialized_start=1313
  _TAPROOTTWEAKDESC._serialized_end=1376
  _MUSIG2COMBINEKEYSREQUEST._serialized_start=1379
  _MUSIG2COMBINEKEYSREQUEST._serialized_end=1560
  _MUSIG2COMBINEKEYSRESPONSE._serialized_start=1562
  _MUSIG2COMBINEKEYSRESPONSE._serialized_end=1682
  _MUSIG2SESSIONREQUEST._serialized_start=1685
  _MUSIG2SESSIONREQUEST._serialized_end=1970
  _MUSIG2SESSIONRESPONSE._serialized_start=1973
  _MUSIG2SESSIONRESPONSE._serialized_end=2163
  _MUSIG2REGISTERNONCESREQUEST._serialized_start=2165
  _MUSIG2REGISTERNONCESREQUEST._serialized_end=2250
  _MUSIG2REGISTERNONCESRESPONSE._serialized_start=2252
  _MUSIG2REGISTERNONCESRESPONSE._serialized_end=2307
  _MUSIG2SIGNREQUEST._serialized_start=2309
  _MUSIG2SIGNREQUEST._serialized_end=2389
  _MUSIG2SIGNRESPONSE._serialized_start=2391
  _MUSIG2SIGNRESPONSE._serialized_end=2444
  _MUSIG2COMBINESIGREQUEST._serialized_start=2446
  _MUSIG2COMBINESIGREQUEST._serialized_end=2525
  _MUSIG2COMBINESIGRESPONSE._serialized_start=2527
  _MUSIG2COMBINESIGRESPONSE._serialized_end=2607
  _MUSIG2CLEANUPREQUEST._serialized_start=2609
  _MUSIG2CLEANUPREQUEST._serialized_end=2651
  _MUSIG2CLEANUPRESPONSE._serialized_start=2653
  _MUSIG2CLEANUPRESPONSE._serialized_end=2676
  _SIGNER._serialized_start=2938
  _SIGNER._serialized_end=3797
# @@protoc_insertion_point(module_scope)
