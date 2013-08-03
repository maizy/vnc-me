#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details

import runpy
from os import path
import sys

if __name__ == '__main__':
    src_dir = path.abspath(path.join(path.dirname(__file__), '..', 'src'))
    sys.path.append(src_dir)
    runpy.run_module('vnc_me_tests')
