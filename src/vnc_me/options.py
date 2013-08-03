# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.

from os import path

from tornado.options import define


def define_global_options():
    project_dir = path.abspath(path.join(path.dirname(__file__), '..', '..'))

    define('port', type=int, default=8080, help='listen port')
    define('host', type=str, default='0.0.0.0', help='listen host')

    define('tmp_dir', type=str, default=path.join(project_dir, 'tmp'))

    define('debug', type=bool, default=False)

    define('config', type=str, default=path.join(project_dir, 'etc', 'vnc-me.conf'))
