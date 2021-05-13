import numpy as np
import scipy as sp


def addsubtract(a,b):
    if a > b:
        return a-b
    else:
        return a+b

vec_addsubtract = sp.vectorize(addsubtract)

res = vec_addsubtract([0,3,6,9],[1,3,5,7])
print(res)
