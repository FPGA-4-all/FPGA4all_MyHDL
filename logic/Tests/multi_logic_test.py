from myhdl import *
import nand_gate, or_gate, xor_gate, and_gate
from random import randrange
a, b, c, d, e, f, g = [Signal(intbv(0)) for i in range(7)]

and_inst    =   and_gate.two_input_and(a, b, c)
or_inst     =   or_gate.two_input_or(d, e, f)
xor_inst    =   xor_gate.two_input_xor(c, f, g)

def test_multi_logic():
    print("a, b, c, d, e, f, g")
    for i in range(10):
        a.next, b.next, d.next, e.next = randrange(2), randrange(2), randrange(2), randrange(2)
        yield delay(10),
        print "%s, %s, %s, %s, %s, %s, %s" % (a, b, c, d, e, f, g)
test_1 = test_multi_logic()
sim = Simulation(and_inst, or_inst, xor_inst, test_1).run()
