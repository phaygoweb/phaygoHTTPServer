import socket
import http.server

SSL = False
PORT = 443 if SSL else 80

def do_request(connstream, from_addr):
    x = object()
    http.server.SimpleHTTPRequestHandler(connstream, from_addr, x)

def serve():
    bindsocket = socket.socket()
    bindsocket.bind(('localhost', PORT))
    bindsocket.listen(5)

    print("Serving on port", PORT)

    while True:
        try:
            newsocket, from_addr = bindsocket.accept()
            if SSL:
                connstream = ssl.wrap_socket(newsocket, server_side = True, certfile = 'localhost.pem', ssl_version = ssl.PROTOCOL_TLSv1)
            else:
                connstream = newsocket

            do_request(connstream, from_addr)
        
        except Exception:
            traceback.print_exc()
            
serve()