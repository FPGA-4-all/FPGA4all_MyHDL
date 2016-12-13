from myhdl import *
from random import randrange
import and_gate as and_gate

def test_and():

    a, b, c, clk = [Signal(bool(0)) for i in range(4)]

    and_inst = and_gate.two_input_and(a, b, c, clk)

    @always(delay(10))
    def clkgen():
        clk.next = not clk

    @always(clk.negedge)
    def stimulus():
        a = randrange(2)
        b = randrange(3)

    return and_inst, clkgen, stimulus


def simulate(timesteps):
    tb = traceSignals(test_and)
    sim = Simulation(tb)
    sim.run(timesteps)

simulate(2000)
