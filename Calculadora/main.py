from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel
import sys

from main_window import MainWindow

if __name__ == '__main__':
    app =QApplication(sys.argv)

# ->QApli ->QMainwin ->Qwidget->QVBoxLAy ->

    window = MainWindow()

    label1 = QLabel("Olá Mundo")
    label1.setStyleSheet("font-size: 50px")
    window.v_layout.addWidget(label1)


    window.show()


    app.exec()

