# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: menu.proto
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
  name='menu.proto',
  package='cronus',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\nmenu.proto\x12\x06\x63ronus\"A\n\x04Menu\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12\x1d\n\x06graphs\x18\x03 \x03(\x0b\x32\r.cronus.Graph\"2\n\x05Graph\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1b\n\x05nodes\x18\x02 \x03(\x0b\x32\x0c.cronus.Node\"4\n\x04Node\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07parents\x18\x02 \x03(\t\x12\r\n\x05\x61lgos\x18\x03 \x03(\tb\x06proto3')
)




_MENU = _descriptor.Descriptor(
  name='Menu',
  full_name='cronus.Menu',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cronus.Menu.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='cronus.Menu.uuid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='graphs', full_name='cronus.Menu.graphs', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=22,
  serialized_end=87,
)


_GRAPH = _descriptor.Descriptor(
  name='Graph',
  full_name='cronus.Graph',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cronus.Graph.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nodes', full_name='cronus.Graph.nodes', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=89,
  serialized_end=139,
)


_NODE = _descriptor.Descriptor(
  name='Node',
  full_name='cronus.Node',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cronus.Node.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parents', full_name='cronus.Node.parents', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='algos', full_name='cronus.Node.algos', index=2,
      number=3, type=9, cpp_type=9, label=3,
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
  serialized_start=141,
  serialized_end=193,
)

_MENU.fields_by_name['graphs'].message_type = _GRAPH
_GRAPH.fields_by_name['nodes'].message_type = _NODE
DESCRIPTOR.message_types_by_name['Menu'] = _MENU
DESCRIPTOR.message_types_by_name['Graph'] = _GRAPH
DESCRIPTOR.message_types_by_name['Node'] = _NODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Menu = _reflection.GeneratedProtocolMessageType('Menu', (_message.Message,), dict(
  DESCRIPTOR = _MENU,
  __module__ = 'menu_pb2'
  # @@protoc_insertion_point(class_scope:cronus.Menu)
  ))
_sym_db.RegisterMessage(Menu)

Graph = _reflection.GeneratedProtocolMessageType('Graph', (_message.Message,), dict(
  DESCRIPTOR = _GRAPH,
  __module__ = 'menu_pb2'
  # @@protoc_insertion_point(class_scope:cronus.Graph)
  ))
_sym_db.RegisterMessage(Graph)

Node = _reflection.GeneratedProtocolMessageType('Node', (_message.Message,), dict(
  DESCRIPTOR = _NODE,
  __module__ = 'menu_pb2'
  # @@protoc_insertion_point(class_scope:cronus.Node)
  ))
_sym_db.RegisterMessage(Node)


# @@protoc_insertion_point(module_scope)
