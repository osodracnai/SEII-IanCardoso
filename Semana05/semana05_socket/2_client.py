#Ian Cardoso  11411EMT014

import socket

HEADERSIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))

while  True:
    full_msg = ''
    new_msg = True
    while True:
            msg = s.recv(16) #Define o tamanho maximo de bytes a ser recebido
            if new_msg:
                print(f"comprimento de new_msg: {msg[:HEADERSIZE]}")
                msglen = int(msg[:HEADERSIZE]) #muda o tipo de variável para int do tamanho de HEADERSIZE
                new_msg = False				   #se cair nesse if, obrigatoriamente passará pela condição else na proxima execução

            full_msg += (msg.decode("utf-8"))
            if len(full_msg) - HEADERSIZE ==msglen:
                print("full msg recebido")
                print(full_msg[HEADERSIZE:])
                new_msg = True 				   #se cair nesse if, obrigatoriamente passará outra condição na proxima execução do laço
                full_msg = ''

        print(full_msg)
