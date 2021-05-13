import numpy as np




a = np.array([1,5,6,8,0,2,6,5,8,4])
b = np.array([5,2,9,7,6,4,3,2,7,9])

c = a + b
print(type(c))

d = np.random.default_rng(0)
d.random(3)

d = d.random((3,2))
print(d)
