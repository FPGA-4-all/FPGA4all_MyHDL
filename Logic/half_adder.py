from xor_gate import *
from and_gate import *
from myhdl import *

def half_adder(a, b, s, c):
    """half adder module
        a, b    -> data input
        s       -> sum
        c       -> overflow
    """
    @always_comb
    def half_add():
        s.next = two_input_xor(a, b)
        c.next = two_input_and(a, b)
    return half_add
