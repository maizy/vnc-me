# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.

from tornado.options import define


def define_global_options():
    define('port', type=int, default=8080, help='listen port')
    define('host', type='str', default='0.0.0.0', help='listen host')
