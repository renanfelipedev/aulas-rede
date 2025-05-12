#!/usr/bin/env python3
#### CLIENTE #####

import socket

address = input("Digite o endereço do servidor (deixe em branco para 'localhost'): ") or 'localhost'
port = input("Digite a porta do servidor (deixe em branco para '10000'): ") or 10000
port = int(port)
server_address = (address, port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server_address)
print("Conexão estabelecida com o SERVIDOR: %s:%s" % server_address)

try:
    message = input("CLIENTE> ")
    client.sendall(message.encode())
    response = client.recv(port)
    print("SERVIDOR> %s" % response.decode())
except Exception as e:
    print("Erro: %s" % e)
finally:
    client.close()
