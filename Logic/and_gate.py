#and gate class
from myhdl import *
class and_gate:
    def __init__(self):
        self.inputs = 2
    def two_input_and(self, a, b, c):
        """Two Input And Gate
        a, b    -> Data imputs
        c       -> output
        """
        @always_comb
        def and_logic():
            c.next = a & b
        return and_logic

    def three_input_and(self, a, b, c, d):
        """Two Input And Gate
        a, b, c    -> Data imputs
        d       -> output
        """
        @always_comb
        def and_logic():
            d.next = a & b & c
        return and_logic
