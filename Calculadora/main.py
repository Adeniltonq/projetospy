import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication 

from button import ButtonsGrid
from display import Display
from info import Info
from main_window import MainWindow

from styles import setupTheme
from variables import WINDOW_ICON_DIR
 
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow()
 
 
    icon = QIcon(str(WINDOW_ICON_DIR))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)
 
  
    info = Info('Sua conta')
    window.addWidgetToVLayout(info)
 
   
    display = Display()
    window.addWidgetToVLayout(display)
 
    buttonsGrid = ButtonsGrid(display)
    window.vLayout.addLayout(buttonsGrid)
 
   
  
    window.show()
    app.exec()
