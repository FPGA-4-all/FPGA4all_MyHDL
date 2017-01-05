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
        a, b, c     -> Data imputs
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

    def four_input_mux(self, a, b, c, d, out, sel):
        """Two Input or Gate
        a, b, c, d    -> Data imputs
        out     -> output
        sel     -> select
        """
        @always_comb
        def muxLogic():
            if(sel == 0):
                out.next = a
            elif(sel  == 1):
                out.next = b
            elif(sel == 2):
                out.next = c
            else:
                out.next = d

    def five_input_mux(self, a, b, c, d, e, out, sel):
        @always_comb
        def muxLogic():
            if(sel == 0):
                out.next = a
            elif(sel  == 1):
                out.next = b
            elif(sel == 2):
                out.next = c
            elif(sel == 3):
                out.next = d
            else:
                out.next = e

    def six_input_mux(self, a, b, c, d, e, f, out, sel):
        @always_comb
        def muxLogic():
            if(sel == 0):
                out.next = a
            elif(sel  == 1):
                out.next = b
            elif(sel == 2):
                out.next = c
            elif(sel == 3):
                out.next = d
            elif(sel == 4):
                out.next = e
            else:
                out.next = f

    def seven_input_mux(self, a, b, c, d, e, f, g, out, sel):
        @always_comb
        def muxLogic():
            if(sel == 0):
                out.next = a
            elif(sel  == 1):
                out.next = b
            elif(sel == 2):
                out.next = c
            elif(sel == 3):
                out.next = d
            elif(sel == 4):
                out.next = e
            elif(sel == 5):
                out.next = f
            else:
                out.next = g
