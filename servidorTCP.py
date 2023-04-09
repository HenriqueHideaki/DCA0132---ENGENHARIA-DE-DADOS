from socket import * # sockets

# definicao das variaveis
serverPort = 30000 # porta a servir
serverSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
serverSocket.bind(('',serverPort)) # bind do ip do servidor com a porta
serverSocket.listen(1) # socket pronto para 'ouvir' conexoes
serverIP=gethostbyname(gethostname())
print ('> servidor iniciado em %s:%d ...' % (serverIP,serverPort))
while 1:
  connectionSocket, addr = serverSocket.accept() # aceita as conexoes dos clientes
  sentence = connectionSocket.recv(1024) # recebe dados do cliente
  sentence = sentence.decode('utf-8') # codifica em utf-8
  print ('> mensagem recebida de %s -> %s' % (addr, sentence))
  connectionSocket.close() # encerra o socket com o cliente
serverSocket.close() # encerra o socket do servidor