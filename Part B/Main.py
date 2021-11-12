import socket

def client():
    query = input("Ask the magic ball a question: ")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 5000))
    sock.send(query.encode())
    from_server = sock.recv(4096)
    sock.close()
    print(from_server.decode())
    


