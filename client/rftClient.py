from socket import *


def ret_file(clientSocket, file_name):
    file_recv = open(file_name,"wb")

    line = clientSocket.recv(1000)
    #print(line)
    if line == b"file not found":
       print(line)
    else:
        while line:
            file_recv.write(line)
            line = clientSocket.recv(1000)


        print("rcv successful")

def main():
    clientSocket = socket(AF_INET, SOCK_STREAM)

    #requesting the user to give the destination where our files will be sent to.
    ip_addr = input("Please provide a destination IP address to connect: ")
    port = input("Please provide a destination port number to connect: ")

    server_port = int(port) 
    clientSocket.connect((ip_addr, server_port))
  
    print("YOU HAVE CONNECTED")

    request_file = input("please type the file name you want to retrieve using RETR at the start: ")

    send_req = request_file.encode()
    clientSocket.send(send_req)

    file_name = request_file[4:]
   


    ret_file(clientSocket,file_name)


if __name__ == '__main__':
    main()