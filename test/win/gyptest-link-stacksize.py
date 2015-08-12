#!/usr/bin/env python

# Copyright (c) 2015 Google Inc. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""
Make sure StackReserveSize and StackCommitSize settings are extracted properly.
"""

import TestGyp

import sys

if sys.platform == 'win32':
  test = TestGyp.TestGyp(formats=['msvs', 'ninja'])

  CHDIR = 'linker-flags'
  test.run_gyp('stacksize.gyp', chdir=CHDIR)
  test.build('stacksize.gyp', test.ALL, chdir=CHDIR)

  def GetHeaders(exe):
    return test.run_dumpbin('/headers', test.built_file_path(exe, chdir=CHDIR))
  if '5.01 subsystem version' not in GetHeaders('test_console_xp.exe'):
    test.fail_test()
  if '5.01 subsystem version' not in GetHeaders('test_windows_xp.exe'):
    test.fail_test()

  test.pass_test()
