#Ian Cardoso  11411EMT014

import socket
import time
import pickle


HEADERSIZE= 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1236))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Conexão com {address} foi estabelecida!")
    d= {1: "hello", 2: "how ya doin??"} #dados a serem serializados
    msg = pickle.dumps(d) #função que transforma 'd' em bytes

    msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg

    clientsocket.send(msg)





