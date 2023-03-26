from socket import *
import os

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('localhost', 8888))
serverSocket.listen(100)

client, addr = serverSocket.accept()

print("connected to: ", addr)

while True:
    print("receiving request")
    data = client.recv(1024)

    #print(data)

    #converting to a string by deconding the byte message
    message = data.decode()
    print(message[0:4])

    filename = message.split(" ", 1)
    
    #print(filename)
    if("RETR" == message[0:4]):
        print("RETR request received")

        #might need to be used for a different implementation if we don't have the correct path set
        #file_location = "server/"+filename[1]
        #print(file_location)

        #using the os import to be able to check the server directory if a file of that name exists
        if os.path.exists(filename[1]) ==  True:
            print("file is found")
            file = open(filename[1],"rb")
        
            #Checking the file size 
            file_size = os.path.getsize(filename[1])
            print(file_size)

            #send the content of the file to the client
            file_data = file.read(1000)
            
            #sending the packets back to back by reading 1000 bytes and then sending those 1000 bytes 
            while file_data:
                client.send(file_data)
                file_data = file.read(1000)

            print("file has been transferred")
            file.close()
        else:
            client.send(b"file not found")

        break
    


client.close()
serverSocket.close()


