import unittest
import pytest

from hyperorm.api import run

class TestRun(unittest.TestCase):

	def setUp(self):
		pass

	def test_boot(self):
		cmds = run.boot();
		assert len(cmds) == 2

if __name__ == '__main__':
    unittest.main()
