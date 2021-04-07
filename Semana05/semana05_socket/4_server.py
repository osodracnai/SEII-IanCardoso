#Ian Cardoso - 11411EMT014

import socket
import select


HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234


server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

server_socket.bind((IP, PORT))

server_socket.listen()
sockets_list =[server_socket]   #lista de sockets

clients={}  #tupla de clientes
def receive_message (client_socket):    #função para receber mensagem
    try:
        message_header = client_socket.recv(HEADER_LENGTH)    #recebe o HeaderLength

        if not len(message_header):  #se vier vazio, retorna falso
            return False
        message_length = int(message_header.decode("utf-8").strip())  #coloca headelenght como um inteiro sem espaços em message length
        return {"header:": message_header, "data":client_socket.recv(message_length)}

    except:  #tratamento de exceção: retorna falso
        return False

while   True:  #laço continuo

''' Nesse laço, o client_socket é um parametro para receive message, que irá ler o headere passado e faz a verificação do tamanho dele.
    São lidos endereço e o usuario, indicando se o valor do usuario e são adicionados ou não a socket list para que a conexao seja aceita
falso ou verdadeiro, indicado na linha 41. Caso falso, ele continua, caso contrario, é adicionado ao sockets.list o 
client_socket, indicando assim que a conexao foi aceita e mostrando o usuario e o endereço da conexão estabelecida.
 '''



    read_sockets, _, exception_sockets = select.select(sockets_list,[], sockets_list)   

    for notified_socket in read_sockets:  #percorre a lista de  sockets
        if notified_socket == server_socket: #caso seja igual ao servidor aceita o socket com as informações do cliente
            client_socket, client_address = server_socket.accept()

            user = receive_message(client_socket)   
            if user is False:
                continue

                sockets_list.append(client_socket)
                clients[client_socket] = user
                print(f"Nova conexao aceita de {client_address[0]}:{client_address[1]} usuario:{user['data'].decode('utf-8')}")

            else:
                message = receive_message(notified_socket)

                if message is False:
                    print(f"Conexao encerrada de {clients[notified_socket]['data'].decode('utf-8')}")
                    sockets_list.remove(notified_socket)
                    del clients[notified_socket]
                    continue

                user = clients[notified_socket]
                print(f"Mensagem recebida de {user['data'].decode('utf-8')}: {message['data'].decode('utf-8')}")

                for client_socket in clients:
                    if client_socket != notified_socket:
                        client_socket.send(user['header'] + user['data'] + message['header']+ message['data'])


    for notified_socket in exception_sockets:   #tratamento de exceções: os sockets marcados como exception_sockets são removidos da lista e os clientes deletados
        sockets_list.remove(notified_socket)
        del clients[notified_socket]




