from myhdl import *
def full_adder(a, b, c_in, s, c_out):
    """half adder module
        a, b    -> data input
        s       -> sum
        c       -> overflow
    """
    @always_comb
    def full_add():
        p = a ^y
        s.next = p ^ c_in

        r = p & c_in
        s = x & y
        c_out.next = r | s
    return full_add
