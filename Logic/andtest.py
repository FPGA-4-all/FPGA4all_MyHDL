from myhdl import *
from random import randrange
from and_gate import and_gate
import pytest
and_gates = and_gate()

a, b, c, d = [Signal(intbv(0)) for i in range(4)]
and_inst = and_gates.three_input_and(a, b, c, d)

def test_and():
    #print "a b c | d"
    for i in range (10):
        a.next, b.next, c.next = randrange(2), randrange(2) ,randrange(2)
        yield delay(10)
        print "%s, %s, %s, %s" % (a, b, c, d)
test_1 = test_and()
sim = Simulation(and_inst, test_1).run()
