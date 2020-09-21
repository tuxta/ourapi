from PyQt5.QtWidgets import QDialog, QLineEdit, QDialogButtonBox, QFormLayout


class FunctionInputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.name_input = QLineEdit(self)
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)

        layout = QFormLayout(self)
        layout.addRow("Name", self.name_input)
        layout.addWidget(button_box)

        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

    def get_entry(self):
        return self.name_input.text()


class VariableInputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.name_input = QLineEdit(self)
        self.value_input = QLineEdit(self)
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)

        layout = QFormLayout(self)
        layout.addRow("Name", self.name_input)
        layout.addRow("Value", self.value_input)
        layout.addWidget(button_box)

        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

    def get_entries(self):
        return self.name_input.text(), self.value_input.text()
