
from typing import TYPE_CHECKING
import math

from PySide6.QtWidgets import QPushButton, QGridLayout, QMessageBox
from PySide6.QtCore import Slot


from variables import MEDIUM_FONT_SIZE
from utils import isNotNumOrDotAndIsEmpty, isValidNumber

if TYPE_CHECKING:
    from display import Display
    from info import Info
    from main_window import MainWindow


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)


class ButtonsGrid(QGridLayout):
    def __init__(self, display: 'Display', info: 'Info', window: 'MainWindow',*args, **kwargs):
        super().__init__(*args, **kwargs)

        self._grid_mask = [
            ['C', "D", "^", "/"],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['', '0', '.', '=']
        ]

        self.display = display
        self.info = info
        self.window = window
        self._equation = ''
        self._makeGrid()
        self._left = None
        self._right =None
        self._op = None
        self._equationInitialValue = "Sua conta"
        self.equation = self._equationInitialValue

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def vouApagarVoce(self):
        print("Sinal recebido")

    def _makeGrid(self):

        self.display.eqRequested.connect(self.vouApagarVoce)
        self.display.eqPressed.connect(self.display.backspace)
        self.display.delPressed.connect(self.vouApagarVoce)
        self.display.inputPressed.connect(self.vouApagarVoce)

        for i, row in enumerate(self._grid_mask):
            for j, button_text in enumerate(row):
                if button_text == '':
                    continue

                button = Button(button_text)

                if isNotNumOrDotAndIsEmpty(button_text):
                    button.setStyleSheet("background-color: blue; color: white;")
                    self._configSpecialButton(button)

                self.addWidget(button, i, j)

                slot = self._makeSlot(self._insertButtonTextToDisplay, button)
                self._connectButtonClicked(button, slot)

    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button):
        text = button.text()

        if text == 'C':
            slot = self._makeSlot(self._clear, 'Mensagem')
            self._connectButtonClicked(button, slot)

        if text == 'D':
         
            self._connectButtonClicked(button, self.display.backspace)
           

        if text in '+-/*^':
            self._connectButtonClicked(button, self._makeSlot(self._operatorCliked, button))

        if text == '=':
            self._connectButtonClicked(button, self._eq)

    def _makeSlot(self, func, *args, **kwargs):
        @Slot()
        def realSlot(checked=False):
            func(*args, **kwargs)
        return realSlot

    def _insertButtonTextToDisplay(self, button):
        buttonText = button.text()

        newDisplayValue = self.display.text() + buttonText

        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(buttonText)

    def _clear(self, msg):
        print("Vou fazeer algo", msg)
        self.display.clear()
        self.equation = self._equationInitialValue

    def _operatorCliked(self,button):
        buttonText = button.text()
        displayText = self.display.text()
        self.display.clear()
        


        if not isValidNumber(displayText) and  self._left is None:
            self._left = None
            self._right =None
            self._op = None
          
            return
        
        if self._left is None:
            self._left = float(displayText)
            

        self._op = buttonText
        self.equation = f'{self._left} {self._op} ??'

    def _eq(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            self._showError("Voce não digitou nada")
            return
    
        self._right = float(displayText)
        self.equation = f'{self._left} {self._op} {self._right}'
        result = 'error'
        self._left: float
        try:
            if '^' in self.equation:
                result = math.pow(self._left, self._right)
            else:
                result = eval(self.equation)
        except ZeroDivisionError:
                print('Erro: divisão por zero')
        
        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')
        self._left = result
        self._right = None

        if result == 'error':
            self._left = None

    def _showError(self, text):
        msgBox  =self.window.makeMsgBox()
        msgBox.setText(text)
        msgBox.setIcon(msgBox.Icon.Warning)
        msgBox.exec()
    