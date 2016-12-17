from myhdl import *
from random import randrange
from and_gate import *
import pytest

a, b, c, d = [Signal(intbv(0)) for i in range(4)]
and_inst = three_input_and(a, b, c, d)

def test_and():
    #print "a b c | d"
    for i in range (10):
        a.next, b.next, c.next = randrange(2), randrange(2) ,randrange(2)
        yield delay(10)
        sim = Simulation(and_inst, test_1).run()
        assert d == a.next & b.next & c.next
