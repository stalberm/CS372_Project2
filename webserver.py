import socket
import sys

if len(sys.argv) > 1:
    port = sys.argv[1]
else:
    port = 28333
    
s = socket.socket()
s.bind(('', int(port)))
s.listen()
response = f"HTTP/1.1 200 OK\r\n\
Content-Type: text/plain\r\n\
Content-Length: 6\r\n\
Connection: close\r\n\r\n\
Hello!"

response = response.encode("ISO-8859-1")
while True:
    new_conn = s.accept()
    new_socket = new_conn[0]
    request = ''
    while True:
        chunk = new_socket.recv(4096).decode("ISO-8859-1")
        request = request + chunk
        if request.find("\r\n\r\n"):
            break
    new_socket.sendall(response)
    new_socket.close()