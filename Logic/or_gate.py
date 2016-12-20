#or gate class
from myhdl import *
class or_gate:
    def __init__(self):
        self.inputs = 2
    def two_input_or(self, a, b, c):
        """Two Input or Gate
        a, b    -> Data imputs
        c       -> output
        """
        @always_comb
        def or_logic():
            c.next = a | b
        return or_logic

    def three_input_or(self, a, b, c, d):
        """Three Input or Gate
        a, b, c    -> Data imputs
        d       -> output
        """
        @always_comb
        def or_logic():
            d.next = a | b | c
        return or_logic
