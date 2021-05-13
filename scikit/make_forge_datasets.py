import numpy as np
import scipy as sp
import mglearn
import matplotlib.pyplot as plt


from mglearn.datasets import make_forge
from sklearn.model_selection import train_test_split


X, y = make_forge()

print(X,y)
print(X[:,0])
print(X[:,1])

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])

ax.scatter(X[:,0],y, color='r',marker='^')
ax.scatter(X[:,1],y, color = 'b')

ax.set_xlabel("First Feature")
ax.set_ylabel("Second Feature")
ax.set_title("Make forge data scatter plot")
ax.legend(labels=["1st","2nd"])
plt.ylim(-3,3)
plt.show()


