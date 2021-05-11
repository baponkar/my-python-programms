import matplotlib.pyplot as plt
import random


#x-values
xVal = []
for i in range(10):
    xVal.append(i)

#y-values
yVal = []
while len(yVal) != 10:
    yVal.append(random.randint(0,100))

print(yVal)


#ploting the points
plt.plot(xVal, yVal)

#naming the x-axis
plt.xlabel("X-Axis")

#naming the y-axis
plt.ylabel("Y-Axis")

#giving title name
plt.title("My First Graph")

#showing the plot
plt.show()

