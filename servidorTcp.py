import socket
HOST = ''              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
resposta = 'Ola! Sou o Servidor Robmusic. Seu IP e Porta sao : '
CL = '[Cliente] : '
SV = '[Servidor] : '

while True:
    flname = 'C:\Users\Robson\Desktop\TESTEPYTHON\servidor\servidor.txt'
    fyle = open(flname, 'wb')
    con, cliente = tcp.accept()
    print SV,'Concetado por', cliente
    fyle.write(con.recv(6053))
    print SV, 'arquivo recebido'
    con.send('arquivo recebido' + '\n' + resposta + ' '.join(map(str, cliente)))
    fyle.close()
    while True:
        msg = con.recv(6053)
        if not msg: break
        print CL, cliente, msg
        resp = ' '.join(map(str, cliente))
        con.send(resposta + resp)
    print 'Finalizando conexao do cliente', cliente
    con.close()