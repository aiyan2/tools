#!/usr/bin/env python3

from http.server import HTTPServer, BaseHTTPRequestHandler
from http import cookies
import socket 
from io import BytesIO
import ssl

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        #content_str = 'Hello, Fortinet!\r\n'
        content_str = 'X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*'
		content_str += subprocess.check_output('hostname -I', shell=True).decode('utf-8')	
        content = content_str.encode();  # convert to byte   
       
        self.send_header('Content-Length',len(content_str))
        self.send_header('Content-type', 'text/html')
        #self.send_header('Content-Encoding','gzip')
        #self.send_header('Content-Encoding','deflate')

        cookie = cookies.SimpleCookie()
        cookie['username'] = "ama@ftnt.com"
        self.send_header("Set-Cookie", cookie.output(header='', sep=''))
        
        self.end_headers()

        self.wfile.write(content)
       

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        #response.write(b'This is POST request. ')
        #response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())

httpds = HTTPServer(('0.0.0.0', 8443), SimpleHTTPRequestHandler)
httpds.socket = ssl.wrap_socket (httpds.socket, 
        keyfile='key.pem', 
        certfile='cert.pem', server_side=True)
httpds.serve_forever()


httpd = HTTPServer(('0.0.0.0', 8005), SimpleHTTPRequestHandler)
# has to comment out for ipv6 support to execute following states:
#httpd.serve_forever()

class HTTPServerV6(HTTPServer):
    address_family = socket.AF_INET6
httpd6 = HTTPServerV6(('::', 8006), SimpleHTTPRequestHandler)
#httpd6.serve_forever()




