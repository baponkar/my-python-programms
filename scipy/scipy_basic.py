import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt



p = sp.poly1d([3,4,5])
print(p)

intp = p.integ(k=6)
print(intp)

dervp = p.deriv()
print(dervp)





