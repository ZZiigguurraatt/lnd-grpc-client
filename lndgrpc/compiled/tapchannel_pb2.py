# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lndgrpc/compiled/tapchannel.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from lndgrpc.compiled import rfq_pb2 as lndgrpc_dot_compiled_dot_rfq__pb2
from lndgrpc.compiled import lightning_pb2 as lndgrpc_dot_compiled_dot_lightning__pb2
from lndgrpc.compiled import router_pb2 as lndgrpc_dot_compiled_dot_router__pb2
from lndgrpc.compiled import taprootassets_pb2 as lndgrpc_dot_compiled_dot_taprootassets__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!lndgrpc/compiled/tapchannel.proto\x12\rtapchannelrpc\x1a\x1alndgrpc/compiled/rfq.proto\x1a lndgrpc/compiled/lightning.proto\x1a\x1dlndgrpc/compiled/router.proto\x1a$lndgrpc/compiled/taprootassets.proto\"\x96\x01\n\x12\x46undChannelRequest\x12\x14\n\x0c\x61sset_amount\x18\x01 \x01(\x04\x12\x10\n\x08\x61sset_id\x18\x02 \x01(\x0c\x12\x13\n\x0bpeer_pubkey\x18\x03 \x01(\x0c\x12\x1e\n\x16\x66\x65\x65_rate_sat_per_vbyte\x18\x04 \x01(\r\x12\x10\n\x08push_sat\x18\x05 \x01(\x03\x12\x11\n\tgroup_key\x18\x06 \x01(\x0c\"9\n\x13\x46undChannelResponse\x12\x0c\n\x04txid\x18\x01 \x01(\t\x12\x14\n\x0coutput_index\x18\x02 \x01(\x05\"\xab\x01\n\x15RouterSendPaymentData\x12M\n\rasset_amounts\x18\x01 \x03(\x0b\x32\x36.tapchannelrpc.RouterSendPaymentData.AssetAmountsEntry\x12\x0e\n\x06rfq_id\x18\x02 \x01(\x0c\x1a\x33\n\x11\x41ssetAmountsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x04:\x02\x38\x01\"j\n\x1a\x45ncodeCustomRecordsRequest\x12\x43\n\x13router_send_payment\x18\x01 \x01(\x0b\x32$.tapchannelrpc.RouterSendPaymentDataH\x00\x42\x07\n\x05input\"\xaa\x01\n\x1b\x45ncodeCustomRecordsResponse\x12U\n\x0e\x63ustom_records\x18\x01 \x03(\x0b\x32=.tapchannelrpc.EncodeCustomRecordsResponse.CustomRecordsEntry\x1a\x34\n\x12\x43ustomRecordsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x04\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"\xc3\x01\n\x12SendPaymentRequest\x12\x10\n\x08\x61sset_id\x18\x01 \x01(\x0c\x12\x14\n\x0c\x61sset_amount\x18\x02 \x01(\x04\x12\x13\n\x0bpeer_pubkey\x18\x03 \x01(\x0c\x12\x36\n\x0fpayment_request\x18\x04 \x01(\x0b\x32\x1d.routerrpc.SendPaymentRequest\x12\x0e\n\x06rfq_id\x18\x05 \x01(\x0c\x12\x15\n\rallow_overpay\x18\x06 \x01(\x08\x12\x11\n\tgroup_key\x18\x07 \x01(\x0c\"\x87\x01\n\x13SendPaymentResponse\x12<\n\x13\x61\x63\x63\x65pted_sell_order\x18\x01 \x01(\x0b\x32\x1d.rfqrpc.PeerAcceptedSellQuoteH\x00\x12(\n\x0epayment_result\x18\x02 \x01(\x0b\x32\x0e.lnrpc.PaymentH\x00\x42\x08\n\x06result\"#\n\x0bHodlInvoice\x12\x14\n\x0cpayment_hash\x18\x01 \x01(\x0c\"\xbe\x01\n\x11\x41\x64\x64InvoiceRequest\x12\x10\n\x08\x61sset_id\x18\x01 \x01(\x0c\x12\x14\n\x0c\x61sset_amount\x18\x02 \x01(\x04\x12\x13\n\x0bpeer_pubkey\x18\x03 \x01(\x0c\x12\'\n\x0finvoice_request\x18\x04 \x01(\x0b\x32\x0e.lnrpc.Invoice\x12\x30\n\x0chodl_invoice\x18\x05 \x01(\x0b\x32\x1a.tapchannelrpc.HodlInvoice\x12\x11\n\tgroup_key\x18\x06 \x01(\x0c\"\x81\x01\n\x12\x41\x64\x64InvoiceResponse\x12\x38\n\x12\x61\x63\x63\x65pted_buy_quote\x18\x01 \x01(\x0b\x32\x1c.rfqrpc.PeerAcceptedBuyQuote\x12\x31\n\x0einvoice_result\x18\x02 \x01(\x0b\x32\x19.lnrpc.AddInvoiceResponse\"J\n\x0b\x41ssetPayReq\x12\x10\n\x08\x61sset_id\x18\x01 \x01(\x0c\x12\x16\n\x0epay_req_string\x18\x02 \x01(\t\x12\x11\n\tgroup_key\x18\x03 \x01(\x0c\"\xd0\x01\n\x13\x41ssetPayReqResponse\x12\x14\n\x0c\x61sset_amount\x18\x01 \x01(\x04\x12/\n\x0f\x64\x65\x63imal_display\x18\x02 \x01(\x0b\x32\x16.taprpc.DecimalDisplay\x12\'\n\x0b\x61sset_group\x18\x03 \x01(\x0b\x32\x12.taprpc.AssetGroup\x12)\n\x0cgenesis_info\x18\x04 \x01(\x0b\x32\x13.taprpc.GenesisInfo\x12\x1e\n\x07pay_req\x18\x05 \x01(\x0b\x32\r.lnrpc.PayReq2\xdf\x03\n\x14TaprootAssetChannels\x12T\n\x0b\x46undChannel\x12!.tapchannelrpc.FundChannelRequest\x1a\".tapchannelrpc.FundChannelResponse\x12q\n\x13\x45ncodeCustomRecords\x12).tapchannelrpc.EncodeCustomRecordsRequest\x1a*.tapchannelrpc.EncodeCustomRecordsResponse\"\x03\x88\x02\x01\x12V\n\x0bSendPayment\x12!.tapchannelrpc.SendPaymentRequest\x1a\".tapchannelrpc.SendPaymentResponse0\x01\x12Q\n\nAddInvoice\x12 .tapchannelrpc.AddInvoiceRequest\x1a!.tapchannelrpc.AddInvoiceResponse\x12S\n\x11\x44\x65\x63odeAssetPayReq\x12\x1a.tapchannelrpc.AssetPayReq\x1a\".tapchannelrpc.AssetPayReqResponseB>Z<github.com/lightninglabs/taproot-assets/taprpc/tapchannelrpcb\x06proto3')



_FUNDCHANNELREQUEST = DESCRIPTOR.message_types_by_name['FundChannelRequest']
_FUNDCHANNELRESPONSE = DESCRIPTOR.message_types_by_name['FundChannelResponse']
_ROUTERSENDPAYMENTDATA = DESCRIPTOR.message_types_by_name['RouterSendPaymentData']
_ROUTERSENDPAYMENTDATA_ASSETAMOUNTSENTRY = _ROUTERSENDPAYMENTDATA.nested_types_by_name['AssetAmountsEntry']
_ENCODECUSTOMRECORDSREQUEST = DESCRIPTOR.message_types_by_name['EncodeCustomRecordsRequest']
_ENCODECUSTOMRECORDSRESPONSE = DESCRIPTOR.message_types_by_name['EncodeCustomRecordsResponse']
_ENCODECUSTOMRECORDSRESPONSE_CUSTOMRECORDSENTRY = _ENCODECUSTOMRECORDSRESPONSE.nested_types_by_name['CustomRecordsEntry']
_SENDPAYMENTREQUEST = DESCRIPTOR.message_types_by_name['SendPaymentRequest']
_SENDPAYMENTRESPONSE = DESCRIPTOR.message_types_by_name['SendPaymentResponse']
_HODLINVOICE = DESCRIPTOR.message_types_by_name['HodlInvoice']
_ADDINVOICEREQUEST = DESCRIPTOR.message_types_by_name['AddInvoiceRequest']
_ADDINVOICERESPONSE = DESCRIPTOR.message_types_by_name['AddInvoiceResponse']
_ASSETPAYREQ = DESCRIPTOR.message_types_by_name['AssetPayReq']
_ASSETPAYREQRESPONSE = DESCRIPTOR.message_types_by_name['AssetPayReqResponse']
FundChannelRequest = _reflection.GeneratedProtocolMessageType('FundChannelRequest', (_message.Message,), {
  'DESCRIPTOR' : _FUNDCHANNELREQUEST,
  '__module__' : 'lndgrpc.compiled.tapchannel_pb2'
  # @@protoc_insertion_point(class_scope:tapchannelrpc.FundChannelRequest)
  })
_sym_db.RegisterMessage(FundChannelRequest)

FundChannelResponse = _reflection.GeneratedProtocolMessageType('FundChannelResponse', (_message.Message,), {
  'DESCRIPTOR' : _FUNDCHANNELRESPONSE,
  '__module__' : 'lndgrpc.compiled.tapchannel_pb2'
  # @@protoc_insertion_point(class_scope:tapchannelrpc.FundChannelResponse)
  })
_sym_db.RegisterMessage(FundChannelResponse)

RouterSendPaymentData = _reflection.GeneratedProtocolMessageType('RouterSendPaymentData', (_message.Message,), {

  'AssetAmountsEntry' : _reflection.GeneratedProtocolMessageType('AssetAmountsEntry', (_message.Message,), {
    'DESCRIPTOR' : _ROUTERSENDPAYMENTDATA_ASSETAMOUNTSENTRY,
    '__module__' : 'lndgrpc.compiled.tapchannel_pb2'
    # @@protoc_insertion_point(class_scope:tapchannelrpc.RouterSendPaymentData.AssetAmountsEntry)
    })
  ,
  'DESCRIPTOR' : _ROUTERSENDPAYMENTDATA,
  '__module__' : 'lndgrpc.compiled.tapchannel_pb2'
  # @@protoc_insertion_point(class_scope:tapchannelrpc.RouterSendPaymentData)
  })
_sym_db.RegisterMessage(RouterSendPaymentData)
_sym_db.RegisterMessage(RouterSendPaymentData.AssetAmountsEntry)

EncodeCustomRecordsRequest = _reflection.GeneratedProtocolMessageType('EncodeCustomRecordsRequest', (_message.Message,), {
  'DESCRIPTOR' : _ENCODECUSTOMRECORDSREQUEST,
  '__module__' : 'lndgrpc.compiled.tapchannel_pb2'
  # @@protoc_insertion_point(class_scope:tapchannelrpc.EncodeCustomRecordsRequest)
  })
_sym_db.RegisterMessage(EncodeCustomRecordsRequest)

EncodeCustomRecordsResponse = _reflection.GeneratedProtocolMessageType('EncodeCustomRecordsResponse', (_message.Message,), {

  'CustomRecordsEntry' : _reflection.GeneratedProtocolMessageType('CustomRecordsEntry', (_message.Message,), {
    'DESCRIPTOR' : _ENCODECUSTOMRECORDSRESPONSE_CUSTOMRECORDSENTRY,
    '__module__' : 'lndgrpc.compiled.tapchannel_pb2'
    # @@protoc_insertion_point(class_scope:tapchannelrpc.EncodeCustomRecordsResponse.CustomRecordsEntry)
    })
  ,
  'DESCRIPTOR' : _ENCODECUSTOMRECORDSRESPONSE,
  '__module__' : 'lndgrpc.compiled.tapchannel_pb2'
  # @@protoc_insertion_point(class_scope:tapchannelrpc.EncodeCustomRecordsResponse)
  })
_sym_db.RegisterMessage(EncodeCustomRecordsResponse)
_sym_db.RegisterMessage(EncodeCustomRecordsResponse.CustomRecordsEntry)

SendPaymentRequest = _reflection.GeneratedProtocolMessageType('SendPaymentRequest', (_message.Message,), {
  'DESCRIPTOR' : _SENDPAYMENTREQUEST,
  '__module__' : 'lndgrpc.compiled.tapchannel_pb2'
  # @@protoc_insertion_point(class_scope:tapchannelrpc.SendPaymentRequest)
  })
_sym_db.RegisterMessage(SendPaymentRequest)

SendPaymentResponse = _reflection.GeneratedProtocolMessageType('SendPaymentResponse', (_message.Message,), {
  'DESCRIPTOR' : _SENDPAYMENTRESPONSE,
  '__module__' : 'lndgrpc.compiled.tapchannel_pb2'
  # @@protoc_insertion_point(class_scope:tapchannelrpc.SendPaymentResponse)
  })
_sym_db.RegisterMessage(SendPaymentResponse)

HodlInvoice = _reflection.GeneratedProtocolMessageType('HodlInvoice', (_message.Message,), {
  'DESCRIPTOR' : _HODLINVOICE,
  '__module__' : 'lndgrpc.compiled.tapchannel_pb2'
  # @@protoc_insertion_point(class_scope:tapchannelrpc.HodlInvoice)
  })
_sym_db.RegisterMessage(HodlInvoice)

AddInvoiceRequest = _reflection.GeneratedProtocolMessageType('AddInvoiceRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDINVOICEREQUEST,
  '__module__' : 'lndgrpc.compiled.tapchannel_pb2'
  # @@protoc_insertion_point(class_scope:tapchannelrpc.AddInvoiceRequest)
  })
_sym_db.RegisterMessage(AddInvoiceRequest)

AddInvoiceResponse = _reflection.GeneratedProtocolMessageType('AddInvoiceResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDINVOICERESPONSE,
  '__module__' : 'lndgrpc.compiled.tapchannel_pb2'
  # @@protoc_insertion_point(class_scope:tapchannelrpc.AddInvoiceResponse)
  })
_sym_db.RegisterMessage(AddInvoiceResponse)

AssetPayReq = _reflection.GeneratedProtocolMessageType('AssetPayReq', (_message.Message,), {
  'DESCRIPTOR' : _ASSETPAYREQ,
  '__module__' : 'lndgrpc.compiled.tapchannel_pb2'
  # @@protoc_insertion_point(class_scope:tapchannelrpc.AssetPayReq)
  })
_sym_db.RegisterMessage(AssetPayReq)

AssetPayReqResponse = _reflection.GeneratedProtocolMessageType('AssetPayReqResponse', (_message.Message,), {
  'DESCRIPTOR' : _ASSETPAYREQRESPONSE,
  '__module__' : 'lndgrpc.compiled.tapchannel_pb2'
  # @@protoc_insertion_point(class_scope:tapchannelrpc.AssetPayReqResponse)
  })
_sym_db.RegisterMessage(AssetPayReqResponse)

_TAPROOTASSETCHANNELS = DESCRIPTOR.services_by_name['TaprootAssetChannels']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z<github.com/lightninglabs/taproot-assets/taprpc/tapchannelrpc'
  _ROUTERSENDPAYMENTDATA_ASSETAMOUNTSENTRY._options = None
  _ROUTERSENDPAYMENTDATA_ASSETAMOUNTSENTRY._serialized_options = b'8\001'
  _ENCODECUSTOMRECORDSRESPONSE_CUSTOMRECORDSENTRY._options = None
  _ENCODECUSTOMRECORDSRESPONSE_CUSTOMRECORDSENTRY._serialized_options = b'8\001'
  _TAPROOTASSETCHANNELS.methods_by_name['EncodeCustomRecords']._options = None
  _TAPROOTASSETCHANNELS.methods_by_name['EncodeCustomRecords']._serialized_options = b'\210\002\001'
  _FUNDCHANNELREQUEST._serialized_start=184
  _FUNDCHANNELREQUEST._serialized_end=334
  _FUNDCHANNELRESPONSE._serialized_start=336
  _FUNDCHANNELRESPONSE._serialized_end=393
  _ROUTERSENDPAYMENTDATA._serialized_start=396
  _ROUTERSENDPAYMENTDATA._serialized_end=567
  _ROUTERSENDPAYMENTDATA_ASSETAMOUNTSENTRY._serialized_start=516
  _ROUTERSENDPAYMENTDATA_ASSETAMOUNTSENTRY._serialized_end=567
  _ENCODECUSTOMRECORDSREQUEST._serialized_start=569
  _ENCODECUSTOMRECORDSREQUEST._serialized_end=675
  _ENCODECUSTOMRECORDSRESPONSE._serialized_start=678
  _ENCODECUSTOMRECORDSRESPONSE._serialized_end=848
  _ENCODECUSTOMRECORDSRESPONSE_CUSTOMRECORDSENTRY._serialized_start=796
  _ENCODECUSTOMRECORDSRESPONSE_CUSTOMRECORDSENTRY._serialized_end=848
  _SENDPAYMENTREQUEST._serialized_start=851
  _SENDPAYMENTREQUEST._serialized_end=1046
  _SENDPAYMENTRESPONSE._serialized_start=1049
  _SENDPAYMENTRESPONSE._serialized_end=1184
  _HODLINVOICE._serialized_start=1186
  _HODLINVOICE._serialized_end=1221
  _ADDINVOICEREQUEST._serialized_start=1224
  _ADDINVOICEREQUEST._serialized_end=1414
  _ADDINVOICERESPONSE._serialized_start=1417
  _ADDINVOICERESPONSE._serialized_end=1546
  _ASSETPAYREQ._serialized_start=1548
  _ASSETPAYREQ._serialized_end=1622
  _ASSETPAYREQRESPONSE._serialized_start=1625
  _ASSETPAYREQRESPONSE._serialized_end=1833
  _TAPROOTASSETCHANNELS._serialized_start=1836
  _TAPROOTASSETCHANNELS._serialized_end=2315
# @@protoc_insertion_point(module_scope)
