import random
import time

#f = open('example.txt', 'wt')

x = 0
while True:
    #x = random.randint(0,100)
    y = random.randint(0,100)
    x += 1
    f = open('example.txt','at')
    s = str(x) + ',' + str(y) + '\n'
    f.write(s)
    f.close()
    time.sleep(0.1)
