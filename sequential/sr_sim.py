from __future__ import absolute_import
from random import randrange
from myhdl import *
from sr import sr_gate

Q, Qn, G, S, R = [Signal(bool(0)) for i in range(5)]
sr_inst = sr_gate(Q, Qn, G, S, R)

def test_sr_gate():
    for i in range(10):
        S.next, G.next, R.next = randrange(2), randrange(2) ,randrange(2)
        yield delay(10)
        print "%s, %s, %s, %s, %s" % (Q, Qn, G, S, R)
test_1 = test_and()
sim = Simulation(sr_inst, test_1).run()
