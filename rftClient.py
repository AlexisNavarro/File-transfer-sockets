from socket import *

clientSocket = socket(AF_INET, SOCK_STREAM)

#requesting the user to give the destination where our files will be sent to.
ip_addr = input("Please provide a destination IP address to connect: ")
port = input("Please provide a destination port number to connect: ")

server_port = int(port) 
clientSocket.connect((ip_addr, server_port))
clientSocket.send(b"Hello server")
print("YOU HAVE CONNECTED")