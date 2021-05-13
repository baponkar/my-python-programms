import numpy as np
import random

a = np.linspace(1,5,10)
print(a)
print('shape:',a.shape)
print('size : ',a.size)
print('ndim :',a.ndim)

sa = sorted(a)

b = (a > 2.5)
print(b)

c = (a[a > 2.5])
print(c)
