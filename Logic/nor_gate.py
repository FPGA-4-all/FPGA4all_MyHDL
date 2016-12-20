#nor gate class
from myhdl import *
class nor_gate:
    def __init__(self):
        self.inputs = 2
    def two_input_nor(self, a, b, c):
        """Two Input or Gate
        a, b    -> Data imputs
        c       -> output
        """
        @always_comb
        def or_logic():
            c.next = intbv(not(a | b))
        return or_logic

    def three_input_nor(self, a, b, c, d):
        """Three Input or Gate
        a, b, c    -> Data imputs
        d       -> output
        """
        @always_comb
        def or_logic():
            d.next = intbv(not(a | b | c))
        return or_logic
