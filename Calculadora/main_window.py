from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None =None, *args, **kwargs) -> None:
            super().__init__(parent,*args,**kwargs)

            self.cw = QWidget()
            self.vLayout = QVBoxLayout()
            self.cw.setLayout(self.vLayout)
            self.setWindowTitle("Calculadora")



            self.setCentralWidget(self.cw)



    def addWidgetToVLayout(self,widget: QWidget):
            self.vLayout.addWidget(widget)

