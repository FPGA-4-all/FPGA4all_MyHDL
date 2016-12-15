# moduel 2_input_or(a, b, y);
# input a, b;
# output y;
# assign y = a | b;
# endmodule
from myhdl import *
def two_input_xor(a, b, c):
    """Two Input or Gate
    a, b    -> Data imputs
    c       -> output
    """
    @always_comb
    def or_logic():
        c.next = a ^ b
    return or_logic

def three_input_xor(a, b, c, d):
    """Three Input or Gate
    a, b, c    -> Data imputs
    d       -> output
    """
    @always_comb
    def or_logic():
        d.next = a ^ b ^ c
    return or_logic
