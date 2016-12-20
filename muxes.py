class mux:
    def __init__():
        self.inputs = 2

    def two_input_mux(self, a, b, out, sel):
        """Two Input or Gate
        a, b    -> Data imputs
        out     -> output
        sel     -> select
        """
        @always_comb
        def muxLogic():
            if(sel == 0):
                out.next = a
            else:
                out.next = b

    def three_input_mux(self, a, b, c, out, sel):
        """Two Input or Gate
        a, b    -> Data imputs
        out     -> output
        sel     -> select
        """
        @always_comb
        def muxLogic():
            if(sel == 0):
                out.next = a
            elif(sel  == 1):
                out.next = b
            else:
                out.next = c