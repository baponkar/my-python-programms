#sudo apt install redis-server
#sudo pip3 install redis




import redis

conn = redis.Redis()



topics = ['bapon', 'mathor']

sub = conn.pubsub()
sub.subscribe(topics)


for msg in sub.listen():
    if msg['type'] == 'message':
        cat = msg['channel']
        hat = msg['data']
        print('Subscribe: %s profesion %s' % (cat,hat))


