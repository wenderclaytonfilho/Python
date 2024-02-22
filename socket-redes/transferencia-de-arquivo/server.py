import socket
#Aqui eu consigo o nome do host
hostname = socket.gethostname()
#E aqui estou pegando o IP do host
HOST = socket.gethostbyname(hostname)
PORT = 40000
#socket() Cria um socket e retorna um descritor de arquivo 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind() Associa o socket criado com um endere ̧co e uma porta
s.bind((HOST,PORT))
#listen() Coloca o socket para aguardar conexões
s.listen(1)
#accept() Aceita uma nova conex ̃ao e cria um novo socket no servidor dedicado a esse cliente.
conn,addr = s.accept()
arq = open('socket-redes\transferencia-de-arquivo\dados.txt','wb')
while 1:
    #recv() Recebe as mensagens através do socket. O argumento informa o número de bytes (do buffer) que podem ser recebidos.
    dados = conn.recv(8)
    if not dados:
        break
    print(dados)
    arq.write(dados)
arq.close()
#close() Desaloca o descritor de arquivo ou fecha o socket
conn.close()