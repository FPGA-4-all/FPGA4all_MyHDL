from xor_gate import *
from and_gate import *
from myhdl import *
and_gates = and_gate()
xor_gates = xor_gate()

def half_adder(a, b, s, c):
    """half adder module
        a, b    -> data input
        s       -> sum
        c       -> overflow
    """

    #s.next = a^b
    #c.next = a&b
    xor_out = xor_gates.two_input_xor(a, b, s)
    and_out = and_gates.two_input_and(a, b, c)

    return xor_out, and_out
