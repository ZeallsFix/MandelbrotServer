import socket

HOST = '127.0.0.1'
PORT = 8080


def recive(host, port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    sock.listen(0)
    request, addr = sock.accept()
    return request.makefile('r', 0)


#for line in recive(HOST, PORT):
 #   print(line)


# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now connect to the web server on port 80 - the normal http port
s.connect(("www.python.org", 80))