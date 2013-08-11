# _*_ coding: utf-8 _*_

import logging
from subprocess import DEVNULL

from tornado.options import options
from tornado.process import Subprocess

_static_clients = {}

log = logging.getLogger('vnc_me.vnc_client')


class VncClient(object):

    @classmethod
    def get_client(cls, name):
        if name not in _static_clients:
            _static_clients[name] = cls()
        return _static_clients[name]

    def __init__(self, name):
        self._name = name
        self.proc = None
        self.runnig = False
        self.last_host = None
        self.last_port = None
        self.last_passfile = None
        self.start_time = None
        self.log = log
        self.bin = options.vnc_bin

    @property
    def name(self):
        return self._name

    def start(self, host, port, password):
        if self.runnig:
            return False
        self.log.info('Vnc client "{name}" started for {port}::{host}, password: {password}'
                      .format(name=self.name, port=port, host=host, password='*' * len(password)))
        self.runnig = True
        self._start_proc(host, port, self._create_passfile(password))
        return True

    def stop(self):
        if not self.runnig:
            return False
        self.log.info('Vnc client "{name}" stopped'.format(name=self.name))
        self._stop_proc()
        self.runnig = False
        return True

    def _create_passfile(self, password):  # TODO
        return None

    def _start_proc(self, host, port, pass_file=None):  # TODO
        # proc = Subprocess(args=['/usr/bin/xev'], stdout=DEVNULL, stderr=DEVNULL)
        pass

    def _stop_proc(self):  # TODO
        # proc = processes.pop()
        # proc.set_exit_callback(cb)
        # proc.proc.terminate()
        pass

    def get_pid(self):  # TODO
        return None
