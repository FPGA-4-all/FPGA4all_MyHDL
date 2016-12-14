# moduel 2_input_and(a, b, y);
# input a, b;
# output y;
# assign y = a & b;
# endmodule
from myhdl import *
def two_input_and(a, b, c):
    """Two Input And Gate
    a, b    -> Data imputs
    c       -> output
    """
    @always_comb
    def and_logic():
        c.next = a & b
    return and_logic

def three_input_and(a, b, c, d):
    """Two Input And Gate
    a, b, c    -> Data imputs
    d       -> output
    """
    @always_comb
    def and_logic():
        d.next = a & b & c
    return and_logic
