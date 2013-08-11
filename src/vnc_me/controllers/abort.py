# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.

from vnc_me.controllers import HttpHandler


class Handler(HttpHandler):

    def post(self):
        ok = self.get_argument('ok', False) == 'true'
        if not ok:
            self.redirect('/?aborted=false')
            return
        self.redirect('/?aborted=true')
