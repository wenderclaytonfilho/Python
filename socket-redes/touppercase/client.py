import socket

serverName = socket.gethostname()
serverPort = 12000
#socket() Cria um socket e retorna um descritor de arquivo 
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect() Tenta estabelecer uma conexão com um socket em um servidor.
clientSocket.connect((serverName, serverPort))
sentence = input("Entre com a mensagem usando letras minúsculas: ")
 #send() Transmite mensagem pelo socket do cliente para a conexão, usado no TCP por não precisar anexar o par (endereço IP, Porta), já que isso já  ́e resolvido na conexão.
clientSocket.send(sentence.encode())
#recv() Recebe as mensagens através do socket. O argumento informa o número de bytes (do buffer) que podem ser recebidos.
modifiedSentence = clientSocket.recv(1024)
print('Resposta do servidor:', modifiedSentence.decode())
#close() Desaloca o descritor de arquivo ou fecha o socket
clientSocket.close()
