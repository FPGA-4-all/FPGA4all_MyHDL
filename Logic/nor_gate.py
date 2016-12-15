# moduel 2_input_or(a, b, y);
# input a, b;
# output y;
# assign y = a | b;
# endmodule
from myhdl import *
def two_input_nor(a, b, c):
    """Two Input or Gate
    a, b    -> Data imputs
    c       -> output
    """
    @always_comb
    def or_logic():
        c.next = intbv(not(a | b))
    return or_logic

def three_input_nor(a, b, c, d):
    """Three Input or Gate
    a, b, c    -> Data imputs
    d       -> output
    """
    @always_comb
    def or_logic():
        d.next = intbv(not(a | b | c))
    return or_logic
