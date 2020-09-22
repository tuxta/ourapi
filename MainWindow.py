from PyQt5.QtWidgets import QMainWindow, QFileDialog
from Ui_MainWindow import Ui_MainWindow
from HttpServer import HttpServer

from ClientGET import ClientGET


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Our api')

        self.httpd = HttpServer()
        self.httpd.request_text_change.connect(self.add_to_request)
        self.httpd.client_text_change.connect(self.add_to_client)
        self.httpd.response_text_change.connect(self.add_to_response)
        self.httpd.start()

        self.ui.saveSession.clicked.connect(self.save_session)
        self.ui.resetSession.clicked.connect(self.reset_session)
        self.ui.testClientGet.clicked.connect(self.run_test_client_get)
        self.ui.testClientPost.clicked.connect(self.run_test_client_post)

        self.session_string = ''

        self.ui.requestText.setReadOnly(True)
        self.ui.clientText.setReadOnly(True)
        self.ui.responseText.setReadOnly(True)

    def add_to_request(self, request_text):
        request_type, request_string = request_text.split(',')
        self.ui.requestText.setText(request_string)
        request_log = f"""\n\n
################### NEW REQUEST ###################
\t{request_string}\t
###################################################

"""
        self.session_string += request_log

    def add_to_client(self, client_text):
        self.ui.clientText.setText(client_text)
        request_log = f"Client details\n{client_text}\n"
        self.session_string += request_log

    def add_to_response(self, response_text):
        self.ui.responseText.setText(response_text)
        request_log = f"\nResponse\n{response_text}\n\n"
        self.session_string += request_log

    def save_session(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Session File", "", "Text Files (*.txt)")
        if file_name:
            with open(file_name, "w") as session_file:
                session_file.write(self.session_string)

    def reset_session(self):
        self.session_string = ''
        self.ui.requestText.clear()
        self.ui.clientText.clear()
        self.ui.responseText.clear()

    def run_test_client_get(self):
        get_client = ClientGET(self)
        get_client.setModal(False)
        get_client.show()

    def run_test_client_post(self):
        get_client = ClientGET(self)
        get_client.setModal(False)
        get_client.show()
