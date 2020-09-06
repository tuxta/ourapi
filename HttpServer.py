from http.server import CGIHTTPRequestHandler, HTTPServer
from PyQt5.QtCore import QThread, pyqtSignal
from io import BytesIO


class HttpHandler(CGIHTTPRequestHandler):

    request_text_change = None
    body = ''

    def set_signaller(self, signal_function):
        self.request_text_change = signal_function

    def do_GET(self):
        self.request_text_change.emit(self.command + " request for " + self.path)
        client_addr, client_port = self.client_address
        self.request_text_change.emit("Client IP Address " + str(client_addr) + " and port " + str(client_port))
        CGIHTTPRequestHandler.do_GET(self)
        self.request_text_change.emit("Returned data: " + self.body)

    def do_POST(self):
        self.request_text_change.emit(self.command + " request for " + self.path)
        CGIHTTPRequestHandler.do_POST(self)

    def setup(self):
        CGIHTTPRequestHandler.setup(self)
        self.original_wfile = self.wfile
        self.wfile = BytesIO()
        # Use subprocess not dup
        self.have_fork = False

    def run_cgi(self):
        CGIHTTPRequestHandler.run_cgi(self)
        self.wfile.seek(0)
        self.body = str(self.wfile.read())
        self.wfile.seek(0)
        self.original_wfile.write(self.wfile.read())


class HttpServer(QThread):

    request_text_change = pyqtSignal(str)

    def run(self):
        handler = HttpHandler
        handler.set_signaller(handler, signal_function=self.request_text_change)
        handler.cgi_directories = ['/API', ]
        httpd = HTTPServer(("localhost", 8000), handler)
        print("serving at port", 8000)
        httpd.serve_forever()
