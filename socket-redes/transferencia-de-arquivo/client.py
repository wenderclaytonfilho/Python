import socket

#Aqui eu consigo o nome do host
hostname = socket.gethostname()
#E aqui estou pegando o IP do host
HOST = socket.gethostbyname(hostname)

PORT=65432
#socket() Cria um socket e retorna um descritor de arquivo 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect() Tenta estabelecer uma conexão com um socket em um servidor.
s.connect((HOST,PORT))

arq = open('socket-redes\transferencia-de-arquivo\dados.txt','r')
for i in arq.readlines():
    print(i,'\n')
    s.send(i.encode())
arq.close()
#close() Desaloca o descritor de arquivo ou fecha o socket
s.close()