from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel

import sys

from main_window import MainWindow
from variables import WINDOW_ICON_DIR

if __name__ == '__main__':
    app =QApplication(sys.argv)

# ->QApli ->QMainwin ->Qwidget->QVBoxLAy ->

    window = MainWindow()

    label1 = QLabel("Olá Mundo")
    label1.setStyleSheet("font-size: 50px")
    window.addWidgetToVLayout(label1)

    icon =QIcon(str(WINDOW_ICON_DIR))

    app.setWindowIcon(icon)





    window.show()


    app.exec()

