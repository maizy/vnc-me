# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.

from vnc_me.controllers import HttpHandler


class Handler(HttpHandler):

    def post(self):
        host = self.get_argument('host', None)
        port = self.get_argument('port', None)

        if not host or not port:
            self.redirect('/?error=bad_params&connected=true')
            return

        self.redirect('/?hs&connected=false')  # TODO
