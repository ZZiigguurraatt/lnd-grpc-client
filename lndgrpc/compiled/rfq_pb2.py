# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lndgrpc/compiled/rfq.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1alndgrpc/compiled/rfq.proto\x12\x06rfqrpc\"p\n\x0e\x41ssetSpecifier\x12\x12\n\x08\x61sset_id\x18\x01 \x01(\x0cH\x00\x12\x16\n\x0c\x61sset_id_str\x18\x02 \x01(\tH\x00\x12\x13\n\tgroup_key\x18\x03 \x01(\x0cH\x00\x12\x17\n\rgroup_key_str\x18\x04 \x01(\tH\x00\x42\x04\n\x02id\"0\n\nFixedPoint\x12\x13\n\x0b\x63oefficient\x18\x01 \x01(\t\x12\r\n\x05scale\x18\x02 \x01(\r\"\xc2\x01\n\x17\x41\x64\x64\x41ssetBuyOrderRequest\x12/\n\x0f\x61sset_specifier\x18\x01 \x01(\x0b\x32\x16.rfqrpc.AssetSpecifier\x12\x15\n\rasset_max_amt\x18\x02 \x01(\x04\x12\x0e\n\x06\x65xpiry\x18\x03 \x01(\x04\x12\x14\n\x0cpeer_pub_key\x18\x04 \x01(\x0c\x12\x17\n\x0ftimeout_seconds\x18\x05 \x01(\r\x12 \n\x18skip_asset_channel_check\x18\x06 \x01(\x08\"\xce\x01\n\x18\x41\x64\x64\x41ssetBuyOrderResponse\x12\x36\n\x0e\x61\x63\x63\x65pted_quote\x18\x01 \x01(\x0b\x32\x1c.rfqrpc.PeerAcceptedBuyQuoteH\x00\x12\x35\n\rinvalid_quote\x18\x02 \x01(\x0b\x32\x1c.rfqrpc.InvalidQuoteResponseH\x00\x12\x37\n\x0erejected_quote\x18\x03 \x01(\x0b\x32\x1d.rfqrpc.RejectedQuoteResponseH\x00\x42\n\n\x08response\"\xc5\x01\n\x18\x41\x64\x64\x41ssetSellOrderRequest\x12/\n\x0f\x61sset_specifier\x18\x01 \x01(\x0b\x32\x16.rfqrpc.AssetSpecifier\x12\x17\n\x0fpayment_max_amt\x18\x02 \x01(\x04\x12\x0e\n\x06\x65xpiry\x18\x03 \x01(\x04\x12\x14\n\x0cpeer_pub_key\x18\x04 \x01(\x0c\x12\x17\n\x0ftimeout_seconds\x18\x05 \x01(\r\x12 \n\x18skip_asset_channel_check\x18\x06 \x01(\x08\"\xd0\x01\n\x19\x41\x64\x64\x41ssetSellOrderResponse\x12\x37\n\x0e\x61\x63\x63\x65pted_quote\x18\x01 \x01(\x0b\x32\x1d.rfqrpc.PeerAcceptedSellQuoteH\x00\x12\x35\n\rinvalid_quote\x18\x02 \x01(\x0b\x32\x1c.rfqrpc.InvalidQuoteResponseH\x00\x12\x37\n\x0erejected_quote\x18\x03 \x01(\x0b\x32\x1d.rfqrpc.RejectedQuoteResponseH\x00\x42\n\n\x08response\"^\n\x18\x41\x64\x64\x41ssetSellOfferRequest\x12/\n\x0f\x61sset_specifier\x18\x01 \x01(\x0b\x32\x16.rfqrpc.AssetSpecifier\x12\x11\n\tmax_units\x18\x02 \x01(\x04\"\x1b\n\x19\x41\x64\x64\x41ssetSellOfferResponse\"]\n\x17\x41\x64\x64\x41ssetBuyOfferRequest\x12/\n\x0f\x61sset_specifier\x18\x01 \x01(\x0b\x32\x16.rfqrpc.AssetSpecifier\x12\x11\n\tmax_units\x18\x02 \x01(\x04\"\x1a\n\x18\x41\x64\x64\x41ssetBuyOfferResponse\" \n\x1eQueryPeerAcceptedQuotesRequest\"\xb5\x01\n\x14PeerAcceptedBuyQuote\x12\x0c\n\x04peer\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x0c\x12\x0c\n\x04scid\x18\x03 \x01(\x04\x12\x18\n\x10\x61sset_max_amount\x18\x04 \x01(\x04\x12*\n\x0e\x61sk_asset_rate\x18\x05 \x01(\x0b\x32\x12.rfqrpc.FixedPoint\x12\x0e\n\x06\x65xpiry\x18\x06 \x01(\x04\x12\x1f\n\x17min_transportable_units\x18\x07 \x01(\x04\"\xb1\x01\n\x15PeerAcceptedSellQuote\x12\x0c\n\x04peer\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x0c\x12\x0c\n\x04scid\x18\x03 \x01(\x04\x12\x14\n\x0c\x61sset_amount\x18\x04 \x01(\x04\x12*\n\x0e\x62id_asset_rate\x18\x05 \x01(\x0b\x32\x12.rfqrpc.FixedPoint\x12\x0e\n\x06\x65xpiry\x18\x06 \x01(\x04\x12\x1e\n\x16min_transportable_msat\x18\x07 \x01(\x04\"Y\n\x14InvalidQuoteResponse\x12\'\n\x06status\x18\x01 \x01(\x0e\x32\x17.rfqrpc.QuoteRespStatus\x12\x0c\n\x04peer\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\x0c\"\\\n\x15RejectedQuoteResponse\x12\x0c\n\x04peer\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x0c\x12\x15\n\rerror_message\x18\x03 \x01(\t\x12\x12\n\nerror_code\x18\x04 \x01(\r\"\x87\x01\n\x1fQueryPeerAcceptedQuotesResponse\x12\x30\n\nbuy_quotes\x18\x01 \x03(\x0b\x32\x1c.rfqrpc.PeerAcceptedBuyQuote\x12\x32\n\x0bsell_quotes\x18\x02 \x03(\x0b\x32\x1d.rfqrpc.PeerAcceptedSellQuote\"\x1f\n\x1dSubscribeRfqEventNtfnsRequest\"m\n\x19PeerAcceptedBuyQuoteEvent\x12\x11\n\ttimestamp\x18\x01 \x01(\x04\x12=\n\x17peer_accepted_buy_quote\x18\x02 \x01(\x0b\x32\x1c.rfqrpc.PeerAcceptedBuyQuote\"p\n\x1aPeerAcceptedSellQuoteEvent\x12\x11\n\ttimestamp\x18\x01 \x01(\x04\x12?\n\x18peer_accepted_sell_quote\x18\x02 \x01(\x0b\x32\x1d.rfqrpc.PeerAcceptedSellQuote\"2\n\x0f\x41\x63\x63\x65ptHtlcEvent\x12\x11\n\ttimestamp\x18\x01 \x01(\x04\x12\x0c\n\x04scid\x18\x02 \x01(\x04\"\xd1\x01\n\x08RfqEvent\x12\x44\n\x17peer_accepted_buy_quote\x18\x01 \x01(\x0b\x32!.rfqrpc.PeerAcceptedBuyQuoteEventH\x00\x12\x46\n\x18peer_accepted_sell_quote\x18\x02 \x01(\x0b\x32\".rfqrpc.PeerAcceptedSellQuoteEventH\x00\x12.\n\x0b\x61\x63\x63\x65pt_htlc\x18\x03 \x01(\x0b\x32\x17.rfqrpc.AcceptHtlcEventH\x00\x42\x07\n\x05\x65vent*Z\n\x0fQuoteRespStatus\x12\x17\n\x13INVALID_ASSET_RATES\x10\x00\x12\x12\n\x0eINVALID_EXPIRY\x10\x01\x12\x1a\n\x16PRICE_ORACLE_QUERY_ERR\x10\x02\x32\xa8\x04\n\x03Rfq\x12U\n\x10\x41\x64\x64\x41ssetBuyOrder\x12\x1f.rfqrpc.AddAssetBuyOrderRequest\x1a .rfqrpc.AddAssetBuyOrderResponse\x12X\n\x11\x41\x64\x64\x41ssetSellOrder\x12 .rfqrpc.AddAssetSellOrderRequest\x1a!.rfqrpc.AddAssetSellOrderResponse\x12X\n\x11\x41\x64\x64\x41ssetSellOffer\x12 .rfqrpc.AddAssetSellOfferRequest\x1a!.rfqrpc.AddAssetSellOfferResponse\x12U\n\x10\x41\x64\x64\x41ssetBuyOffer\x12\x1f.rfqrpc.AddAssetBuyOfferRequest\x1a .rfqrpc.AddAssetBuyOfferResponse\x12j\n\x17QueryPeerAcceptedQuotes\x12&.rfqrpc.QueryPeerAcceptedQuotesRequest\x1a\'.rfqrpc.QueryPeerAcceptedQuotesResponse\x12S\n\x16SubscribeRfqEventNtfns\x12%.rfqrpc.SubscribeRfqEventNtfnsRequest\x1a\x10.rfqrpc.RfqEvent0\x01\x42\x37Z5github.com/lightninglabs/taproot-assets/taprpc/rfqrpcb\x06proto3')

_QUOTERESPSTATUS = DESCRIPTOR.enum_types_by_name['QuoteRespStatus']
QuoteRespStatus = enum_type_wrapper.EnumTypeWrapper(_QUOTERESPSTATUS)
INVALID_ASSET_RATES = 0
INVALID_EXPIRY = 1
PRICE_ORACLE_QUERY_ERR = 2


_ASSETSPECIFIER = DESCRIPTOR.message_types_by_name['AssetSpecifier']
_FIXEDPOINT = DESCRIPTOR.message_types_by_name['FixedPoint']
_ADDASSETBUYORDERREQUEST = DESCRIPTOR.message_types_by_name['AddAssetBuyOrderRequest']
_ADDASSETBUYORDERRESPONSE = DESCRIPTOR.message_types_by_name['AddAssetBuyOrderResponse']
_ADDASSETSELLORDERREQUEST = DESCRIPTOR.message_types_by_name['AddAssetSellOrderRequest']
_ADDASSETSELLORDERRESPONSE = DESCRIPTOR.message_types_by_name['AddAssetSellOrderResponse']
_ADDASSETSELLOFFERREQUEST = DESCRIPTOR.message_types_by_name['AddAssetSellOfferRequest']
_ADDASSETSELLOFFERRESPONSE = DESCRIPTOR.message_types_by_name['AddAssetSellOfferResponse']
_ADDASSETBUYOFFERREQUEST = DESCRIPTOR.message_types_by_name['AddAssetBuyOfferRequest']
_ADDASSETBUYOFFERRESPONSE = DESCRIPTOR.message_types_by_name['AddAssetBuyOfferResponse']
_QUERYPEERACCEPTEDQUOTESREQUEST = DESCRIPTOR.message_types_by_name['QueryPeerAcceptedQuotesRequest']
_PEERACCEPTEDBUYQUOTE = DESCRIPTOR.message_types_by_name['PeerAcceptedBuyQuote']
_PEERACCEPTEDSELLQUOTE = DESCRIPTOR.message_types_by_name['PeerAcceptedSellQuote']
_INVALIDQUOTERESPONSE = DESCRIPTOR.message_types_by_name['InvalidQuoteResponse']
_REJECTEDQUOTERESPONSE = DESCRIPTOR.message_types_by_name['RejectedQuoteResponse']
_QUERYPEERACCEPTEDQUOTESRESPONSE = DESCRIPTOR.message_types_by_name['QueryPeerAcceptedQuotesResponse']
_SUBSCRIBERFQEVENTNTFNSREQUEST = DESCRIPTOR.message_types_by_name['SubscribeRfqEventNtfnsRequest']
_PEERACCEPTEDBUYQUOTEEVENT = DESCRIPTOR.message_types_by_name['PeerAcceptedBuyQuoteEvent']
_PEERACCEPTEDSELLQUOTEEVENT = DESCRIPTOR.message_types_by_name['PeerAcceptedSellQuoteEvent']
_ACCEPTHTLCEVENT = DESCRIPTOR.message_types_by_name['AcceptHtlcEvent']
_RFQEVENT = DESCRIPTOR.message_types_by_name['RfqEvent']
AssetSpecifier = _reflection.GeneratedProtocolMessageType('AssetSpecifier', (_message.Message,), {
  'DESCRIPTOR' : _ASSETSPECIFIER,
  '__module__' : 'lndgrpc.compiled.rfq_pb2'
  # @@protoc_insertion_point(class_scope:rfqrpc.AssetSpecifier)
  })
_sym_db.RegisterMessage(AssetSpecifier)

FixedPoint = _reflection.GeneratedProtocolMessageType('FixedPoint', (_message.Message,), {
  'DESCRIPTOR' : _FIXEDPOINT,
  '__module__' : 'lndgrpc.compiled.rfq_pb2'
  # @@protoc_insertion_point(class_scope:rfqrpc.FixedPoint)
  })
_sym_db.RegisterMessage(FixedPoint)

AddAssetBuyOrderRequest = _reflection.GeneratedProtocolMessageType('AddAssetBuyOrderRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDASSETBUYORDERREQUEST,
  '__module__' : 'lndgrpc.compiled.rfq_pb2'
  # @@protoc_insertion_point(class_scope:rfqrpc.AddAssetBuyOrderRequest)
  })
_sym_db.RegisterMessage(AddAssetBuyOrderRequest)

AddAssetBuyOrderResponse = _reflection.GeneratedProtocolMessageType('AddAssetBuyOrderResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDASSETBUYORDERRESPONSE,
  '__module__' : 'lndgrpc.compiled.rfq_pb2'
  # @@protoc_insertion_point(class_scope:rfqrpc.AddAssetBuyOrderResponse)
  })
_sym_db.RegisterMessage(AddAssetBuyOrderResponse)

AddAssetSellOrderRequest = _reflection.GeneratedProtocolMessageType('AddAssetSellOrderRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDASSETSELLORDERREQUEST,
  '__module__' : 'lndgrpc.compiled.rfq_pb2'
  # @@protoc_insertion_point(class_scope:rfqrpc.AddAssetSellOrderRequest)
  })
_sym_db.RegisterMessage(AddAssetSellOrderRequest)

AddAssetSellOrderResponse = _reflection.GeneratedProtocolMessageType('AddAssetSellOrderResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDASSETSELLORDERRESPONSE,
  '__module__' : 'lndgrpc.compiled.rfq_pb2'
  # @@protoc_insertion_point(class_scope:rfqrpc.AddAssetSellOrderResponse)
  })
_sym_db.RegisterMessage(AddAssetSellOrderResponse)

AddAssetSellOfferRequest = _reflection.GeneratedProtocolMessageType('AddAssetSellOfferRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDASSETSELLOFFERREQUEST,
  '__module__' : 'lndgrpc.compiled.rfq_pb2'
  # @@protoc_insertion_point(class_scope:rfqrpc.AddAssetSellOfferRequest)
  })
_sym_db.RegisterMessage(AddAssetSellOfferRequest)

AddAssetSellOfferResponse = _reflection.GeneratedProtocolMessageType('AddAssetSellOfferResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDASSETSELLOFFERRESPONSE,
  '__module__' : 'lndgrpc.compiled.rfq_pb2'
  # @@protoc_insertion_point(class_scope:rfqrpc.AddAssetSellOfferResponse)
  })
_sym_db.RegisterMessage(AddAssetSellOfferResponse)

AddAssetBuyOfferRequest = _reflection.GeneratedProtocolMessageType('AddAssetBuyOfferRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDASSETBUYOFFERREQUEST,
  '__module__' : 'lndgrpc.compiled.rfq_pb2'
  # @@protoc_insertion_point(class_scope:rfqrpc.AddAssetBuyOfferRequest)
  })
_sym_db.RegisterMessage(AddAssetBuyOfferRequest)

AddAssetBuyOfferResponse = _reflection.GeneratedProtocolMessageType('AddAssetBuyOfferResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDASSETBUYOFFERRESPONSE,
  '__module__' : 'lndgrpc.compiled.rfq_pb2'
  # @@protoc_insertion_point(class_scope:rfqrpc.AddAssetBuyOfferResponse)
  })
_sym_db.RegisterMessage(AddAssetBuyOfferResponse)

QueryPeerAcceptedQuotesRequest = _reflection.GeneratedProtocolMessageType('QueryPeerAcceptedQuotesRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPEERACCEPTEDQUOTESREQUEST,
  '__module__' : 'lndgrpc.compiled.rfq_pb2'
  # @@protoc_insertion_point(class_scope:rfqrpc.QueryPeerAcceptedQuotesRequest)
  })
_sym_db.RegisterMessage(QueryPeerAcceptedQuotesRequest)

PeerAcceptedBuyQuote = _reflection.GeneratedProtocolMessageType('PeerAcceptedBuyQuote', (_message.Message,), {
  'DESCRIPTOR' : _PEERACCEPTEDBUYQUOTE,
  '__module__' : 'lndgrpc.compiled.rfq_pb2'
  # @@protoc_insertion_point(class_scope:rfqrpc.PeerAcceptedBuyQuote)
  })
_sym_db.RegisterMessage(PeerAcceptedBuyQuote)

PeerAcceptedSellQuote = _reflection.GeneratedProtocolMessageType('PeerAcceptedSellQuote', (_message.Message,), {
  'DESCRIPTOR' : _PEERACCEPTEDSELLQUOTE,
  '__module__' : 'lndgrpc.compiled.rfq_pb2'
  # @@protoc_insertion_point(class_scope:rfqrpc.PeerAcceptedSellQuote)
  })
_sym_db.RegisterMessage(PeerAcceptedSellQuote)

InvalidQuoteResponse = _reflection.GeneratedProtocolMessageType('InvalidQuoteResponse', (_message.Message,), {
  'DESCRIPTOR' : _INVALIDQUOTERESPONSE,
  '__module__' : 'lndgrpc.compiled.rfq_pb2'
  # @@protoc_insertion_point(class_scope:rfqrpc.InvalidQuoteResponse)
  })
_sym_db.RegisterMessage(InvalidQuoteResponse)

RejectedQuoteResponse = _reflection.GeneratedProtocolMessageType('RejectedQuoteResponse', (_message.Message,), {
  'DESCRIPTOR' : _REJECTEDQUOTERESPONSE,
  '__module__' : 'lndgrpc.compiled.rfq_pb2'
  # @@protoc_insertion_point(class_scope:rfqrpc.RejectedQuoteResponse)
  })
_sym_db.RegisterMessage(RejectedQuoteResponse)

QueryPeerAcceptedQuotesResponse = _reflection.GeneratedProtocolMessageType('QueryPeerAcceptedQuotesResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPEERACCEPTEDQUOTESRESPONSE,
  '__module__' : 'lndgrpc.compiled.rfq_pb2'
  # @@protoc_insertion_point(class_scope:rfqrpc.QueryPeerAcceptedQuotesResponse)
  })
_sym_db.RegisterMessage(QueryPeerAcceptedQuotesResponse)

SubscribeRfqEventNtfnsRequest = _reflection.GeneratedProtocolMessageType('SubscribeRfqEventNtfnsRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBERFQEVENTNTFNSREQUEST,
  '__module__' : 'lndgrpc.compiled.rfq_pb2'
  # @@protoc_insertion_point(class_scope:rfqrpc.SubscribeRfqEventNtfnsRequest)
  })
_sym_db.RegisterMessage(SubscribeRfqEventNtfnsRequest)

PeerAcceptedBuyQuoteEvent = _reflection.GeneratedProtocolMessageType('PeerAcceptedBuyQuoteEvent', (_message.Message,), {
  'DESCRIPTOR' : _PEERACCEPTEDBUYQUOTEEVENT,
  '__module__' : 'lndgrpc.compiled.rfq_pb2'
  # @@protoc_insertion_point(class_scope:rfqrpc.PeerAcceptedBuyQuoteEvent)
  })
_sym_db.RegisterMessage(PeerAcceptedBuyQuoteEvent)

PeerAcceptedSellQuoteEvent = _reflection.GeneratedProtocolMessageType('PeerAcceptedSellQuoteEvent', (_message.Message,), {
  'DESCRIPTOR' : _PEERACCEPTEDSELLQUOTEEVENT,
  '__module__' : 'lndgrpc.compiled.rfq_pb2'
  # @@protoc_insertion_point(class_scope:rfqrpc.PeerAcceptedSellQuoteEvent)
  })
_sym_db.RegisterMessage(PeerAcceptedSellQuoteEvent)

AcceptHtlcEvent = _reflection.GeneratedProtocolMessageType('AcceptHtlcEvent', (_message.Message,), {
  'DESCRIPTOR' : _ACCEPTHTLCEVENT,
  '__module__' : 'lndgrpc.compiled.rfq_pb2'
  # @@protoc_insertion_point(class_scope:rfqrpc.AcceptHtlcEvent)
  })
_sym_db.RegisterMessage(AcceptHtlcEvent)

RfqEvent = _reflection.GeneratedProtocolMessageType('RfqEvent', (_message.Message,), {
  'DESCRIPTOR' : _RFQEVENT,
  '__module__' : 'lndgrpc.compiled.rfq_pb2'
  # @@protoc_insertion_point(class_scope:rfqrpc.RfqEvent)
  })
_sym_db.RegisterMessage(RfqEvent)

_RFQ = DESCRIPTOR.services_by_name['Rfq']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z5github.com/lightninglabs/taproot-assets/taprpc/rfqrpc'
  _QUOTERESPSTATUS._serialized_start=2510
  _QUOTERESPSTATUS._serialized_end=2600
  _ASSETSPECIFIER._serialized_start=38
  _ASSETSPECIFIER._serialized_end=150
  _FIXEDPOINT._serialized_start=152
  _FIXEDPOINT._serialized_end=200
  _ADDASSETBUYORDERREQUEST._serialized_start=203
  _ADDASSETBUYORDERREQUEST._serialized_end=397
  _ADDASSETBUYORDERRESPONSE._serialized_start=400
  _ADDASSETBUYORDERRESPONSE._serialized_end=606
  _ADDASSETSELLORDERREQUEST._serialized_start=609
  _ADDASSETSELLORDERREQUEST._serialized_end=806
  _ADDASSETSELLORDERRESPONSE._serialized_start=809
  _ADDASSETSELLORDERRESPONSE._serialized_end=1017
  _ADDASSETSELLOFFERREQUEST._serialized_start=1019
  _ADDASSETSELLOFFERREQUEST._serialized_end=1113
  _ADDASSETSELLOFFERRESPONSE._serialized_start=1115
  _ADDASSETSELLOFFERRESPONSE._serialized_end=1142
  _ADDASSETBUYOFFERREQUEST._serialized_start=1144
  _ADDASSETBUYOFFERREQUEST._serialized_end=1237
  _ADDASSETBUYOFFERRESPONSE._serialized_start=1239
  _ADDASSETBUYOFFERRESPONSE._serialized_end=1265
  _QUERYPEERACCEPTEDQUOTESREQUEST._serialized_start=1267
  _QUERYPEERACCEPTEDQUOTESREQUEST._serialized_end=1299
  _PEERACCEPTEDBUYQUOTE._serialized_start=1302
  _PEERACCEPTEDBUYQUOTE._serialized_end=1483
  _PEERACCEPTEDSELLQUOTE._serialized_start=1486
  _PEERACCEPTEDSELLQUOTE._serialized_end=1663
  _INVALIDQUOTERESPONSE._serialized_start=1665
  _INVALIDQUOTERESPONSE._serialized_end=1754
  _REJECTEDQUOTERESPONSE._serialized_start=1756
  _REJECTEDQUOTERESPONSE._serialized_end=1848
  _QUERYPEERACCEPTEDQUOTESRESPONSE._serialized_start=1851
  _QUERYPEERACCEPTEDQUOTESRESPONSE._serialized_end=1986
  _SUBSCRIBERFQEVENTNTFNSREQUEST._serialized_start=1988
  _SUBSCRIBERFQEVENTNTFNSREQUEST._serialized_end=2019
  _PEERACCEPTEDBUYQUOTEEVENT._serialized_start=2021
  _PEERACCEPTEDBUYQUOTEEVENT._serialized_end=2130
  _PEERACCEPTEDSELLQUOTEEVENT._serialized_start=2132
  _PEERACCEPTEDSELLQUOTEEVENT._serialized_end=2244
  _ACCEPTHTLCEVENT._serialized_start=2246
  _ACCEPTHTLCEVENT._serialized_end=2296
  _RFQEVENT._serialized_start=2299
  _RFQEVENT._serialized_end=2508
  _RFQ._serialized_start=2603
  _RFQ._serialized_end=3155
# @@protoc_insertion_point(module_scope)
