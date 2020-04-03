# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tdigest.proto
# Copyright © Her Majesty the Queen in Right of Canada, as represented
# by the Minister of Statistics Canada, 2019.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tdigest.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rtdigest.proto\"\x87\x01\n\rTDigest_store\x12\x31\n\ndigest_map\x18\x01 \x03(\x0b\x32\x1d.TDigest_store.DigestMapEntry\x1a\x43\n\x0e\x44igestMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12 \n\x05value\x18\x02 \x01(\x0b\x32\x11.TDigest_instance:\x02\x38\x01\"g\n\x10TDigest_instance\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\t\n\x01K\x18\x02 \x01(\x02\x12\r\n\x05\x64\x65lta\x18\x03 \x01(\x02\x12 \n\tcentroids\x18\x04 \x03(\x0b\x32\r.Centroid_map\x12\t\n\x01n\x18\x05 \x01(\x02\"$\n\x0c\x43\x65ntroid_map\x12\t\n\x01\x63\x18\x01 \x01(\x02\x12\t\n\x01m\x18\x02 \x01(\x02\x62\x06proto3')
)




_TDIGEST_STORE_DIGESTMAPENTRY = _descriptor.Descriptor(
  name='DigestMapEntry',
  full_name='TDigest_store.DigestMapEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='TDigest_store.DigestMapEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='TDigest_store.DigestMapEntry.value', index=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=86,
  serialized_end=153,
)

_TDIGEST_STORE = _descriptor.Descriptor(
  name='TDigest_store',
  full_name='TDigest_store',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='digest_map', full_name='TDigest_store.digest_map', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TDIGEST_STORE_DIGESTMAPENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=153,
)


_TDIGEST_INSTANCE = _descriptor.Descriptor(
  name='TDigest_instance',
  full_name='TDigest_instance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='TDigest_instance.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='K', full_name='TDigest_instance.K', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='delta', full_name='TDigest_instance.delta', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='centroids', full_name='TDigest_instance.centroids', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='n', full_name='TDigest_instance.n', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=155,
  serialized_end=258,
)


_CENTROID_MAP = _descriptor.Descriptor(
  name='Centroid_map',
  full_name='Centroid_map',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='c', full_name='Centroid_map.c', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m', full_name='Centroid_map.m', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=260,
  serialized_end=296,
)

_TDIGEST_STORE_DIGESTMAPENTRY.fields_by_name['value'].message_type = _TDIGEST_INSTANCE
_TDIGEST_STORE_DIGESTMAPENTRY.containing_type = _TDIGEST_STORE
_TDIGEST_STORE.fields_by_name['digest_map'].message_type = _TDIGEST_STORE_DIGESTMAPENTRY
_TDIGEST_INSTANCE.fields_by_name['centroids'].message_type = _CENTROID_MAP
DESCRIPTOR.message_types_by_name['TDigest_store'] = _TDIGEST_STORE
DESCRIPTOR.message_types_by_name['TDigest_instance'] = _TDIGEST_INSTANCE
DESCRIPTOR.message_types_by_name['Centroid_map'] = _CENTROID_MAP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TDigest_store = _reflection.GeneratedProtocolMessageType('TDigest_store', (_message.Message,), dict(

  DigestMapEntry = _reflection.GeneratedProtocolMessageType('DigestMapEntry', (_message.Message,), dict(
    DESCRIPTOR = _TDIGEST_STORE_DIGESTMAPENTRY,
    __module__ = 'tdigest_pb2'
    # @@protoc_insertion_point(class_scope:TDigest_store.DigestMapEntry)
    ))
  ,
  DESCRIPTOR = _TDIGEST_STORE,
  __module__ = 'tdigest_pb2'
  # @@protoc_insertion_point(class_scope:TDigest_store)
  ))
_sym_db.RegisterMessage(TDigest_store)
_sym_db.RegisterMessage(TDigest_store.DigestMapEntry)

TDigest_instance = _reflection.GeneratedProtocolMessageType('TDigest_instance', (_message.Message,), dict(
  DESCRIPTOR = _TDIGEST_INSTANCE,
  __module__ = 'tdigest_pb2'
  # @@protoc_insertion_point(class_scope:TDigest_instance)
  ))
_sym_db.RegisterMessage(TDigest_instance)

Centroid_map = _reflection.GeneratedProtocolMessageType('Centroid_map', (_message.Message,), dict(
  DESCRIPTOR = _CENTROID_MAP,
  __module__ = 'tdigest_pb2'
  # @@protoc_insertion_point(class_scope:Centroid_map)
  ))
_sym_db.RegisterMessage(Centroid_map)


_TDIGEST_STORE_DIGESTMAPENTRY._options = None
# @@protoc_insertion_point(module_scope)
