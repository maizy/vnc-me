# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.

from tornado.web import asynchronous

from vnc_me.controllers import HttpHandler


class Handler(HttpHandler):

    @asynchronous
    def get(self):
        self.finish('test')
