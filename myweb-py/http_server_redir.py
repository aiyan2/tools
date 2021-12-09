#!/usr/bin/env python3

import sys
import http.server
import socketserver
from urllib.parse import urlparse
from urllib.parse import parse_qs
import argparse
import logging

FORMAT = '%(asctime)-15s %(message)s'
REDIRECT_LINK="https://httpbin.org/ip"

class RedirReqHandler(http.server.SimpleHTTPRequestHandler):
   

    def do_case1(self):    # null-body-chunked
        query_components = parse_qs(urlparse(self.path).query)
        logging.debug("Got query: {}".format(query_components))
        self.send_response(307)
        self.send_header('Location', REDIRECT_LINK)
        self.send_header('Transfer-Encoding', 'chunked')
        self.send_header('Connecion', 'keep-alive')
        self.end_headers()
        self.wfile.write(b'0\r\n\r\n')

    def do_case2(self):    # half of the chunked data
        query_components = parse_qs(urlparse(self.path).query)
        logging.debug("Got query: {}".format(query_components))
        self.send_response(200)
        self.send_header('Transfer-Encoding', 'chunked')
        self.send_header('Connecion', 'keep-alive')
        self.end_headers()
        self.wfile.write(b'3\r\nlab\r\n')
        #self.wfile.write(b'0\r\n\r\n')

    def do_GET(self):
        if self.path == '/case1':
            RedirReqHandler.do_case1(self)
        if self.path == '/case2':
            RedirReqHandler.do_case2(self)  

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s: [%(module)s %(lineno)d] : %(message)s'
    )
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("--redirurl", required=False, default=REDIRECT_LINK, help="URL link to run")
        parser.add_argument("--port", required=False, default=8000, help="Listening port number")

        args = parser.parse_args(sys.argv[1:])
        REDIRECT_LINK = args.__getattribute__("redirurl")
        listen_port = args.__getattribute__("port")
        logging.debug("Start HTTP server at: '%s'", listen_port)
        logging.debug("Redir URL: '%s'", REDIRECT_LINK)
    except Exception as ex:
        logging.error("Parsing arg error %s", ex)
        sys.exit(1)

    try:
        # Create an object of the above class
        HandleClass = RedirReqHandler
        HandleClass.protocol_version = "HTTP/1.1"
        socketserver.TCPServer.allow_reuse_address = True
        httpd = socketserver.TCPServer(("", int(listen_port)), RedirReqHandler)
        httpd.serve_forever()
    except Exception as ex:
        logging.error("Fail to start http server: %s", ex)

