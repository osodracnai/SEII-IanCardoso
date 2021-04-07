#Ian Cardoso  11411EMT014
 
import socket
import time

HEADERSIZE= 10 #Variavel global para o tamanho do header

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1235))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Conexão com {address} foi estabelecida!")

    msg = "Bem vindo ao Servidor!"
    msg = f'{len(msg):<{HEADERSIZE}}' + msg #mostra o tamanho da mensagem (no max até HEADERSIZE)

    clientsocket.send(bytes(msg, "utf-8"))

    while   True:
        time.sleep(3) #suspende durante 3 segundos
        msg = f"O tempo de execução foi: {time.time()}"
        msg = f'{len(msg):<{HEADERSIZE}}' + msg
        clientsocket.send(bytes(msg, "utf-8"))    #envia a msg em bytes




