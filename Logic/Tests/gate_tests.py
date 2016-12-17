#=========================================================================
# Gate_tests
#=========================================================================

import pytest
import random

random.seed(0xdeadbead)

from myhdl import *


class TestClass:
    def test_one(self):
        x = "this"
        assert 'h' in x
    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')


#-------------------------------------------------------------------------
# Test Case Table
#-------------------------------------------------------------------------
