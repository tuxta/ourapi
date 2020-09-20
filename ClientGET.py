from PyQt5.QtWidgets import QDialog
from Ui_ClientGET import Ui_ClientGET
import requests


class ClientGET(QDialog):
    def __init__(self, parent):
        super(QDialog, self).__init__(parent)

        self.setModal(False)
        self.ui = Ui_ClientGET()
        self.ui.setupUi(self)

        self.setWindowTitle("GET Client")

        self.ui.functionButton.clicked.connect(self.set_function)
        self.ui.variableButton.clicked.connect(self.add_variable)
        self.ui.resetButton.clicked.connect(self.reset)
        self.ui.runButton.clicked.connect(self.run)

        self.function = ''
        self.variables = []
        self.url ='/api/'

    def set_function(self):
        self.function = 'country_info'
        self.ui.functionText.setPlainText(self.function)
        self.rebuild_url()

    def add_variable(self):
        new_var = ['country', 'Canada']
        self.variables.append(new_var)
        var_text = self.ui.variablesText.toPlainText() + "\n" + new_var[0] + ' : ' + new_var[1]
        self.ui.variablesText.setPlainText(var_text)
        self.rebuild_url()

    def reset(self):
        self.function = ''
        self.variables = []
        self.url = ''
        self.ui.urlText.setText('/api/')
        self.ui.functionText.setPlainText('')
        self.ui.variablesText.setPlainText('')

    def rebuild_url(self):
        self.url = f'/api/{self.function}'
        if len(self.variables) > 0:
            self.url = self.url + '?'
            for var in self.variables:
                self.url = self.url + f"{var[0]}={var[1]}&"
                print(self.url)
            self.url = self.url[:-1]
        self.ui.urlText.setText(self.url)

    def run(self):
        return_data = requests.get('http://127.0.0.1:8000' + self.url)
        print(return_data.content.decode('ascii'))
