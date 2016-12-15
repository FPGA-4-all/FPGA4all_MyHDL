from myhdl import *
def two_input_nand(a, b, c):
    """Two Input And Gate
    a, b    -> Data imputs
    c       -> output
    """
    @always_comb
    def and_logic():
        c.next = intbv(not(a & b))
    return and_logic


def three_input_nand(a, b, c, d):
    """Two Input And Gate
    a, b, c    -> Data imputs
    d       -> output
    """
    @always_comb
    def and_logic():
        d.next = intbv(not(a & b & c))
    return and_logic
