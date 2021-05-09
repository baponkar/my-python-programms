#sudo pip3 install bottle, to install

from bottle import route, run


@route('/')

def home():
    return "It is not fancy, but it's my home page"


run(host='localhost', port=9999)



