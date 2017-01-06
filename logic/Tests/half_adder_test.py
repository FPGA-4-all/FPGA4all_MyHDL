from half_adder import *
from myhdl import *
from random import randrange

a, b, c, s = [Signal(intbv(0)) for i in range(4)]

half_adder_inst =   half_adder(a,b,s,c)

def test_half_adder():
    print("a, b, s, c")
    for i in range(10):
        a.next, b.next = randrange(2), randrange(2)
        yield delay(10)
        print "%s, %s, %s, %s" % (a, b, s, c)
test_1 = test_half_adder()
sim = Simulation(half_adder_inst, test_1).run()
