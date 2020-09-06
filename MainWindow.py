from PyQt5.QtWidgets import QMainWindow
from Ui_MainWindow import Ui_MainWindow
from HttpServer import HttpServer


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Our API')

        self.httpd = HttpServer()
        self.httpd.request_text_change.connect(self.add_to_text)
        self.httpd.start()

    def add_to_text(self, new_text):
        self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + '\n' + new_text)
