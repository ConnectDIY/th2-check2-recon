# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: th2/message_comparator.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from th2 import infra_pb2 as th2_dot_infra__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='th2/message_comparator.proto',
  package='th2.utility',
  syntax='proto3',
  serialized_options=b'\n/com.exactpro.th2.utility.messagecomparator.grpcP\001',
  serialized_pb=b'\n\x1cth2/message_comparator.proto\x12\x0bth2.utility\x1a\x0fth2/infra.proto\"+\n\x12\x43omparisonSettings\x12\x15\n\rignore_fields\x18\x01 \x03(\t\"\x97\x01\n\x1e\x43ompareFilterVsMessagesRequest\x12\"\n\x06\x66ilter\x18\x01 \x01(\x0b\x32\x12.th2.MessageFilter\x12\x1e\n\x08messages\x18\x02 \x03(\x0b\x32\x0c.th2.Message\x12\x31\n\x08settings\x18\x03 \x01(\x0b\x32\x1f.th2.utility.ComparisonSettings\"h\n\x1f\x43ompareFilterVsMessagesResponse\x12\x45\n\x12\x63omparison_results\x18\x01 \x03(\x0b\x32).th2.utility.CompareFilterVsMessageResult\"{\n\x1c\x43ompareFilterVsMessageResult\x12\"\n\nmessage_id\x18\x01 \x01(\x0b\x32\x0e.th2.MessageID\x12\x37\n\x11\x63omparison_result\x18\x02 \x01(\x0b\x32\x1c.th2.utility.ComparisonEntry\"d\n\x1e\x43ompareMessageVsMessageRequest\x12\x42\n\x10\x63omparison_tasks\x18\x01 \x03(\x0b\x32(.th2.utility.CompareMessageVsMessageTask\"i\n\x1f\x43ompareMessageVsMessageResponse\x12\x46\n\x12\x63omparison_results\x18\x01 \x03(\x0b\x32*.th2.utility.CompareMessageVsMessageResult\"\x8b\x01\n\x1b\x43ompareMessageVsMessageTask\x12\x1b\n\x05\x66irst\x18\x01 \x01(\x0b\x32\x0c.th2.Message\x12\x1c\n\x06second\x18\x02 \x01(\x0b\x32\x0c.th2.Message\x12\x31\n\x08settings\x18\x03 \x01(\x0b\x32\x1f.th2.utility.ComparisonSettings\"\xad\x01\n\x1d\x43ompareMessageVsMessageResult\x12(\n\x10\x66irst_message_id\x18\x01 \x01(\x0b\x32\x0e.th2.MessageID\x12)\n\x11second_message_id\x18\x02 \x01(\x0b\x32\x0e.th2.MessageID\x12\x37\n\x11\x63omparison_result\x18\x03 \x01(\x0b\x32\x1c.th2.utility.ComparisonEntry\"\xd4\x02\n\x0f\x43omparisonEntry\x12.\n\x04type\x18\x01 \x01(\x0e\x32 .th2.utility.ComparisonEntryType\x12\x32\n\x06status\x18\x02 \x01(\x0e\x32\".th2.utility.ComparisonEntryStatus\x12\r\n\x05\x66irst\x18\x03 \x01(\t\x12\x0e\n\x06second\x18\x04 \x01(\t\x12\'\n\toperation\x18\x05 \x01(\x0e\x32\x14.th2.FilterOperation\x12\x0e\n\x06is_key\x18\x06 \x01(\x08\x12\x38\n\x06\x66ields\x18\x07 \x03(\x0b\x32(.th2.utility.ComparisonEntry.FieldsEntry\x1aK\n\x0b\x46ieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.th2.utility.ComparisonEntry:\x02\x38\x01*0\n\x13\x43omparisonEntryType\x12\t\n\x05\x46IELD\x10\x00\x12\x0e\n\nCOLLECTION\x10\x01*7\n\x15\x43omparisonEntryStatus\x12\x06\n\x02NA\x10\x00\x12\n\n\x06PASSED\x10\x01\x12\n\n\x06\x46\x41ILED\x10\x02\x32\x86\x02\n\x18MessageComparatorService\x12t\n\x17\x63ompareFilterVsMessages\x12+.th2.utility.CompareFilterVsMessagesRequest\x1a,.th2.utility.CompareFilterVsMessagesResponse\x12t\n\x17\x63ompareMessageVsMessage\x12+.th2.utility.CompareMessageVsMessageRequest\x1a,.th2.utility.CompareMessageVsMessageResponseB3\n/com.exactpro.th2.utility.messagecomparator.grpcP\x01\x62\x06proto3'
  ,
  dependencies=[th2_dot_infra__pb2.DESCRIPTOR,])

_COMPARISONENTRYTYPE = _descriptor.EnumDescriptor(
  name='ComparisonEntryType',
  full_name='th2.utility.ComparisonEntryType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FIELD', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COLLECTION', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1362,
  serialized_end=1410,
)
_sym_db.RegisterEnumDescriptor(_COMPARISONENTRYTYPE)

ComparisonEntryType = enum_type_wrapper.EnumTypeWrapper(_COMPARISONENTRYTYPE)
_COMPARISONENTRYSTATUS = _descriptor.EnumDescriptor(
  name='ComparisonEntryStatus',
  full_name='th2.utility.ComparisonEntryStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NA', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PASSED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1412,
  serialized_end=1467,
)
_sym_db.RegisterEnumDescriptor(_COMPARISONENTRYSTATUS)

ComparisonEntryStatus = enum_type_wrapper.EnumTypeWrapper(_COMPARISONENTRYSTATUS)
FIELD = 0
COLLECTION = 1
NA = 0
PASSED = 1
FAILED = 2



_COMPARISONSETTINGS = _descriptor.Descriptor(
  name='ComparisonSettings',
  full_name='th2.utility.ComparisonSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ignore_fields', full_name='th2.utility.ComparisonSettings.ignore_fields', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=105,
)


_COMPAREFILTERVSMESSAGESREQUEST = _descriptor.Descriptor(
  name='CompareFilterVsMessagesRequest',
  full_name='th2.utility.CompareFilterVsMessagesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filter', full_name='th2.utility.CompareFilterVsMessagesRequest.filter', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='messages', full_name='th2.utility.CompareFilterVsMessagesRequest.messages', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='settings', full_name='th2.utility.CompareFilterVsMessagesRequest.settings', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=108,
  serialized_end=259,
)


_COMPAREFILTERVSMESSAGESRESPONSE = _descriptor.Descriptor(
  name='CompareFilterVsMessagesResponse',
  full_name='th2.utility.CompareFilterVsMessagesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='comparison_results', full_name='th2.utility.CompareFilterVsMessagesResponse.comparison_results', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=261,
  serialized_end=365,
)


_COMPAREFILTERVSMESSAGERESULT = _descriptor.Descriptor(
  name='CompareFilterVsMessageResult',
  full_name='th2.utility.CompareFilterVsMessageResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message_id', full_name='th2.utility.CompareFilterVsMessageResult.message_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='comparison_result', full_name='th2.utility.CompareFilterVsMessageResult.comparison_result', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=367,
  serialized_end=490,
)


_COMPAREMESSAGEVSMESSAGEREQUEST = _descriptor.Descriptor(
  name='CompareMessageVsMessageRequest',
  full_name='th2.utility.CompareMessageVsMessageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='comparison_tasks', full_name='th2.utility.CompareMessageVsMessageRequest.comparison_tasks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=492,
  serialized_end=592,
)


_COMPAREMESSAGEVSMESSAGERESPONSE = _descriptor.Descriptor(
  name='CompareMessageVsMessageResponse',
  full_name='th2.utility.CompareMessageVsMessageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='comparison_results', full_name='th2.utility.CompareMessageVsMessageResponse.comparison_results', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=594,
  serialized_end=699,
)


_COMPAREMESSAGEVSMESSAGETASK = _descriptor.Descriptor(
  name='CompareMessageVsMessageTask',
  full_name='th2.utility.CompareMessageVsMessageTask',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='first', full_name='th2.utility.CompareMessageVsMessageTask.first', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='second', full_name='th2.utility.CompareMessageVsMessageTask.second', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='settings', full_name='th2.utility.CompareMessageVsMessageTask.settings', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=702,
  serialized_end=841,
)


_COMPAREMESSAGEVSMESSAGERESULT = _descriptor.Descriptor(
  name='CompareMessageVsMessageResult',
  full_name='th2.utility.CompareMessageVsMessageResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='first_message_id', full_name='th2.utility.CompareMessageVsMessageResult.first_message_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='second_message_id', full_name='th2.utility.CompareMessageVsMessageResult.second_message_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='comparison_result', full_name='th2.utility.CompareMessageVsMessageResult.comparison_result', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=844,
  serialized_end=1017,
)


_COMPARISONENTRY_FIELDSENTRY = _descriptor.Descriptor(
  name='FieldsEntry',
  full_name='th2.utility.ComparisonEntry.FieldsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='th2.utility.ComparisonEntry.FieldsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='th2.utility.ComparisonEntry.FieldsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1285,
  serialized_end=1360,
)

_COMPARISONENTRY = _descriptor.Descriptor(
  name='ComparisonEntry',
  full_name='th2.utility.ComparisonEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='th2.utility.ComparisonEntry.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='th2.utility.ComparisonEntry.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='first', full_name='th2.utility.ComparisonEntry.first', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='second', full_name='th2.utility.ComparisonEntry.second', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operation', full_name='th2.utility.ComparisonEntry.operation', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_key', full_name='th2.utility.ComparisonEntry.is_key', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fields', full_name='th2.utility.ComparisonEntry.fields', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_COMPARISONENTRY_FIELDSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1020,
  serialized_end=1360,
)

_COMPAREFILTERVSMESSAGESREQUEST.fields_by_name['filter'].message_type = th2_dot_infra__pb2._MESSAGEFILTER
_COMPAREFILTERVSMESSAGESREQUEST.fields_by_name['messages'].message_type = th2_dot_infra__pb2._MESSAGE
_COMPAREFILTERVSMESSAGESREQUEST.fields_by_name['settings'].message_type = _COMPARISONSETTINGS
_COMPAREFILTERVSMESSAGESRESPONSE.fields_by_name['comparison_results'].message_type = _COMPAREFILTERVSMESSAGERESULT
_COMPAREFILTERVSMESSAGERESULT.fields_by_name['message_id'].message_type = th2_dot_infra__pb2._MESSAGEID
_COMPAREFILTERVSMESSAGERESULT.fields_by_name['comparison_result'].message_type = _COMPARISONENTRY
_COMPAREMESSAGEVSMESSAGEREQUEST.fields_by_name['comparison_tasks'].message_type = _COMPAREMESSAGEVSMESSAGETASK
_COMPAREMESSAGEVSMESSAGERESPONSE.fields_by_name['comparison_results'].message_type = _COMPAREMESSAGEVSMESSAGERESULT
_COMPAREMESSAGEVSMESSAGETASK.fields_by_name['first'].message_type = th2_dot_infra__pb2._MESSAGE
_COMPAREMESSAGEVSMESSAGETASK.fields_by_name['second'].message_type = th2_dot_infra__pb2._MESSAGE
_COMPAREMESSAGEVSMESSAGETASK.fields_by_name['settings'].message_type = _COMPARISONSETTINGS
_COMPAREMESSAGEVSMESSAGERESULT.fields_by_name['first_message_id'].message_type = th2_dot_infra__pb2._MESSAGEID
_COMPAREMESSAGEVSMESSAGERESULT.fields_by_name['second_message_id'].message_type = th2_dot_infra__pb2._MESSAGEID
_COMPAREMESSAGEVSMESSAGERESULT.fields_by_name['comparison_result'].message_type = _COMPARISONENTRY
_COMPARISONENTRY_FIELDSENTRY.fields_by_name['value'].message_type = _COMPARISONENTRY
_COMPARISONENTRY_FIELDSENTRY.containing_type = _COMPARISONENTRY
_COMPARISONENTRY.fields_by_name['type'].enum_type = _COMPARISONENTRYTYPE
_COMPARISONENTRY.fields_by_name['status'].enum_type = _COMPARISONENTRYSTATUS
_COMPARISONENTRY.fields_by_name['operation'].enum_type = th2_dot_infra__pb2._FILTEROPERATION
_COMPARISONENTRY.fields_by_name['fields'].message_type = _COMPARISONENTRY_FIELDSENTRY
DESCRIPTOR.message_types_by_name['ComparisonSettings'] = _COMPARISONSETTINGS
DESCRIPTOR.message_types_by_name['CompareFilterVsMessagesRequest'] = _COMPAREFILTERVSMESSAGESREQUEST
DESCRIPTOR.message_types_by_name['CompareFilterVsMessagesResponse'] = _COMPAREFILTERVSMESSAGESRESPONSE
DESCRIPTOR.message_types_by_name['CompareFilterVsMessageResult'] = _COMPAREFILTERVSMESSAGERESULT
DESCRIPTOR.message_types_by_name['CompareMessageVsMessageRequest'] = _COMPAREMESSAGEVSMESSAGEREQUEST
DESCRIPTOR.message_types_by_name['CompareMessageVsMessageResponse'] = _COMPAREMESSAGEVSMESSAGERESPONSE
DESCRIPTOR.message_types_by_name['CompareMessageVsMessageTask'] = _COMPAREMESSAGEVSMESSAGETASK
DESCRIPTOR.message_types_by_name['CompareMessageVsMessageResult'] = _COMPAREMESSAGEVSMESSAGERESULT
DESCRIPTOR.message_types_by_name['ComparisonEntry'] = _COMPARISONENTRY
DESCRIPTOR.enum_types_by_name['ComparisonEntryType'] = _COMPARISONENTRYTYPE
DESCRIPTOR.enum_types_by_name['ComparisonEntryStatus'] = _COMPARISONENTRYSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ComparisonSettings = _reflection.GeneratedProtocolMessageType('ComparisonSettings', (_message.Message,), {
  'DESCRIPTOR' : _COMPARISONSETTINGS,
  '__module__' : 'th2.message_comparator_pb2'
  # @@protoc_insertion_point(class_scope:th2.utility.ComparisonSettings)
  })
_sym_db.RegisterMessage(ComparisonSettings)

CompareFilterVsMessagesRequest = _reflection.GeneratedProtocolMessageType('CompareFilterVsMessagesRequest', (_message.Message,), {
  'DESCRIPTOR' : _COMPAREFILTERVSMESSAGESREQUEST,
  '__module__' : 'th2.message_comparator_pb2'
  # @@protoc_insertion_point(class_scope:th2.utility.CompareFilterVsMessagesRequest)
  })
_sym_db.RegisterMessage(CompareFilterVsMessagesRequest)

CompareFilterVsMessagesResponse = _reflection.GeneratedProtocolMessageType('CompareFilterVsMessagesResponse', (_message.Message,), {
  'DESCRIPTOR' : _COMPAREFILTERVSMESSAGESRESPONSE,
  '__module__' : 'th2.message_comparator_pb2'
  # @@protoc_insertion_point(class_scope:th2.utility.CompareFilterVsMessagesResponse)
  })
_sym_db.RegisterMessage(CompareFilterVsMessagesResponse)

CompareFilterVsMessageResult = _reflection.GeneratedProtocolMessageType('CompareFilterVsMessageResult', (_message.Message,), {
  'DESCRIPTOR' : _COMPAREFILTERVSMESSAGERESULT,
  '__module__' : 'th2.message_comparator_pb2'
  # @@protoc_insertion_point(class_scope:th2.utility.CompareFilterVsMessageResult)
  })
_sym_db.RegisterMessage(CompareFilterVsMessageResult)

CompareMessageVsMessageRequest = _reflection.GeneratedProtocolMessageType('CompareMessageVsMessageRequest', (_message.Message,), {
  'DESCRIPTOR' : _COMPAREMESSAGEVSMESSAGEREQUEST,
  '__module__' : 'th2.message_comparator_pb2'
  # @@protoc_insertion_point(class_scope:th2.utility.CompareMessageVsMessageRequest)
  })
_sym_db.RegisterMessage(CompareMessageVsMessageRequest)

CompareMessageVsMessageResponse = _reflection.GeneratedProtocolMessageType('CompareMessageVsMessageResponse', (_message.Message,), {
  'DESCRIPTOR' : _COMPAREMESSAGEVSMESSAGERESPONSE,
  '__module__' : 'th2.message_comparator_pb2'
  # @@protoc_insertion_point(class_scope:th2.utility.CompareMessageVsMessageResponse)
  })
_sym_db.RegisterMessage(CompareMessageVsMessageResponse)

CompareMessageVsMessageTask = _reflection.GeneratedProtocolMessageType('CompareMessageVsMessageTask', (_message.Message,), {
  'DESCRIPTOR' : _COMPAREMESSAGEVSMESSAGETASK,
  '__module__' : 'th2.message_comparator_pb2'
  # @@protoc_insertion_point(class_scope:th2.utility.CompareMessageVsMessageTask)
  })
_sym_db.RegisterMessage(CompareMessageVsMessageTask)

CompareMessageVsMessageResult = _reflection.GeneratedProtocolMessageType('CompareMessageVsMessageResult', (_message.Message,), {
  'DESCRIPTOR' : _COMPAREMESSAGEVSMESSAGERESULT,
  '__module__' : 'th2.message_comparator_pb2'
  # @@protoc_insertion_point(class_scope:th2.utility.CompareMessageVsMessageResult)
  })
_sym_db.RegisterMessage(CompareMessageVsMessageResult)

ComparisonEntry = _reflection.GeneratedProtocolMessageType('ComparisonEntry', (_message.Message,), {

  'FieldsEntry' : _reflection.GeneratedProtocolMessageType('FieldsEntry', (_message.Message,), {
    'DESCRIPTOR' : _COMPARISONENTRY_FIELDSENTRY,
    '__module__' : 'th2.message_comparator_pb2'
    # @@protoc_insertion_point(class_scope:th2.utility.ComparisonEntry.FieldsEntry)
    })
  ,
  'DESCRIPTOR' : _COMPARISONENTRY,
  '__module__' : 'th2.message_comparator_pb2'
  # @@protoc_insertion_point(class_scope:th2.utility.ComparisonEntry)
  })
_sym_db.RegisterMessage(ComparisonEntry)
_sym_db.RegisterMessage(ComparisonEntry.FieldsEntry)


DESCRIPTOR._options = None
_COMPARISONENTRY_FIELDSENTRY._options = None

_MESSAGECOMPARATORSERVICE = _descriptor.ServiceDescriptor(
  name='MessageComparatorService',
  full_name='th2.utility.MessageComparatorService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1470,
  serialized_end=1732,
  methods=[
  _descriptor.MethodDescriptor(
    name='compareFilterVsMessages',
    full_name='th2.utility.MessageComparatorService.compareFilterVsMessages',
    index=0,
    containing_service=None,
    input_type=_COMPAREFILTERVSMESSAGESREQUEST,
    output_type=_COMPAREFILTERVSMESSAGESRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='compareMessageVsMessage',
    full_name='th2.utility.MessageComparatorService.compareMessageVsMessage',
    index=1,
    containing_service=None,
    input_type=_COMPAREMESSAGEVSMESSAGEREQUEST,
    output_type=_COMPAREMESSAGEVSMESSAGERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MESSAGECOMPARATORSERVICE)

DESCRIPTOR.services_by_name['MessageComparatorService'] = _MESSAGECOMPARATORSERVICE

# @@protoc_insertion_point(module_scope)
