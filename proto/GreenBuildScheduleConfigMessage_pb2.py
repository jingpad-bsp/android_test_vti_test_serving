# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GreenBuildScheduleConfigMessage.proto

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
  name='GreenBuildScheduleConfigMessage.proto',
  package='android.test.lab',
  syntax='proto2',
  serialized_pb=_b('\n%GreenBuildScheduleConfigMessage.proto\x12\x10\x61ndroid.test.lab\"\xfa\x01\n\x1fGreenBuildScheduleConfigMessage\x12\x0c\n\x04name\x18\x01 \x01(\x0c\x12\x10\n\x08schedule\x18\x02 \x01(\x0c\x12\x10\n\x08priority\x18\x03 \x01(\x0c\x12\x12\n\ngsi_branch\x18\x0b \x01(\x0c\x12\x1a\n\x12gsi_pab_account_id\x18\x0c \x01(\x0c\x12\x13\n\x0btest_branch\x18\x15 \x01(\x0c\x12\x1b\n\x13test_pab_account_id\x18\x16 \x01(\x0c\x12\x43\n\x04test\x18\x1f \x03(\x0b\x32\x35.android.test.lab.GreenBuildTestScheduleConfigMessage\"\xd2\x01\n#GreenBuildTestScheduleConfigMessage\x12\x11\n\ttest_name\x18\x01 \x01(\x0c\x12\x19\n\x11test_build_target\x18\x0b \x01(\x0c\x12\x15\n\rdevice_branch\x18\x15 \x01(\x0c\x12\x1d\n\x15\x64\x65vice_pab_account_id\x18\x16 \x01(\x0c\x12G\n\x06\x64\x65vice\x18\x1f \x03(\x0b\x32\x37.android.test.lab.GreenBuildDeviceScheduleConfigMessage\"\xb4\x01\n%GreenBuildDeviceScheduleConfigMessage\x12\x0e\n\x06\x64\x65vice\x18\x01 \x01(\x0c\x12\x0e\n\x06shards\x18\x0b \x01(\x05\x12\x15\n\rdevice_branch\x18\x15 \x01(\x0c\x12\x1b\n\x13\x64\x65vice_build_target\x18\x16 \x01(\x0c\x12\x1d\n\x15\x64\x65vice_pab_account_id\x18\x17 \x01(\x0c\x12\x18\n\x10gsi_build_target\x18\x1f \x01(\x0c')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GREENBUILDSCHEDULECONFIGMESSAGE = _descriptor.Descriptor(
  name='GreenBuildScheduleConfigMessage',
  full_name='android.test.lab.GreenBuildScheduleConfigMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='android.test.lab.GreenBuildScheduleConfigMessage.name', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='schedule', full_name='android.test.lab.GreenBuildScheduleConfigMessage.schedule', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='priority', full_name='android.test.lab.GreenBuildScheduleConfigMessage.priority', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gsi_branch', full_name='android.test.lab.GreenBuildScheduleConfigMessage.gsi_branch', index=3,
      number=11, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gsi_pab_account_id', full_name='android.test.lab.GreenBuildScheduleConfigMessage.gsi_pab_account_id', index=4,
      number=12, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='test_branch', full_name='android.test.lab.GreenBuildScheduleConfigMessage.test_branch', index=5,
      number=21, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='test_pab_account_id', full_name='android.test.lab.GreenBuildScheduleConfigMessage.test_pab_account_id', index=6,
      number=22, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='test', full_name='android.test.lab.GreenBuildScheduleConfigMessage.test', index=7,
      number=31, type=11, cpp_type=10, label=3,
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
  serialized_start=60,
  serialized_end=310,
)


_GREENBUILDTESTSCHEDULECONFIGMESSAGE = _descriptor.Descriptor(
  name='GreenBuildTestScheduleConfigMessage',
  full_name='android.test.lab.GreenBuildTestScheduleConfigMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='test_name', full_name='android.test.lab.GreenBuildTestScheduleConfigMessage.test_name', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='test_build_target', full_name='android.test.lab.GreenBuildTestScheduleConfigMessage.test_build_target', index=1,
      number=11, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_branch', full_name='android.test.lab.GreenBuildTestScheduleConfigMessage.device_branch', index=2,
      number=21, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_pab_account_id', full_name='android.test.lab.GreenBuildTestScheduleConfigMessage.device_pab_account_id', index=3,
      number=22, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device', full_name='android.test.lab.GreenBuildTestScheduleConfigMessage.device', index=4,
      number=31, type=11, cpp_type=10, label=3,
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
  serialized_start=313,
  serialized_end=523,
)


_GREENBUILDDEVICESCHEDULECONFIGMESSAGE = _descriptor.Descriptor(
  name='GreenBuildDeviceScheduleConfigMessage',
  full_name='android.test.lab.GreenBuildDeviceScheduleConfigMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device', full_name='android.test.lab.GreenBuildDeviceScheduleConfigMessage.device', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shards', full_name='android.test.lab.GreenBuildDeviceScheduleConfigMessage.shards', index=1,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_branch', full_name='android.test.lab.GreenBuildDeviceScheduleConfigMessage.device_branch', index=2,
      number=21, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_build_target', full_name='android.test.lab.GreenBuildDeviceScheduleConfigMessage.device_build_target', index=3,
      number=22, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_pab_account_id', full_name='android.test.lab.GreenBuildDeviceScheduleConfigMessage.device_pab_account_id', index=4,
      number=23, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gsi_build_target', full_name='android.test.lab.GreenBuildDeviceScheduleConfigMessage.gsi_build_target', index=5,
      number=31, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=526,
  serialized_end=706,
)

_GREENBUILDSCHEDULECONFIGMESSAGE.fields_by_name['test'].message_type = _GREENBUILDTESTSCHEDULECONFIGMESSAGE
_GREENBUILDTESTSCHEDULECONFIGMESSAGE.fields_by_name['device'].message_type = _GREENBUILDDEVICESCHEDULECONFIGMESSAGE
DESCRIPTOR.message_types_by_name['GreenBuildScheduleConfigMessage'] = _GREENBUILDSCHEDULECONFIGMESSAGE
DESCRIPTOR.message_types_by_name['GreenBuildTestScheduleConfigMessage'] = _GREENBUILDTESTSCHEDULECONFIGMESSAGE
DESCRIPTOR.message_types_by_name['GreenBuildDeviceScheduleConfigMessage'] = _GREENBUILDDEVICESCHEDULECONFIGMESSAGE

GreenBuildScheduleConfigMessage = _reflection.GeneratedProtocolMessageType('GreenBuildScheduleConfigMessage', (_message.Message,), dict(
  DESCRIPTOR = _GREENBUILDSCHEDULECONFIGMESSAGE,
  __module__ = 'GreenBuildScheduleConfigMessage_pb2'
  # @@protoc_insertion_point(class_scope:android.test.lab.GreenBuildScheduleConfigMessage)
  ))
_sym_db.RegisterMessage(GreenBuildScheduleConfigMessage)

GreenBuildTestScheduleConfigMessage = _reflection.GeneratedProtocolMessageType('GreenBuildTestScheduleConfigMessage', (_message.Message,), dict(
  DESCRIPTOR = _GREENBUILDTESTSCHEDULECONFIGMESSAGE,
  __module__ = 'GreenBuildScheduleConfigMessage_pb2'
  # @@protoc_insertion_point(class_scope:android.test.lab.GreenBuildTestScheduleConfigMessage)
  ))
_sym_db.RegisterMessage(GreenBuildTestScheduleConfigMessage)

GreenBuildDeviceScheduleConfigMessage = _reflection.GeneratedProtocolMessageType('GreenBuildDeviceScheduleConfigMessage', (_message.Message,), dict(
  DESCRIPTOR = _GREENBUILDDEVICESCHEDULECONFIGMESSAGE,
  __module__ = 'GreenBuildScheduleConfigMessage_pb2'
  # @@protoc_insertion_point(class_scope:android.test.lab.GreenBuildDeviceScheduleConfigMessage)
  ))
_sym_db.RegisterMessage(GreenBuildDeviceScheduleConfigMessage)


# @@protoc_insertion_point(module_scope)
