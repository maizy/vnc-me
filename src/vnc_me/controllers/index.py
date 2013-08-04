# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.

from subprocess import DEVNULL

from tornado.web import asynchronous
from tornado.process import Subprocess
from vnc_me.controllers import HttpHandler

processes = []


class Handler(HttpHandler):

    @asynchronous
    def get(self):
        action = self.get_argument('action', None)
        actions = ['start', 'stop', 'status']
        if not action or action not in actions:
            return self.finish('Actions: {}'.format(', '.join(actions)))
        getattr(self, action)()

    def start(self):
        if len(processes) > 0:
            self.status()
        else:
            proc = Subprocess(args=['/usr/bin/xev'], stdout=DEVNULL, stderr=DEVNULL)
            processes.append(proc)
            self.write('запускаю процесс')
            self.finish()

    def stop(self):

        def cb(exit_code):
            self.write('process closed, exit code {}'.format(exit_code))
            self.finish()

        if len(processes) > 0:
            proc = processes.pop()
            proc.set_exit_callback(cb)
            self.write('останавливаю процесс')
            proc.proc.terminate()
        else:
            self.status()

    def status(self):
        if len(processes) > 0:
            self.write('что-то уже запущено')
        else:
            self.write('ничего не запущено')
        self.finish()
