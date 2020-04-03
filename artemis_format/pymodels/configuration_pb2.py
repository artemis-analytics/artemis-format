# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: configuration.proto
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
  name='configuration.proto',
  package='cronus',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13\x63onfiguration.proto\x12\x06\x63ronus\"0\n\nProperties\x12\"\n\x08property\x18\x01 \x03(\x0b\x32\x10.cronus.Property\"5\n\x08Property\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\"]\n\x06Module\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06module\x18\x02 \x01(\t\x12\r\n\x05klass\x18\x03 \x01(\t\x12&\n\nproperties\x18\x04 \x01(\x0b\x32\x12.cronus.Properties\"0\n\x0eGeneratorInput\x12\x1e\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x0e.cronus.Module\"5\n\tAtomInput\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04repo\x18\x02 \x01(\t\x12\x0c\n\x04glob\x18\x03 \x01(\t\"S\n\x05Input\x12)\n\tgenerator\x18\x01 \x01(\x0b\x32\x16.cronus.GeneratorInput\x12\x1f\n\x04\x61tom\x18\x02 \x01(\x0b\x32\x11.cronus.AtomInput\"+\n\x07Sampler\x12\x0f\n\x07ndatums\x18\x01 \x01(\x05\x12\x0f\n\x07nchunks\x18\x02 \x01(\x05\"\x98\x02\n\rConfiguration\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12/\n\x05tools\x18\x03 \x03(\x0b\x32 .cronus.Configuration.ToolsEntry\x12\x1d\n\x05\x61lgos\x18\x04 \x03(\x0b\x32\x0e.cronus.Module\x12\x1d\n\x15max_malloc_size_bytes\x18\x05 \x01(\x04\x12 \n\x07sampler\x18\x06 \x01(\x0b\x32\x0f.cronus.Sampler\x12\x1c\n\x05input\x18\x07 \x01(\x0b\x32\r.cronus.Input\x1a<\n\nToolsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1d\n\x05value\x18\x02 \x01(\x0b\x32\x0e.cronus.Module:\x02\x38\x01\x62\x06proto3')
)




_PROPERTIES = _descriptor.Descriptor(
  name='Properties',
  full_name='cronus.Properties',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='property', full_name='cronus.Properties.property', index=0,
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
  serialized_start=31,
  serialized_end=79,
)


_PROPERTY = _descriptor.Descriptor(
  name='Property',
  full_name='cronus.Property',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cronus.Property.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='cronus.Property.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='cronus.Property.value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=81,
  serialized_end=134,
)


_MODULE = _descriptor.Descriptor(
  name='Module',
  full_name='cronus.Module',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cronus.Module.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='module', full_name='cronus.Module.module', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='klass', full_name='cronus.Module.klass', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='properties', full_name='cronus.Module.properties', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=136,
  serialized_end=229,
)


_GENERATORINPUT = _descriptor.Descriptor(
  name='GeneratorInput',
  full_name='cronus.GeneratorInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='config', full_name='cronus.GeneratorInput.config', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=231,
  serialized_end=279,
)


_ATOMINPUT = _descriptor.Descriptor(
  name='AtomInput',
  full_name='cronus.AtomInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cronus.AtomInput.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repo', full_name='cronus.AtomInput.repo', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='glob', full_name='cronus.AtomInput.glob', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=281,
  serialized_end=334,
)


_INPUT = _descriptor.Descriptor(
  name='Input',
  full_name='cronus.Input',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='generator', full_name='cronus.Input.generator', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='atom', full_name='cronus.Input.atom', index=1,
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
  serialized_start=336,
  serialized_end=419,
)


_SAMPLER = _descriptor.Descriptor(
  name='Sampler',
  full_name='cronus.Sampler',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ndatums', full_name='cronus.Sampler.ndatums', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nchunks', full_name='cronus.Sampler.nchunks', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=421,
  serialized_end=464,
)


_CONFIGURATION_TOOLSENTRY = _descriptor.Descriptor(
  name='ToolsEntry',
  full_name='cronus.Configuration.ToolsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='cronus.Configuration.ToolsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='cronus.Configuration.ToolsEntry.value', index=1,
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
  serialized_start=687,
  serialized_end=747,
)

_CONFIGURATION = _descriptor.Descriptor(
  name='Configuration',
  full_name='cronus.Configuration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cronus.Configuration.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='cronus.Configuration.uuid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tools', full_name='cronus.Configuration.tools', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='algos', full_name='cronus.Configuration.algos', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_malloc_size_bytes', full_name='cronus.Configuration.max_malloc_size_bytes', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sampler', full_name='cronus.Configuration.sampler', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='input', full_name='cronus.Configuration.input', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CONFIGURATION_TOOLSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=467,
  serialized_end=747,
)

_PROPERTIES.fields_by_name['property'].message_type = _PROPERTY
_MODULE.fields_by_name['properties'].message_type = _PROPERTIES
_GENERATORINPUT.fields_by_name['config'].message_type = _MODULE
_INPUT.fields_by_name['generator'].message_type = _GENERATORINPUT
_INPUT.fields_by_name['atom'].message_type = _ATOMINPUT
_CONFIGURATION_TOOLSENTRY.fields_by_name['value'].message_type = _MODULE
_CONFIGURATION_TOOLSENTRY.containing_type = _CONFIGURATION
_CONFIGURATION.fields_by_name['tools'].message_type = _CONFIGURATION_TOOLSENTRY
_CONFIGURATION.fields_by_name['algos'].message_type = _MODULE
_CONFIGURATION.fields_by_name['sampler'].message_type = _SAMPLER
_CONFIGURATION.fields_by_name['input'].message_type = _INPUT
DESCRIPTOR.message_types_by_name['Properties'] = _PROPERTIES
DESCRIPTOR.message_types_by_name['Property'] = _PROPERTY
DESCRIPTOR.message_types_by_name['Module'] = _MODULE
DESCRIPTOR.message_types_by_name['GeneratorInput'] = _GENERATORINPUT
DESCRIPTOR.message_types_by_name['AtomInput'] = _ATOMINPUT
DESCRIPTOR.message_types_by_name['Input'] = _INPUT
DESCRIPTOR.message_types_by_name['Sampler'] = _SAMPLER
DESCRIPTOR.message_types_by_name['Configuration'] = _CONFIGURATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Properties = _reflection.GeneratedProtocolMessageType('Properties', (_message.Message,), {
  'DESCRIPTOR' : _PROPERTIES,
  '__module__' : 'configuration_pb2'
  # @@protoc_insertion_point(class_scope:cronus.Properties)
  })
_sym_db.RegisterMessage(Properties)

Property = _reflection.GeneratedProtocolMessageType('Property', (_message.Message,), {
  'DESCRIPTOR' : _PROPERTY,
  '__module__' : 'configuration_pb2'
  # @@protoc_insertion_point(class_scope:cronus.Property)
  })
_sym_db.RegisterMessage(Property)

Module = _reflection.GeneratedProtocolMessageType('Module', (_message.Message,), {
  'DESCRIPTOR' : _MODULE,
  '__module__' : 'configuration_pb2'
  # @@protoc_insertion_point(class_scope:cronus.Module)
  })
_sym_db.RegisterMessage(Module)

GeneratorInput = _reflection.GeneratedProtocolMessageType('GeneratorInput', (_message.Message,), {
  'DESCRIPTOR' : _GENERATORINPUT,
  '__module__' : 'configuration_pb2'
  # @@protoc_insertion_point(class_scope:cronus.GeneratorInput)
  })
_sym_db.RegisterMessage(GeneratorInput)

AtomInput = _reflection.GeneratedProtocolMessageType('AtomInput', (_message.Message,), {
  'DESCRIPTOR' : _ATOMINPUT,
  '__module__' : 'configuration_pb2'
  # @@protoc_insertion_point(class_scope:cronus.AtomInput)
  })
_sym_db.RegisterMessage(AtomInput)

Input = _reflection.GeneratedProtocolMessageType('Input', (_message.Message,), {
  'DESCRIPTOR' : _INPUT,
  '__module__' : 'configuration_pb2'
  # @@protoc_insertion_point(class_scope:cronus.Input)
  })
_sym_db.RegisterMessage(Input)

Sampler = _reflection.GeneratedProtocolMessageType('Sampler', (_message.Message,), {
  'DESCRIPTOR' : _SAMPLER,
  '__module__' : 'configuration_pb2'
  # @@protoc_insertion_point(class_scope:cronus.Sampler)
  })
_sym_db.RegisterMessage(Sampler)

Configuration = _reflection.GeneratedProtocolMessageType('Configuration', (_message.Message,), {

  'ToolsEntry' : _reflection.GeneratedProtocolMessageType('ToolsEntry', (_message.Message,), {
    'DESCRIPTOR' : _CONFIGURATION_TOOLSENTRY,
    '__module__' : 'configuration_pb2'
    # @@protoc_insertion_point(class_scope:cronus.Configuration.ToolsEntry)
    })
  ,
  'DESCRIPTOR' : _CONFIGURATION,
  '__module__' : 'configuration_pb2'
  # @@protoc_insertion_point(class_scope:cronus.Configuration)
  })
_sym_db.RegisterMessage(Configuration)
_sym_db.RegisterMessage(Configuration.ToolsEntry)


_CONFIGURATION_TOOLSENTRY._options = None
# @@protoc_insertion_point(module_scope)
