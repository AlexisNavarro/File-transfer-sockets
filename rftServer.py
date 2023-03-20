from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('localhost', 8888))
serverSocket.listen(100)

client, addr = serverSocket.accept()

print("connected to: ", addr)

client.close()

