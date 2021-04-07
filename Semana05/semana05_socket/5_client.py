#Ian Cardoso - 11411EMT014

import select
import errno 
import socket
import sys


HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234

my_username = input("Username:") #pega a informação do usuario e aloca em my_username
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client_socket.connect((IP, PORT)) 
client_socket.setblocking(False) #impede bloqueamento de dados

username = my_username.encode("utf-8") #tratamento do username
username_header = f"{len(username):<{HEADER_LENGTH}}".encode("utf-8")
client_socket.send(username_header + username) #Manada para o server o username e o header

while   True:
    message = input(f"{my_username} > ") #Usuario insere o nome

    if message: #se a mensagem não vier vazia
        message = message.encode("utf-8")
        message_header = f"{len(message) :<{HEADER_LENGTH} }".encode("utf-8")
        client_socket.send(message_header + message) #envia mensagem ao servidor
    try:
        while True: #Recebendo os objetos
            username_header = client_socket.recv(HEADER_LENGTH)
            if not len(username_header):
                print("Conexão fechada pelo servidor")
                sys.exit()
            username_length = int(username_header.decode("utf-8").strip())
            username = client_socket.recv(username_length).decode("utf-8")

            message_header = client_socket.recv(HEADER_LENGTH)#Recebe o tamanho do header pre definido
            message_length = int(message_header.decode("utf-8").strip())#Transforma em inteiro o header da mensagem
            message = client_socket.recv(message_length).decode("utf-8")#Recebe o tamanho em bytes e volta pra objeto

            print(f"{username} > {message}")

    except IOError as e: #tratamento d erros
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:  #Testa se o erro não é vaizou ou não pertence a biblioteca importada de erro
            sys.exit() #fecha o sistema
        continue

    except Exception as e:
        print('General error', srt(e)) #mostra o erro geral
        sys.exit()
        pass


