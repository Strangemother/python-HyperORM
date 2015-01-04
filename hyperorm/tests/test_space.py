import unittest
import pytest

from hyperorm import run
from hyperorm import Service
# from hyperorm.models import TestModel

import hyperdex
from hyperdex import admin, client
from hyperdex.client import HyperDexClientException

connect_ip='127.0.0.1'
connect_port=1982

from hyperorm.api.core.models import TestModel
from hyperorm.api.core.spaces import TestSpace

class TestRun(unittest.TestCase):

    def setUp(self):
        self.srv = Service()
        self.space = TestSpace(self.srv)

    def test_model(self):
        space = self.space
        Model = self.space.get_model()
        assert Model == TestModel

    def test_model_arg(self):
        space = self.space
        n = 'one'
        m = space.model(n)
        kn = m.get_key_name()
        assert getattr(m, kn) == n

    def test_model_kwarg(self):
        space = self.space
        n = 'trout'
        cn = space.get_model().__name__
        m = space.model(n, name='wubble', number=3)
        kn = m.get_key_name()
        assert getattr(m, kn) == n
        assert m.name == 'wubble'
        assert m.number == 3
        assert str(m) == "HyperModel: %s('%s')" % (cn, n,)


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
