#!/usr/bin/env python3

from http.server import HTTPServer, BaseHTTPRequestHandler
import socket 
from io import BytesIO
import ssl
import argparse
import subprocess

__version__ = 1.1

class MyHandler(BaseHTTPRequestHandler):
    protocol_version = 'HTTP/1.1'

    def do_GET(self):
        self.send_response(200)
        content_str = 'Hello, Fortinet!\r\n'
        #content_str = 'X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*'
        content_str += subprocess.check_output('hostname -I',shell=True).decode('utf-8')
        content = content_str.encode();  # convert to byte      
        self.send_header('Content-Length',len(content_str))
        self.send_header('Content-type', 'text/html')
        #self.send_header('Content-Encoding','gzip')
        #self.send_header('Content-Encoding','deflate')
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

class HTTPServerV6(HTTPServer):
    address_family = socket.AF_INET6
   

parser = argparse.ArgumentParser(description='allweb')
parser.add_argument('--ipv6',
    action='store_true',
    help='ipv4?v6' )

parser.add_argument('--ssl',
    action='store_true',
    help='ssl?' )

parser.add_argument('--port',
                    default=8080,
                    type=int)
args = parser.parse_args()

myport=int(args.port)

#start servers
if not(args.ipv6):
    print ('# http  ipv4 on port:'+str(myport))
    httpd = HTTPServer(('0.0.0.0', myport),MyHandler)
    if args.ssl:        
        httpd.socket = ssl.wrap_socket (httpd.socket, keyfile='key.pem', 
            certfile='cert.pem', server_side=True)
       
    httpd.serve_forever()
else: # ipv6
    print ('# http  ipv6 on port:'+str(myport))
    httpd6 = HTTPServerV6(('::', myport), MyHandler)
    
    if (args.ssl):      
        httpd6.socket = ssl.wrap_socket (httpd6.socket, keyfile='key.pem', 
            certfile='cert.pem', server_side=True)
    httpd6.serve_forever()




