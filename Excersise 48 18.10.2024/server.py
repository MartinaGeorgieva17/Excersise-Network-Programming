from http.server import HTTPServer, BaseHTTPRequestHandler

#make server adress 
ip = '127.0.0.1'
port = 8080
server_adress = (ip, port)

#instantiate the server 
httpd = HTTPServer(server_adress, BaseHTTPRequestHandler)

#start server to listen for client's connections 

print(f"HTTP Server is listening on {ip}:{port}")

httpd.serve_forever()