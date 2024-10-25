import socket

BUFF_SIZE = 1024
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'END'

def send(client, msg):
    message = (msg + "\n").encode(FORMAT)
    client.send(message)
    response = client.recv(BUFF_SIZE).decode(FORMAT)
    print(response)

if __name__=='__main__':
    try:
        # open client socket (TCP)
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # connect to the server
        client.connect(('127.0.0.1', 8888))

        # send some messages:
        while True:
            msg = input("Enter a message: ")
            if msg == '':
                send(client, DISCONNECT_MESSAGE)
                break
            else:
                send(client, msg)
    except KeyboardInterrupt:
        print('Buy...')
    finally:
        client.close()