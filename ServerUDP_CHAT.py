#feito por Beatriz Duque
#Exercicio CHAT

import socket


IP_servidor = "" #endereço onde o Server será executado
PORTA_servidor = 31908      #porta aberta pelo Server para conexão

# Criação de socket UDP
# Argumentos, AF_INET que declara a família do protocolo; se fosse um envio via Bluetooth usariamos AF_BLUETOOTH
# SOCK_DGRAM, indica que será UDP.

IP_destino = ""
PORTA_destino = 31906

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 

# IP e porta que o servidor deve aguardar a conexão
sock.bind((IP_servidor, PORTA_servidor)) 
 
while True:
    # Recebe mensagem via socket sock.recvform
    # aloca 1024 bytes
    #separa dados e armazena em data e o endereço de origem e guarda em addr
    data, addr = sock.recvfrom(1024)
    #imprime endereço do cliente
    print("--------------------------------------")
    print("Mensagem recebida de : ",addr)
    #exibe texto enviado pelo cliente
    print ("Mensagem recebida:", data)
    
    MENSAGEM = input("Digite sua mensagem:")
    print("Mensagem enviada......")

    sock2 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    #Envia mensagem usando socket UDP
    sock2.sendto(MENSAGEM.encode('UTF-8'), (IP_destino, PORTA_destino))
