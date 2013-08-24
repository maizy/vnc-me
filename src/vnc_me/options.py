# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.

from os import path

from tornado.options import define


def define_global_options():
    project_dir = path.abspath(path.join(path.dirname(__file__), '..', '..'))

    define('port', type=int, default=8080, help='listen port')
    define('host', type=str, default='0.0.0.0', help='listen host')

    define('vnc_bin', type=str, default='/usr/bin/xtightvncviewer', help='xtightvncviewer binary path')
    define('x_display', type=str, help='X display to use, by default env var "DISPLAY" used')

    define('tmp_dir', type=str, default=path.join(project_dir, 'tmp'))
    define('static_dir', type=str, default=path.join(project_dir, 'src', 'static'))
    define('template_dir', type=str, default=path.join(project_dir, 'src', 'templates'))

    define('debug', type=bool, default=False)

    define('config', type=str, default=path.join(project_dir, 'etc', 'vnc-me.conf'))
