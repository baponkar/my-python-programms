#sudo pip3 install bottle, to install

from bottle import route, run, static_file
import requests


@route('/')

def home():
    return static_file("index.html", root='.')

@route('/echo/<thing>')
def echo(thing):
    return "Say hello to my little friend: %s!" % thing


run(host='localhost', port=9999)



