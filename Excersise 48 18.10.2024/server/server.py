from http.server import HTTPServer, BaseHTTPRequestHandler


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        #setup header
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        response_body = "<h1>Server is working!</h1>".encode("utf-8")
        self.wfile.write(response_body)

#make server adress 
IP = '127.0.0.1'
PORT = 8080

if __name__== "__main__":
    server_address = (IP, PORT)

#instantiate the server 
    httpd = HTTPServer(server_address, RequestHandler)

#start server to listen for client's connections 

print(f"HTTP Server is listening on {IP}:{PORT}")
httpd.serve_forever()

