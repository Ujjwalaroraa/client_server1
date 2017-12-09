# client_server1
Name: Ujjwal Arora

Student id :17311879

email id : arorau@tcd.ie

Dependencies: Python 2.7

This repository uses sockets to implement a multiclient server system based on TCP for interaction between the both, with stream connections used to provide a call-back capability from client to server. It contains two files Server (implementation of the chat server) and the Client file(implementation of the clients).

Multiple clients are handled by the sever by the process called mulit threading, It uses multiple threads to connect to multiple clients and with the help of their address, it assigns the ports to the clients and thus establishes the connections. It then adds the clients to the chat rooms. Then the server responds to the requests of the clients based on the connection and thus then responds to the chat requests.

Input and output streams are used in order the communicate with the client/clients by the server. When the connection and the chats are successful then it is server who helps the clients to exit the chat room so that more space is available for the other clients to join the chat room and thus communicate with the server.

Working of server:
1	Socket - Creating a new communication endpoint.
2 Bind - Giving a local address to socket. 
3	Listen - Indicating to accept connections. 
4 Accept- Blocking the caller until a connection request arrives.
5 Create- Creating a new socket. 
6 Wait- Waiting for another connection request. 
7 Close - Finishing the connection.

Working of Client: 
1	Socket - Create a new communication endpoint. 
2	Connect - Actively attempt to establish a connection, with the transport- level address
3 Block the caller until a connection has been set up successfully 
4 Send - Send data over the connection 
5 Receive - Receive data over the connection 
6 Close - Finish the connection
