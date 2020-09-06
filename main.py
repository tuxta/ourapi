#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication
from MainWindow import MainWindow


def main():
    app = QApplication(sys.argv)
    app.setOrganizationName("Tuxtas")
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
