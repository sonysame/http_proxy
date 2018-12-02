from socket import *
import sys
import os
import threading
from pwn import *


def open_server(port):
   HOST, PORT='', port
   listen_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
   listen_socket.bind((HOST, PORT))
   listen_socket.listen(1)

   print '(Server side PORT %s)'% PORT
   return listen_socket

def connection(conn, addr, port):
   client_connection=conn
   client_address=addr
   PORT=port
   request=client_connection.recv(4096)
   Request_HOST=request[request.index("Host"):]
   HOST=Request_HOST[len("Host: "):Request_HOST.index("\r\n")]	
   serverName=""
   serverPort=80
   serverName=HOST
   print(serverName, serverPort)
   try:
       clientSocket=socket.socket(AF_INET,SOCK_STREAM)
       clientSocket.connect((serverName,serverPort))
       clientSocket.send(request)
       
       while 1:
           data=clientSocket.recv(4096)
           if(len(data)>0):
               client_connection.send(data)
           else:
               break

   except:
    	print("ERROR")

   finally:
    	if(clientSocket):
    		clientSocket.close()
    	if(client_connection):
    		client_connection.close()

 
if __name__=='__main__':
   
  
   PORT=int(sys.argv[1])
   
   listen_socket=open_server(PORT)
   
   connection_list=[]
   try: 
	   while True:
	      
	    
	      client_connection, client_address=listen_socket.accept()
	      t=threading.Thread(target=connection, args=(client_connection,client_address,PORT))
	      t.daemon=True
	      connection_list.append(t)
	      t.start()
	    

	     
	   for i in connection_list:
	      i.join()
	      print("-----------DONE------------")
   except:
       sys.exit(1)

      
