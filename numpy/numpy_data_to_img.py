import numpy as np
import matplotlib.pyplot as plt
import random


data = []
for i in range(4):
    temp = random.randint(0,256)
    data.append(temp)

data = np.array(data)
data = data.reshape(2,2)


print(data)

plt.imshow(data, interpolation = 'nearest')
plt.show()
