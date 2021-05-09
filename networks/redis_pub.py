#sudo apt install redis-server
#sudo pip3 install redis


import redis
import random


conn = redis.Redis()
cats = [ 'bapon', 'bittu','mango','mathor', 'limbush' ]
hats = [ 'teacher','mobile technecian','lawyear','printer','police']

for msg in range(10):
    cat = random.choice(cats)
    hat = random.choice(hats)
    print('Publish : %s profesion is %s ' % (cat,hat))
    conn.publish(cat,hat)


