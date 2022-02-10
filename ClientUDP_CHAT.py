#feito por Beatriz Duque
#Exercicio CHAT

import socket  #importa modulo socket
  
IP_destino = ""  #Endereço IP do servidor
PORTA_destino = 31908          #Numero de porta do servidor
IP_servidor = ""
PORTA_servidor = 31906
MENSAGEM = 'X'

sock2 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 

# IP e porta que o servidor deve aguardar a conexão
sock2.bind((IP_servidor, PORTA_servidor))

while MENSAGEM!= "quit" :
    print("----------------------------------")
    MENSAGEM = input("Digite sua mensagem:")
     
    print ("Endereço IP de destino:", IP_destino)
    print ("Porta UDP de destino:", PORTA_destino)
    print ("Mensagem enviada:", MENSAGEM)
     
    #Criação de socket UDP
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    #Envia mensagem usando socket UDP
    sock.sendto(MENSAGEM.encode('UTF-8'), (IP_destino, PORTA_destino))

    
    data, addr = sock2.recvfrom(1024)
    #imprime endereço do cliente
    print("Mensagem recebida de : ",addr)
    #exibe texto enviado pelo cliente
    print ("Mensagem recebida:", data)
    

print("\nSAINDO....")
