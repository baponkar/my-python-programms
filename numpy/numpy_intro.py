import numpy as np

a = np.arange(15) # 1x15 matrics
print(a)

a1 = a.reshape(3, 5) #3x5 matrics
print(a1)
print(type(a1))
print(a1.ndim) #2 dimensional
print(a1.size) #15 quantites inside of a1
print(a1.dtype.name) #inside data type is int64


#creating np array
l = [[ 3, 5, 7 ,8],[9,0,7,3]]
ln = np.array(l)
print(type(ln))

npzero = np.zeros((3,4))
print(npzero)

npone = np.ones((3,4))
print(npone)


import cmath

x = 4
y = 3
z = complex(x,y)
print(z)

x1 = 5
y1 = 7
z1 = complex(x1,y1)
print(z1)

resx = np.linspace(x,x1,10)
resy = np.linspace(y,y1,10)
res = [list(resx),list(resy)]
print(res)

d = []
for m in range(10):
    d.append(resx[m]+resy[m]*1j)

d = np.array(d)
print(type(d))
print(d.dtype.name)
print(d.ndim)
print(d.size)
