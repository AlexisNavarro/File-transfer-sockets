from socket import *

#method where we receive the file from the server
def ret_file(clientSocket, file_name):
    file_recv = open(file_name,"wb")

    #recv first 1000 bytes of the files contents
    line = clientSocket.recv(1000)
    
    if line == b"file not found":
       print(line)
    else:
        #ensure that we get every packet of the file that is being recieved
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

    #create the filename for where the content of the requested file will be stored to
    file_name = request_file[4:]
    ret_file(clientSocket,file_name)


if __name__ == '__main__':
    main()