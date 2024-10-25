import socket
import threading

BUFF_SIZE = 1024
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'END'

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True

    while connected:
        msg = conn.recv(BUFF_SIZE).decode(FORMAT).strip()

        if msg == DISCONNECT_MESSAGE:
            connected = False

        print(f"[{addr}] {msg}")
        conn.send( "Msg received".encode(FORMAT) )

    conn.close()

def start():
    while True:
        conn, addr = server.accept() # blocking, untill a client is connected
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__=='__main__':
    try:
        # create an IPv4 TCP socket:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # bind the socket to the host and port
        server.bind(('127.0.0.1', 8888))

        # listen for incoming connections
        server.listen()
        print("Server is listening on 127.0.0.1:8888")

        start()
    except KeyboardInterrupt:
        print('Buy...')
        exit(0)