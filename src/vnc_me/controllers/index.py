# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.

import socket

from tornado.web import asynchronous
from pytils.dt import distance_of_time_in_words

import vnc_me
from vnc_me.controllers import HttpHandler
from vnc_me.vnc_client import VncClient


class Handler(HttpHandler):

    @asynchronous
    def get(self):
        client = VncClient.get_client('main')
        if client.running:
            session = {
                'last_host': client.last_host,
                'last_port': client.last_port,
                'duration': distance_of_time_in_words(client.start_time)
            }
        else:
            session = None
        data = {
            'hostname': socket.gethostname(),
            'user_host': self.request.remote_ip,

            'session': session,
            'info': {
                'version': vnc_me.VERSION,
            }
        }
        self.render('index.html', **data)
