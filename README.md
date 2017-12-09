# client_server1
Name: Ujjwal Arora

Student id :17311879

email id : arorau@tcd.ie

Dependencies: Python 2.7

This repository uses sockets to implement a multiclient server system based on TCP for interaction between the both, with stream connections used to provide a call-back capability from client to server. It contains two files Server (implementation of the chat server) and the Client file(implementation of the clients).

Multiple clients are handled by the sever by the process called mulit threading, It uses multiple threads to connect to multiple clients and with the help of their address, it assigns the ports to the clients and thus establishes the connections. It then adds the clients to the chat rooms. Then the server responds to the requests of the clients based on the connection and thus then responds to the chat requests.

Input and output streams are used in order the communicate with the client/clients by the server. When the connection and the chats are successful then it is server who helps the clients to exit the chat room so that more space is available for the other clients to join the chat room and thus communicate with the server.

Working of server:
 Creating a new communication endpoint.
 Giving a local address to socket. 
 Indicating to accept connections. 
 Blocking the caller until a connection request arrives.
Creating a new socket. 
Waiting for another connection request. Finishing the connection.

Working of Client: 
 Create a new communication endpoint. 
 Actively attempt to establish a connection, with the transport- level address
Block the caller until a connection has been set up successfully  Send data over the connection 
Receive data over the connection 
Finish the connection
