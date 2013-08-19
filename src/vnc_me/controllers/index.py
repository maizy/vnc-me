# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.

import socket

from tornado.web import asynchronous

import vnc_me
from vnc_me.controllers import HttpHandler
from vnc_me.vnc_client import VncClient


class Handler(HttpHandler):

    @asynchronous
    def get(self):
        client = VncClient.get_client('main')
        data = {
            'hostname': socket.gethostname(),
            'user_host': self.request.remote_ip,

            'session': {
                'last_host': client.last_host,
                'last_port': client.last_port,
                'duration': 'последние XXX минут (TODO)'  # TODO
            } if client.running else None,
            'info': {
                'version': vnc_me.VERSION,
            }
        }
        self.render('index.html', **data)
