from socket import *
import sys
import time

# definicao das variaveis
serverName = str(sys.argv[1])
serverPort = 30000 # porta a se conectar
clientSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
clientSocket.connect((serverName, serverPort)) # conecta o socket ao servidor

sentence = 'hostname: ' + gethostname() + ' ip: ' + gethostbyname(gethostname())
print ('> enviando para o servidor -> %s' % sentence)
clientSocket.send(sentence.encode('utf-8')) # envia o texto para o servidor
time.sleep(2)
clientSocket.close() # encerramento o socket do cliente
