# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.

from os import path

import tornado.web
from tornado.options import options
from tornado.ioloop import IOLoop

from vnc_me.log import gen_log
from vnc_me.routes import routes
from vnc_me.options import define_global_options


def build_app():
    gen_log.info('Start server at {host}:{port}{debug}'
                 .format(host=options.host, port=options.port,
                         debug=' in debug mode' if options.debug else ''))
    app = tornado.web.Application(
        routes,
        debug=options.debug
    )
    app.listen(options.port, options.host)
    return app


def run(args):
    define_global_options()
    options.parse_command_line(['server'] + args, final=False)
    config_file = path.expanduser(options.config)
    if path.isfile(config_file):
        options.parse_config_file(config_file, final=False)
    options.run_parse_callbacks()
    if path.isfile(config_file):
        gen_log.info('Config loaded from {}'.format(config_file))
    build_app()
    IOLoop.instance().start()
