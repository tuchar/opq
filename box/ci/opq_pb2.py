# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: opq.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='opq.proto',
  package='opq.proto',
  syntax='proto2',
  serialized_pb=_b('\n\topq.proto\x12\topq.proto\"#\n\x05\x43ycle\x12\x0c\n\x04time\x18\x01 \x02(\x04\x12\x0c\n\x04\x64\x61ta\x18\x02 \x03(\x05\"H\n\x0b\x44\x61taMessage\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0b\n\x03mid\x18\x02 \x01(\x05\x12 \n\x06\x63ycles\x18\x03 \x03(\x0b\x32\x10.opq.proto.Cycle\"]\n\x0eTriggerMessage\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0c\n\x04time\x18\x02 \x02(\x04\x12\x11\n\tfrequency\x18\x03 \x02(\x02\x12\x0b\n\x03rms\x18\x04 \x02(\x02\x12\x11\n\thistogram\x18\x05 \x03(\x05\"\xbf\x01\n\x12RequestDataMessage\x12\x37\n\x04type\x18\x01 \x02(\x0e\x32).opq.proto.RequestDataMessage.RequestType\x12\x0c\n\x04time\x18\x02 \x01(\x04\x12\x0c\n\x04\x62\x61\x63k\x18\x03 \x01(\x05\x12\x0f\n\x07\x66orward\x18\x04 \x01(\x05\x12\x0b\n\x03mid\x18\x05 \x02(\x05\"6\n\x0bRequestType\x12\x08\n\x04PING\x10\x01\x12\x08\n\x04PONG\x10\x02\x12\x08\n\x04READ\x10\x03\x12\t\n\x05\x45RROR\x10\x04')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_REQUESTDATAMESSAGE_REQUESTTYPE = _descriptor.EnumDescriptor(
  name='RequestType',
  full_name='opq.proto.RequestDataMessage.RequestType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PING', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PONG', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READ', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=368,
  serialized_end=422,
)
_sym_db.RegisterEnumDescriptor(_REQUESTDATAMESSAGE_REQUESTTYPE)


_CYCLE = _descriptor.Descriptor(
  name='Cycle',
  full_name='opq.proto.Cycle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='opq.proto.Cycle.time', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='opq.proto.Cycle.data', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=59,
)


_DATAMESSAGE = _descriptor.Descriptor(
  name='DataMessage',
  full_name='opq.proto.DataMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='opq.proto.DataMessage.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mid', full_name='opq.proto.DataMessage.mid', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cycles', full_name='opq.proto.DataMessage.cycles', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=61,
  serialized_end=133,
)


_TRIGGERMESSAGE = _descriptor.Descriptor(
  name='TriggerMessage',
  full_name='opq.proto.TriggerMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='opq.proto.TriggerMessage.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time', full_name='opq.proto.TriggerMessage.time', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='frequency', full_name='opq.proto.TriggerMessage.frequency', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rms', full_name='opq.proto.TriggerMessage.rms', index=3,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='histogram', full_name='opq.proto.TriggerMessage.histogram', index=4,
      number=5, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=135,
  serialized_end=228,
)


_REQUESTDATAMESSAGE = _descriptor.Descriptor(
  name='RequestDataMessage',
  full_name='opq.proto.RequestDataMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='opq.proto.RequestDataMessage.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time', full_name='opq.proto.RequestDataMessage.time', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='back', full_name='opq.proto.RequestDataMessage.back', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='forward', full_name='opq.proto.RequestDataMessage.forward', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mid', full_name='opq.proto.RequestDataMessage.mid', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REQUESTDATAMESSAGE_REQUESTTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=231,
  serialized_end=422,
)

_DATAMESSAGE.fields_by_name['cycles'].message_type = _CYCLE
_REQUESTDATAMESSAGE.fields_by_name['type'].enum_type = _REQUESTDATAMESSAGE_REQUESTTYPE
_REQUESTDATAMESSAGE_REQUESTTYPE.containing_type = _REQUESTDATAMESSAGE
DESCRIPTOR.message_types_by_name['Cycle'] = _CYCLE
DESCRIPTOR.message_types_by_name['DataMessage'] = _DATAMESSAGE
DESCRIPTOR.message_types_by_name['TriggerMessage'] = _TRIGGERMESSAGE
DESCRIPTOR.message_types_by_name['RequestDataMessage'] = _REQUESTDATAMESSAGE

Cycle = _reflection.GeneratedProtocolMessageType('Cycle', (_message.Message,), dict(
  DESCRIPTOR = _CYCLE,
  __module__ = 'opq_pb2'
  # @@protoc_insertion_point(class_scope:opq.proto.Cycle)
  ))
_sym_db.RegisterMessage(Cycle)

DataMessage = _reflection.GeneratedProtocolMessageType('DataMessage', (_message.Message,), dict(
  DESCRIPTOR = _DATAMESSAGE,
  __module__ = 'opq_pb2'
  # @@protoc_insertion_point(class_scope:opq.proto.DataMessage)
  ))
_sym_db.RegisterMessage(DataMessage)

TriggerMessage = _reflection.GeneratedProtocolMessageType('TriggerMessage', (_message.Message,), dict(
  DESCRIPTOR = _TRIGGERMESSAGE,
  __module__ = 'opq_pb2'
  # @@protoc_insertion_point(class_scope:opq.proto.TriggerMessage)
  ))
_sym_db.RegisterMessage(TriggerMessage)

RequestDataMessage = _reflection.GeneratedProtocolMessageType('RequestDataMessage', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTDATAMESSAGE,
  __module__ = 'opq_pb2'
  # @@protoc_insertion_point(class_scope:opq.proto.RequestDataMessage)
  ))
_sym_db.RegisterMessage(RequestDataMessage)


# @@protoc_insertion_point(module_scope)
