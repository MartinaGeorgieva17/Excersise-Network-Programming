import socket

hostname = socket.gethostname()
address = socket.gethostbyname(hostname)
print(hostname)
print(address)