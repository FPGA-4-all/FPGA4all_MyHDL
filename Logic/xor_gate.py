#xor gate class
from myhdl import *
class xor_gate:
    def __init__(self):
        self.inputs = 2
    def two_input_xor(self, a, b, c):
        """Two Input or Gate
        a, b    -> Data imputs
        c       -> output
        """
        @always_comb
        def xor_logic():
            c.next = a ^ b
        return xor_logic

    def three_input_xor(self, a, b, c, d):
        """Three Input or Gate
        a, b, c    -> Data imputs
        d       -> output
        """
        @always_comb
        def xor_logic():
            d.next = a ^ b ^ c
        return xor_logic
x
