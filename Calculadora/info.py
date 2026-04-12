from PySide6.QtWidgets import QLabel, QWidget

from variables import SMALL_FONT_SIZE

from typing import Optional

class Info(QLabel):
    def __init__ (self, text:str, parent: QWidget | None = None) -> None:
        super().__init__(text, parent)

    def configStyle(self):
        self.setStyleSheet(f'font-size: {SMALL_FONT_SIZE}px')
