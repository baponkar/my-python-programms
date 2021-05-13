'''
This plot showing sell of two things tv and fridge in a hop over a year.
'''

import matplotlib.pyplot as plt


year = [1,2,3,4,5,6,7,8,9,10,11,12]
tv = [ 20,40,60,55,30,20,40,34,65,40,45,60]
fridge = [ 40, 20, 5,20,56,49,33,20,42,13,55,50]


fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

l1 = ax.plot(year, tv, 'ys-')
l2 = ax.plot(year, fridge, 'go--')


ax.legend(labels=('TV', 'Fridge'), loc = 'lower right')

ax.set_title("Selling over the year")
ax.set_xlabel("Month")
ax.set_ylabel('sales')

plt.show()
