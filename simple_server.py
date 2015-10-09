import socket
import os

from mersenne_twister import MersenneTwister

host = ''
port = 50000
backlog = 5
size = 1024
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)

while 1:
    print("Started Server....")
    print("At port : %s with process id : %s " % (port,os.getpid()))
    client,address = s.accept()
    data = client.recv(size)
    if data:
        params=data.split("|")
        process_id =int(params[0])
        num_of_rand = int(params[1])
        print("Invoking MersenneTwister with process id : %s and number of random number : %s" % (process_id,num_of_rand))
        rand_gen = MersenneTwister(process_id,num_of_rand)
        client.send(rand_gen.rand())
    else:
        print("Incorrect input recieved from client")
        client.send("Unable to generate random number")
