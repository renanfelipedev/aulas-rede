#!/usr/bin/env python3
#### SERVIDOR #####

import socket

address = input("Digite o endereço do servidor (deixe em branco para endereço 'localhost'): ") or 'localhost'
port = input("Digite a porta do servidor (deixe em branco para porta '10000'): ") or 10000
port = int(port)
server_address = (address, port)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_address)
server.listen(1)
print("Aguardando conexão em %s:%s" % server_address)

connection, client_address = server.accept()
print("Conexão estabelecida com o CLIENTE: %s:%s" % client_address)

try:
    data = connection.recv(port)
    print("CLIENTE> %s" % data.decode())

    message = input("SERVIDOR> ")
    connection.sendall(message.encode())
except Exception as e:
    print("Erro: %s" % e)
finally:
    connection.close()
    server.close()
