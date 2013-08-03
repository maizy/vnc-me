# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.

import tornado.web
from tornado.options import options, parse_command_line
from tornado.ioloop import IOLoop

from vnc_me.routes import routes
from vnc_me.options import define_global_options


def build_app():
    app = tornado.web.Application(
        routes,

    )
    app.listen(options.port, options.host)
    return app


def run(args):
    define_global_options()
    parse_command_line(['server'] + args)
    build_app()
    IOLoop.instance().start()
