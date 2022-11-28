import socket
HOST = '127.0.0.1' #200.238.4.2    # Endereco IP do Servidor
PORT = 5000   # 61021        # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print 'Para sair use CTRL+X\n'
msg = raw_input()
flname = 'C:\Users\Robson\Desktop\TESTEPYTHON\cliente\cliente.txt'
fyle = open(flname, 'rb')
kar = fyle.read(6053)
tcp.send(kar)
CL = '[Cliente] : '
SV = '[Servidor] : '
print CL + 'ENVIANDO ARQUIVO... \n'
while msg <> '\x18':
    resp = tcp.recv(1024)
    if not resp: break
    print SV + resp
    msg = raw_input()
    tcp.send(msg)
fyle.close()
tcp.close()