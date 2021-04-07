#Ian Cardoso - 11411EMT014

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Cria um objeto do tipo socket e chama a função socket() levando como parametros o endereço e protocolo a serem requisitados 
s.bind((socket.gethostname(), 1234)) #liga o socket no endereço retornado em gethostname (ip) na porta 1234
s.listen(5) #o servidor se prepara pra receber uma fila de até 5 conexoes 

while True:
    clientsocket, address = s.accept()  #aceita a conexão de clientsocket no endereço passado
    print(f"Conexão com {address} foi estabelecida!")
    clientsocket.send(bytes("Bem vindo ao Servidor!", "utf-8")) #Mnada mensagem de confirmação para o clientsocket
    clientsocket.close() #Encerra quando a conexao é bem sucedida



