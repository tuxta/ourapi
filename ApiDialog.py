from PyQt5.QtWidgets import QDialog, QTreeWidgetItem
from Ui_ApiDialog import Ui_ApiDialog


class ApiDialog(QDialog):
    def __init__(self, parent, api_dict):
        super().__init__(parent)
        self.ui = Ui_ApiDialog()
        self.ui.setupUi(self)

        self.ui.closeButton.clicked.connect(self.close)

        # Load api into Tree
        node = self.ui.apiTree.invisibleRootItem()
        for key, val in api_dict.items():
            api_func = QTreeWidgetItem()
            api_func.setText(0, str(key))
            api_func.setExpanded(False)
            node.addChild(api_func)

            args_node = QTreeWidgetItem()
            api_func.addChild(args_node)
            args_node.setText(0, 'Args')
            args_node.setExpanded(False)

            if not val['args']:
                child = QTreeWidgetItem()
                args_node.addChild(child)
                child.setText(0, 'None')
                child.setExpanded(False)
            else:
                for index, arg in enumerate(val['args']):
                    child = QTreeWidgetItem()
                    args_node.addChild(child)
                    child.setText(0, str(arg))
                    child.setExpanded(False)

            sql_node = QTreeWidgetItem()
            api_func.addChild(sql_node)
            sql_node.setText(0, 'SQL')
            sql_node.setExpanded(False)

            sql_str = QTreeWidgetItem()
            sql_str.setText(0, val['sql'])
            sql_str.setExpanded(False)
            sql_node.addChild(sql_str)
