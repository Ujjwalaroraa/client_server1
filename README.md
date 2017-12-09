# client_server1
Name: Manik Behl

Student id :17311879

email id : arorau@tcd.ie

Dependencies: Python 2.7

Run the server start.sh [port number]

This repository has the implementation of the centralised Multi-client chat server using Sockets in Python. Chat server is based on the Tcp protocol, designed for stream connections between clients and server, with stream connections used to provide a call-back capability from client to server. This repository contains two files stest (implementation of the chat server) and the client file(implementation of the clients)

Server handles multiple clients using threads. Server connects with the client based on the address and assigns the port to client for transferring messages by including client to the chat room.
Server has the additional feature of authority to add a client in a multiple chat rooms. Also, Server can add multiple clients to single room as well as multiple clients to single room or into multiple rooms.
Server process the client request of client based on the connection and processes the chat request for joining the chat rooms based on the requests from the clients.

Server provides the functionalities of leaving the chat rooms as well.
Server communicates with the single or with multiple client by transferring messages using the input and output streams.
After successful communication server disconnects with the clients which were connected earlier.
Working of server •	Socket - Create a new communication endpoint for a specific transport protocol. • Bind - Attach a local address to the newly created socket. •	Listen - Announce willingness to accept connections. • Accept-

Block caller until a connection request arrives.
Create a new socket with the same properties as the original one and returns it to the caller.
Wait for another connection request on the original socket • Close - Release the connection.
Working of Client: •	Socket - Create a new communication endpoint for a specific transport protocol, but bind is not necessary •	Connect

Actively attempt to establish a connection, with the transport- level address
Block the caller until a connection has been set up successfully • Send - Send some data over the connection • Receive - Receive some data over the connection • Close - Release the connection
