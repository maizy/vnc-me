# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.

from tornado.web import asynchronous

from vnc_me.controllers import HttpHandler
from vnc_me.vnc_client import VncClient


class Handler(HttpHandler):

    @asynchronous
    def post(self):
        ok = self.get_argument('ok', False) == 'true'
        if not ok:
            self.redirect('/')
            return
        client = VncClient.get_client('main')
        if not client.running:
            self.redirect('/?error=not_running')
            return

        def _on_stopped(success):
            if success:
                self.redirect('/?aborted=true')
            else:
                self.redirect('/?error=unknown')

        client.stop(_on_stopped)
