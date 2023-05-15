# File Transfer Sockets Programming
The purpose of this repository is to be able to implement file transfer capabilities while using socket programming. This implementation is created to be able to transfer files such as text files, png, and jpgs.

The intented approach is to have a client and server directory in which the client will request for a file by the user inputing the exact file name. That request will then be sent to the server in which the server will have to search if they have an existing file in that name, assuming it does, the server will transfer the files in packets size of 1000 bytes until the entire packet is sent
