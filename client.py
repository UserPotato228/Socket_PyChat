import socket, threading 

def recvSoc():
   while True:
      data = clnt_sock.recv(2048)
      print(data.decode("utf-8"))

name = input("name: ")
IP = input("IP: ")
server = (IP, 8080)
clnt_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
clnt_sock.bind("localhost", 0)
clnt_sock.sendto(("["+name+"] теперь в пати").encode("utf-8"), server) 

thr = threading.Thread(target = recvSoc)
thr.start()

while True:
   message = input("message: ")
   sendto(("["+name+"]:"+message).encode("utf-8"), server) 
