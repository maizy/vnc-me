# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# Based on https://gist.github.com/mitechie/3436363
# See LICENSE.txt for details.

from os import path
import unittest

import pep8

from vnc_me_tests import VNC_ME_ROOT, VNC_ME_TESTS_ROOT, SRC_ROOT, BIN_ROOT

SOURCES = [VNC_ME_ROOT, VNC_ME_TESTS_ROOT, path.join(SRC_ROOT, 'vnc_pass.py'),
           BIN_ROOT]


class StyleTestCase(unittest.TestCase):
    def test_pep8(self):
        pep8style = pep8.StyleGuide(
            show_pep8=False,
            show_source=True,
            repeat=True,
            max_line_length=119,
            statistics=True,
            )
        result = pep8style.check_files(SOURCES)
        if result.total_errors > 0:
            print('\nStatistics:')
            result.print_statistics()
            self.fail('PEP8 styles errors')
