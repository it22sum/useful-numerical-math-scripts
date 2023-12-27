import numpy as np
import matplotlib.pyplot as plt

# Import from other files:
#from sekanten_verfahren import sekanten_verfahren


# ========================================================
# Idea: use this file to 'play around' and try things out.
# It is supposed to be used as a sort of test environment.
# ========================================================


import struct
def binary(num):
    return ''.join('{:0>8b}'.format(c) for c in struct.pack('!f', num))

print(binary(np.sqrt(3)))