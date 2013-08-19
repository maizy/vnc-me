# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.

from tornado.web import asynchronous

from vnc_me.controllers import HttpHandler
from vnc_me.vnc_client import VncClient


class Handler(HttpHandler):

    @asynchronous
    def post(self):
        host = self.get_argument('host', None)
        port = self.get_argument('port', None)
        password = self.get_argument('password', '')
        if not host or not port:
            self.redirect('/?error=bad_params')
            return

        client = VncClient.get_client('main')
        if client.running:
            self.redirect('/?error=ever_running')
            return

        def _on_connect(success):
            if success:
                self.redirect('/?connected=true')
            else:
                self.redirect('/?error=unknown')

        client.start(_on_connect, host, port,
                     password.encode('utf-8') if password else None)
