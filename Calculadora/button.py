from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot

from variables import MEDIUM_FONT_SIZE
from utils import isNotNumOrDotAndIsEmpty
from display import Display


class  Button(QPushButton):
    def __init__(self,*args ,**kwargs):
        super().__init__(*args,**kwargs)
        self.configStyle()
    

    def configStyle(self):
        self.font().setPixelSize(MEDIUM_FONT_SIZE)
        self.setMinimumSize(75,75)


class ButtonsGrid(QGridLayout):
    def __init__(self,display:Display,*args ,**kwargs):
        super().__init__(*args ,**kwargs)
      

        self._grid_mask =[
            ['C',"<","^","/"],
            ['7', '8','9','*'],
            ['4', '5','6','-'],
            ['1','2','3','='],
            ['','0','.','=']
        ]

        self.display = display
        self._makeGrid()
    def _makeGrid(self):
        for i, row in enumerate(self._grid_mask):
            for j ,button_text in enumerate(row):
                button = Button(button_text)

                if isNotNumOrDotAndIsEmpty(button_text):
                      button.setStyleSheet("background-color: blue; color: white;")

                self.addWidget(button, i, j)
                buttonSlot = self._makeButtonDisplaySlot(self._insertButtonTextToDisplay,button)
                button.clicked.connect(buttonSlot)
                
    def _makeButtonDisplaySlot(self, func, *args, **kwargs):

        @Slot()
        def realSlot(checked):
              func(checked,*args, **kwargs)
        return realSlot

    def _insertButtonTextToDisplay(self,checked,button):
            
            self.display.insert(button.text())
            print(checked)
            
        
    
     
        
