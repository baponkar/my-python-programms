import numpy as np
import matplotlib.pyplot as plt
import math

x = np.arange(0, math.pi*2, 0.05)
y = np.sin(x)


#symbols : - , –, -., , . , , , o , ^ , v , < , > , s , + , x , D , d , 1 , 2 , 3 , 4 , h , H , p ,| , _
#colors : b, g, r, c, m, y, k, w

plt.plot(x, y, 'g4')
plt.xlabel("angle")
plt.ylabel("Sine")
plt.title("Sine Wave")
plt.show()
