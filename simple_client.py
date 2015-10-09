
import socket
import os
import sys

TCP_IP = '127.0.0.1'
TCP_PORT = 50000
BUFFER_SIZE = 1024

if len(sys.argv) > 1:
    num_of_rand = sys.argv[1]
else:
    num_of_rand = 1

MESSAGE =  str.join('', (str(os.getpid()), '|', str(num_of_rand)))

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((TCP_IP,TCP_PORT))
s.send(MESSAGE)
random_hex_string=s.recv(BUFFER_SIZE)
s.close()

print("Random Numbers :",random_hex_string )
