from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None =None, *args, **kwargs) -> None:
            super().__init__(parent,*args,**kwargs)

            self.cw = QWidget()
            self.v_layout = QVBoxLayout()
            self.cw.setLayout(self.v_layout)
            self.setWindowTitle("Calculadora")



            self.setCentralWidget(self.cw)



    def addWidgetToVLayout(self,widget: QWidget):
            self.v_layout.addWidget(widget)

