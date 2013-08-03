#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details

from os import path
import sys


def get_module():
    try:
        import vnc_me.server
    except ImportError:
        src_dir = path.abspath(path.join(path.dirname(__file__), '..', 'src'))
        sys.path.append(src_dir)
        import vnc_me.server
    return vnc_me.server


def run(args):
    module = get_module()
    sys.exit(module.run(args))

if __name__ == '__main__':
    run(sys.argv[1:])
