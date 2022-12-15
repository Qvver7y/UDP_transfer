from sys import  argv
import os
import socket

script,filename,remotefile = argv
FILENAME =  filename 
REMFILENAME =  remotefile
HOST = "localhost"
PORT = 9999
SOCADDR = (HOST, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

file = open(filename, "rb")
file_size =  os.path.getsize(FILENAME)


client.sendto(str(REMFILENAME).encode(), SOCADDR)
client.sendto(str(file_size).encode(), SOCADDR)

data = file.read()
if file_size % 1024 == 0:
    N = file_size / 1024
else:
    N = int(file_size / 1024) + 1

for i in range(0,N):    

    client.sendto(data[i*1024: i*1024+1024], SOCADDR)
client.sendto(b"<END>", SOCADDR)


file.close()
client.close()
