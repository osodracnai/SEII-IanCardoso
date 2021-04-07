#Ian Cardoso - 11411EMT014

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
s.connect((socket.gethostname(),1234)) 				  

full_msg = ''
while True:
    msg = s.recv(1024) #Le no max 1024 bytes
    if msg len(msg) <= 0: #Verifica se o tamanho da mensagem é menor ou igual a 0. Se sim o laço é quebrado
        break
    full_msg += (msg.decode("utf-8")) #concatena as mensagens

print(full_msg)
