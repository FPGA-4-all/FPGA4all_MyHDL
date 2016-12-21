from myhdl import *
class counter:
    def __init__():
        self.name = counter
    def up_counter(self, out, enable, clk, reset):
        @always_posedge(clk)
        def counter_logic():
            if(reset):
                out = 0
            elif(enable):
                out = out + 1
    def down_counter(self, out, enable, clk, reset):
        @always_posedge(clk):
        def counter_logic():
            if(reset):
                out = 0
            elif(enable):
                out = out - 1
