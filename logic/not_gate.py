#not gate class
from myhdl import *
class not_gate:
    def __init__(self):
        self.inputs = 1
    def one_input_not(self, a, b):
        """one input not gate
        a -> input
        b -. output
        """
        @always_comb
        def not_logic():
            b.next = intbv(not(a))
        return not_logic

        
