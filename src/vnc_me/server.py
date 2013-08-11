# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.

from os import path, environ
import sys

import tornado.web
from tornado.options import options
from tornado.ioloop import IOLoop

from vnc_me.log import gen_log
from vnc_me import routes
from vnc_me.options import define_global_options

BAD_CONFIG = 5


def _set_x_display(options):
    if not options.x_display:
        options.x_display = environ.get('DISPLAY')


def _check_x_display(options):
    if not options.x_display:
        gen_log.fatal('X Display not set.\n'
                      'Specify env var "DISPLAY" or x_display option')
        return False
    return True


def build_app():
    if not _check_x_display(options):
        sys.exit(BAD_CONFIG)

    gen_log.info('Start server at {host}:{port}{debug}'
                 .format(host=options.host, port=options.port,
                         debug=' in debug mode' if options.debug else ''))
    app = tornado.web.Application(
        routes.get_routes(),
        debug=options.debug,
        template_path=options.template_dir
    )
    app.listen(options.port, options.host)
    return app


def run(args):
    define_global_options()
    options.parse_command_line(['server'] + args, final=False)
    config_file = path.expanduser(options.config)
    if path.isfile(config_file):
        options.parse_config_file(config_file, final=False)
    _set_x_display(options)
    options.run_parse_callbacks()
    if path.isfile(config_file):
        gen_log.info('Config loaded from {}'.format(config_file))
    build_app()
    IOLoop.instance().start()
