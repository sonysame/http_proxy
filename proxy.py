from socket import *
import sys
import os
import multiprocessing
import time
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
   client_connection.settimeout(30)
   while True:
      try:
        request=client_connection.recv(1024)
    	#print(request)
      	try:
        	Request_HOST=request[request.index("Host"):]
        	HOST=Request_HOST[len("Host: "):Request_HOST.index("\r\n")]	
        	serverName=""
        	serverPort=80
        	serverName=HOST
        #print(serverName, serverPort)
        
        	clientSocket=socket.socket(AF_INET,SOCK_STREAM)
        	clientSocket.connect((serverName,serverPort))
        	clientSocket.send(request)
        	data=clientSocket.recv(6000)
        #print(data)
        	client_connection.send(data)
        except:
          f.write(request)
        	
      except:
        print("TIMEOUT")
        client_connection.close()
        break
 
if __name__=='__main__':
   
   #procs=[]
   f=open("output.txt",'w')

   PORT=int(sys.argv[1])
   
   listen_socket=open_server(PORT)
   
   connection_list=[]
   
   while True:
      
    
      client_connection, client_address=listen_socket.accept()
      t=threading.Thread(target=connection, args=(client_connection,client_address,PORT))
      t.daemon=True
      connection_list.append(t)
      t.start()
    

     
   for i in connection_list:
      i.join()
      print("-----------DONE------------")
   f.close()
      
