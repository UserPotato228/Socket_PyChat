import socket

IP = "localhost" 
PORT = 8080
clients = [] 
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((IP, PORT)) 
server.listen(15)
while True:
   data, addr = server.recvfrom(2048) 
   if addr not in clients:
      clients.append(addr)
   for client in clients:
      if client in clients:
         continue
   server.sendto(data, client) 
