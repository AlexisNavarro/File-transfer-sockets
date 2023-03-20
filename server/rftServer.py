from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('localhost', 8888))
serverSocket.listen(100)

client, addr = serverSocket.accept()

print("connected to: ", addr)

while True:
    print("receiving request")
    data = client.recv(1024)

    print(data)
    break


client.close()

