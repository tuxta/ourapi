import os
from http.server import HTTPServer
from Definitions import Definitions
from OurApiHandler import OurApiHandler
from PyQt5.QtCore import QThread, pyqtSignal


class HttpServer(QThread):

    request_text_change = pyqtSignal(str)
    client_text_change = pyqtSignal(str)
    response_text_change = pyqtSignal(str)

    def run(self):
        print(os.path.dirname(__file__))

        # define server values
        # server_address = ('localhost', 8000)
        server_address = ('0.0.0.0', 8000)

        # load the definitions file into object
        definitions = Definitions('definitions.ini')

        # setup the http handler
        handler = OurApiHandler
        # handler.set_definitions(handler, definitions_dict=definitions.definitions_dict)
        handler.set_definitions(handler, definitions=definitions)

        handler.set_text_signaller(handler, signal_function=self.request_text_change)
        handler.set_client_signaller(handler, signal_function=self.client_text_change)
        handler.set_response_signaller(handler, signal_function=self.response_text_change)

        # start http server
        httpd = HTTPServer(server_address, handler)
        print("Serving on port", 8000)
        httpd.serve_forever()
