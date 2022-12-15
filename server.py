import socket
import os

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("localhost", 9999))
#server.listen()

#client, addr = server.accept()
while True:
    filename = server.recvfrom(1024)[0].decode()
    if len(str(filename)) > 0:
        break
print(filename)
filesize = server.recvfrom(1024)[0].decode()
print(filesize)

file  = open(filename, "wb")

filebytes = b""

done = False

while not done:
    data = server.recvfrom(1024)[0]
    if filebytes[-5:] == b"<END>":
        done = True
        break
    else:
        filebytes += data
    if filebytes[-5:] == b"<END>":
        done = True

file.write(filebytes[:-5])

file.close()
server.close()
