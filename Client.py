from Ui_Client import Ui_Client
from PyQt5.QtWidgets import QDialog, QTreeWidgetItem
from InputDialogs import VariableInputDialog, FunctionInputDialog


class Client(QDialog):
    def __init__(self, parent):
        super(QDialog, self).__init__(parent)

        self.setModal(False)
        self.ui = Ui_Client()
        self.ui.setupUi(self)

        self.ui.functionButton.clicked.connect(self.set_function)
        self.ui.variableButton.clicked.connect(self.add_variable)
        self.ui.resetButton.clicked.connect(self.reset)
        self.ui.runButton.clicked.connect(self.run)

        self.function = ''
        self.variables = {}
        self.url = '/api/'
        self.return_data = None

        self.ui.functionText.setReadOnly(True)
        self.ui.variablesText.setReadOnly(True)

    def set_function(self):
        function_dialog = FunctionInputDialog(self)
        if function_dialog.exec():
            self.reset()
            self.function = function_dialog.get_entry()
            self.ui.functionText.setPlainText(self.function)
            self.rebuild_url()

    def add_variable(self):
        variable_dialog = VariableInputDialog(self)
        if variable_dialog.exec():
            name, value = variable_dialog.get_entries()
            new_var = [name, value]
            self.variables[name] = value
            var_text = self.ui.variablesText.toPlainText() + "\n" + new_var[0] + ' : ' + new_var[1]
            self.ui.variablesText.setPlainText(var_text)

    def reset(self):
        self.function = ''
        self.variables = {}
        self.url = ''
        self.ui.results.clear()
        self.ui.urlText.setText('/api/')
        self.ui.functionText.setPlainText('')
        self.ui.variablesText.setPlainText('')

    def rebuild_url(self):
        self.url = '/api/'
        if len(self.function) > 0:
            self.url += self.function

    def run(self):
        # if the return_data structure status is not 200, then something went wrong
        if self.return_data.status_code > 200:
            # make a simple error dictionary to pass to the build_tree function
            json_dict = {
                'Error':
                    {
                        'Code': self.return_data.status_code, 'Message': self.return_data.content.decode('ascii')
                    }
            }
        else:
            json_dict = self.return_data.json()

        self.ui.results.clear()
        self.build_tree(self.ui.results.invisibleRootItem(), json_dict)

    def build_tree(self, node, value):
        node.setExpanded(False)
        if type(value) is dict:
            for key, val in value.items():
                child = QTreeWidgetItem()
                child.setText(0, str(key))
                node.addChild(child)
                child.setExpanded(False)
                self.build_tree(child, val)
        elif type(value) is list:
            for index, val in enumerate(value):
                child = QTreeWidgetItem()
                node.addChild(child)
                if type(val) is dict:
                    child.setText(0, str(index))
                    self.build_tree(child, val)
                elif type(val) is list:
                    child.setText(0, str(index))
                    self.build_tree(child, val)
                else:
                    child.setText(0, str(val))
                child.setExpanded(False)
        else:
            child = QTreeWidgetItem()
            child.setText(0, str(value))
            node.addChild(child)
            child.setExpanded(False)


