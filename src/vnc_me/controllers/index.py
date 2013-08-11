# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.

import socket

from tornado.web import asynchronous

from vnc_me.controllers import HttpHandler


class Handler(HttpHandler):

    @asynchronous
    def get(self):
        data = {
            'hostname': socket.gethostname(),
            'user_host': self.request.remote_ip,

            'session': {  # TODO,
                'last_host': '127.7.7.7',
                'last_port': '5901',
                'duration': 'последние 10 минут'
            } if self.get_argument('hs', None) is not None else None,
        }
        self.render('index.html', **data)
