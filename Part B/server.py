import socket
import random

Q_Size = 5

responseList = ['It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes definitely.',
                'You may rely on it.', 'As I see it, yes.', 'Most likely.', 'Yes.',
                'Reply hazy, try again.', 'Ask again later lol.',
                "Too lazy try again later.", "Don't count on it.", "No", "Nah", "Doubt it."]


def server():
    serv = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
    serv.bind(('', 5000))
    serv.listen(Q_Size)

    while True:
        conn, addr = serv.accept()
        print("Working")
        print(f'Cntn: {addr}')
        from_client = ''
        while True:
            data = conn.recv(4096)
            if not data:
                break
            Message = random.choice(responseList)

            from_client += data.decode()
            print(from_client)
            conn.send(
                Message.encode())

        conn.close()
        print('client disconnected')

if __name__ == '__main__':
    server()
