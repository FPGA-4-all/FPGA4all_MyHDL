# moduel 2_input_and(a, b, y);
# input a, b;
# output y;
# assign y = a & b;
# endmodule
from myhdl import *
def two_input_and(a, b, c, clk):
    @always(clk)
    def logic():
        c = a&b
        return logic
def three_input_and(a, b, c, clk):
    return a&b&c
