# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.

from tornado.web import StaticFileHandler
from tornado.options import options

from vnc_me.controllers import index, connect, abort


def get_routes():
    return [
        (r'/', index.Handler),
        (r'/static/(.*)', StaticFileHandler, {'path': options.static_dir}),
        (r'/connect', connect.Handler),
        (r'/abort', abort.Handler),
    ]
