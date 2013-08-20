# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.

import logging
try:
    from subprocess import DEVNULL
except ImportError:
    from os import devnull as _devnull
    DEVNULL = open(_devnull, 'wb')
from os import path, unlink
import time
import random
import datetime

import vnc_pass
from tornado.options import options
from tornado.process import Subprocess
from tornado.ioloop import IOLoop

_static_clients = {}

log = logging.getLogger('vnc_me.vnc_client')


class VncClient(object):

    @classmethod
    def get_client(cls, name):
        if name not in _static_clients:
            _static_clients[name] = cls(name)
        return _static_clients[name]

    def __init__(self, name):
        self._name = name
        self.proc = None
        self.running = False
        self.last_host = None
        self.last_port = None
        self.last_passfile = None
        self.start_time = None
        self.log = log
        self.bin = options.vnc_bin

    @property
    def name(self):
        return self._name

    def get_pid(self):
        if not self.running:
            return None
        return self.proc.proc.pid

    def start(self, callback, host, port, password=None):
        if self.running:
            IOLoop.instance().add_callback(callback, False)
        self.running = True
        self.start_time = datetime.datetime.now()
        self.log.info('Vnc client "{name}" started for {port}::{host}, password: {password}'
                      .format(name=self.name, port=port, host=host,
                              password='*' * len(password) if password is not None else '<no pass>'))
        self.last_host = host
        self.last_port = port
        self._start_proc(callback, host, port,
                         self._create_passfile(password) if password is not None else None)

    def stop(self, callback):
        if not self.running:
            IOLoop.instance().add_callback(callback, False)
        self.running = False
        self.start_time = None
        self.log.info('Vnc client "{name}" stopped'.format(name=self.name))
        self._stop_proc(callback)

    def _create_passfile(self, password):
        password = password.encode('utf-8') if not isinstance(password, bytes) else password
        file_name = '{}-{}.passwd'.format(str(time.time()).replace('.', '-'),
                                          random.randint(10000, 99999))
        passfile_path = path.join(options.tmp_dir, file_name)
        with open(passfile_path, 'wb') as f:
            f.write(vnc_pass.encode_password(password))
        self.last_passfile = passfile_path
        return passfile_path

    def _start_proc(self, callback, host, port, pass_file=None):
        args = [options.vnc_bin, '-viewonly', '-fullscreen', '-x11cursor']
        if pass_file is not None:
            args.extend(['-passwd', pass_file])
        args.append('{}::{}'.format(host, port))
        self.log.debug('Vnc client opts: {!r}'.format(args))
        self.proc = Subprocess(args=args, stdout=DEVNULL, stderr=DEVNULL)
        IOLoop.instance().add_callback(callback, True)

    def _stop_proc(self, callback):

        def _cb(ret_code):
            callback(True)

        self.proc.set_exit_callback(_cb)
        if self.last_passfile:
            try:
                unlink(self.last_passfile)
            except IOError:
                pass
        try:
            self.proc.proc.terminate()
        except OSError as e:
            self.log.warning('Failed to kill subprocess: {}'.format(e)),
