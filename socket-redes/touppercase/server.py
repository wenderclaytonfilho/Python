from socket import *
serverPort = 12000
#socket() Cria um socket e retorna um descritor de arquivo 
serverSocket = socket(AF_INET, SOCK_STREAM)
#bind() Associa o socket criado com um endere ̧co e uma porta
serverSocket.bind(('',serverPort))
#listen() Coloca o socket para aguardar conexões
serverSocket.listen(1)

print('O servidor está pronto para receber as mensagens')

while 1:
    connectionSocket, addr = serverSocket.accept()
    #recv() Recebe as mensagens através do socket. O argumento informa o número de bytes (do buffer) que podem ser recebidos.
    sentence = connectionSocket.recv(1024)
    capitalizedSentence = sentence.upper()
    #send() Transmite mensagem pelo socket do cliente para a conexão, usado no TCP por não precisar anexar o par (endereço IP, Porta), já que isso já  ́e resolvido na conexão.
    connectionSocket.send(capitalizedSentence)
    #close() Desaloca o descritor de arquivo ou fecha o socket
    connectionSocket.close()
