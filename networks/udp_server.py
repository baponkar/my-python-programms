#udp:User datagram protocol,Not reliable for long conversion and not give gurrenty for data delivery

from datetime import datetime
import socket



server_address = ('localhost', 6789)
max_size = 4096


print('Starting server at ',datetime.now())
print('Waiting for client call')

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(server_address)


data, client =  server.recvfrom(max_size)


print('At', datetime.now(),client, 'said',data)
server.sendto(b'Are you talking to me?',client)
server.close()

