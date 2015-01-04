import unittest
import pytest

import hyperorm

print 'hyperorm',  hyperorm

from hyperorm import run
from hyperorm import Service
# from hyperorm.models import TestModel

import hyperdex
from hyperdex import admin, client
from hyperdex.client import HyperDexClientException

connect_ip='127.0.0.1'
connect_port=1982


class TestRun(unittest.TestCase):

    def setUp(self):
        self.srv = Service()
        self.a = admin.Admin(connect_ip, connect_port)
        self.c = client.Client(connect_ip, connect_port)

    def test_boot(self):
        cmds = run.boot();
        assert len(cmds) == 2

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
