# Copyright (c) 2015 Google Inc. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
 'targets': [
    {
      'target_name': 'test_default',
      'type': 'executable',
      'sources': ['hello.cc'],
    },
    {
      'target_name': 'test_set_reserved_size',
      'type': 'executable',
      'sources': ['hello.cc'],
      'msvs_settings': {
        'VCLinkerTool': {
          'StackReserveSize': 4096,
        }
      },
    },
    {
      'target_name': 'test_set_commit_size',
      'type': 'executable',
      'sources': ['hello.cc'],
      'msvs_settings': {
        'VCLinkerTool': {
          'StackCommitSize': 4096,
        }
      },
    },
    {
      'target_name': 'test_set_both',
      'type': 'executable',
      'sources': ['hello.cc'],
      'msvs_settings': {
        'VCLinkerTool': {
          'StackReserveSize': 4096,
          'StackCommitSize': 4096,
        }
      },
    },
  ]
}
