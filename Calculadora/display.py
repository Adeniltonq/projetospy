from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt , Signal 
from PySide6.QtGui import QKeyEvent

from variables import BIG_FONT_SIZE, TEXT_MARGIN
from utils import isEmpty, isNumOrDot


class Display(QLineEdit):
    eqPressed = Signal()
    delPressed = Signal()
    eqRequested = Signal()
    inputPressed = Signal(str)
    operatorPressed = Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        margins = [TEXT_MARGIN for _ in range(4)]
        self.setStyleSheet(f"font-size: {BIG_FONT_SIZE}px")
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margins)

    def keyPressEvent(self, event: QKeyEvent) -> None:

        text = event.text().strip()
        key = event.key()
        isEnter = key in [Qt.Key.Key_Enter, Qt.Key.Key_Return]
        isDelete= key in [Qt.Key_Backspace, Qt.Key.Key_Delete]
        isEsc= key in [Qt.Key_Escape]
        isOperator= key in [Qt.Key.Key_Plus, Qt.Key.Minus, Qt.Key.Slash, Qt.Key.Asterisk]

        if isEnter or text == '=':
           self.eqRequested.emit()
           return event.ignore()
        
        if isEsc or text.lower() == 'c':
           self.eqPressed.emit()
           return event.ignore()
        

        if isDelete or text.lower() == 'd':
           self.delPressed.emit()
           
           return event.ignore()
        
        if isOperator:
           self.operatorPressed.emit()
           return event.ignore()
        
        if isEmpty(text):
            return event.ignore()
        

        if isNumOrDot(text):
            self.inputPressed.emit(text)
            return event.ignore()


        
