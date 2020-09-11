from http.server import CGIHTTPRequestHandler, HTTPServer
from PyQt5.QtCore import QThread, pyqtSignal
from io import BytesIO


class HttpHandler(CGIHTTPRequestHandler):

    request_text_change = None
    client_text_change = None
    response_text_change = None
    request = ''
    client = ''
    body = ''

    def set_text_signaller(self, signal_function):
        self.request_text_change = signal_function

    def set_client_signaller(self, signal_function):
        self.client_text_change = signal_function

    def set_response_signaller(self, signal_function):
        self.response_text_change = signal_function

    def do_GET(self):
        CGIHTTPRequestHandler.do_GET(self)
        if self.path[-3:] != 'ico':
            self.request_text_change.emit(self.command + "," + self.path)
            client_address, client_port = self.client_address
            self.client_text_change.emit("Client IP Address " + str(client_address) + " and port " + str(client_port))
            self.response_text_change.emit(self.body)

    def do_POST(self):
        self.request_text_change.emit(self.command + " request for " + self.path)
        client_address, client_port = self.client_address
        self.client_text_change.emit("Client IP Address " + str(client_address) + " and port " + str(client_port))
        CGIHTTPRequestHandler.do_POST(self)
        self.response_text_change.emit("Returned data: " + self.body)

    def setup(self):
        CGIHTTPRequestHandler.setup(self)
        self.original_wfile = self.wfile
        self.wfile = BytesIO()
        # Use subprocess not dup
        self.have_fork = False

    def run_cgi(self):
        CGIHTTPRequestHandler.run_cgi(self)
        self.wfile.seek(0)
        self.body = self.wfile.read().decode()
        self.wfile.seek(0)
        self.original_wfile.write(self.wfile.read())


class HttpServer(QThread):

    request_text_change = pyqtSignal(str)
    client_text_change = pyqtSignal(str)
    response_text_change = pyqtSignal(str)

    def run(self):
        handler = HttpHandler
        handler.set_text_signaller(handler, signal_function=self.request_text_change)
        handler.set_client_signaller(handler, signal_function=self.client_text_change)
        handler.set_response_signaller(handler, signal_function=self.response_text_change)
        handler.cgi_directories = ['/api', ]
        httpd = HTTPServer(("localhost", 8000), handler)
        print("serving at port", 8000)
        httpd.serve_forever()
