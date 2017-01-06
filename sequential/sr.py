from __future__ import absolute_import
from ..logic import and_gate
# if __name__ == '__main__':
#     if __package__ is None:
#         import sys
#         from os import path
#         sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
#         from logic.and_gate import *
#         from logic.nor_gate import *
#     else:
#         from ..logic.and_gate import *
#         from ..logic.nor_gate import *

def sr_gate(Q, Qn, G, S, R):
    S1 = 0
    R1 = 0
    SG_and = and_gate.two_input_and(G, S, S1)
    GR_and = and_gate.two_input_and(G, R, R1)
    QnS1_nor = nor_gate.two_input_nor(S1, Q, Qn)
    QR1_nor = nor_gate.two_input_nor(R1, Qn, Q)
