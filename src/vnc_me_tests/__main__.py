# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.

import sys

import nose

from vnc_me_tests import VNC_ME_TESTS_ROOT

if __name__ in ('__main__', 'vnc_me_tests.__main__'):
    argv = sys.argv[:]
    argv.append(VNC_ME_TESTS_ROOT)
    nose.run_exit(argv=argv)
