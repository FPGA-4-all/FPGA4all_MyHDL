#xor gate class
from myhdl import *
class xnor_gate:
    def __init__(self):
        self.inputs = 2
    def two_input_xnor(self, a, b, c):
        """Two Input xnor Gate
        a, b    -> Data imputs
        c       -> output
        """
        @always_comb
        def xnor_logic():
            c.next = intbv(not(a ^ b))
        return xnor_logic

    def three_input_xnor(self, a, b, c, d):
        """Three Input xnor Gate
        a, b, c    -> Data imputs
        d       -> output
        """
        @always_comb
        def xnor_logic():
            d.next = intbv(not(a ^ b ^ c))
        return xnor_logic
