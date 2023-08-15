from PySide6.QtWidgets import QGridLayout
from PySide6.QtCore import Slot
from Button import Button

from utils import isNumOrDot, isEmpty, isValidNumber, converToNumber

from typing import TYPE_CHECKING  # avoids circular imports

if TYPE_CHECKING:
    from Display import Display
    from Info import Info
    from MainWindow import MainWindow


class GridButton(QGridLayout):
    def __init__(self, display: 'Display', info: 'Info', window: 'MainWindow',
                 *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['N', '0', '.', '='],
        ]

        self.display = display
        self.info = info
        self.window = window
        self.equation = ''
        self._left: float | None = None
        self._right: float | None = None
        self._op: str | None = None

        self._makeGrid()

    def _makeGrid(self):
        self.display.eqPressed.connect(self._eq)
        self.display.deletePressed.connect(self._backspace)
        self.display.clearPressed.connect(self._clear)
        self.display.inputPressed.connect(self._insertTextToDisplay)
        self.display.operatorPressed.connect(self._configLeftOp)

        for rowNumber, row in enumerate(self._gridMask):
            for columnNumber, bttn_text in enumerate(row):
                bttn = Button(bttn_text)

                if not isNumOrDot(bttn_text) and not isEmpty(bttn_text):
                    bttn.setProperty('cssClass', 'specialButton')
                    self.configSpecialButton(bttn)

                self.addWidget(bttn, rowNumber, columnNumber)

                slot = self._makeSlot(self._insertTextToDisplay, bttn.text())
                self._connectButtonClicked(bttn, slot)

    def _connectButtonClicked(self, bttn: Button, slot):
        bttn.clicked.connect(slot)

    def configSpecialButton(self, bttn: Button):
        text = bttn.text()

        if text == 'C':
            slot = self._makeSlot(self._clear)
            self._connectButtonClicked(bttn, slot)

        if text == '◀':
            slot = self._backspace
            self._connectButtonClicked(bttn, slot)

        if text == 'N':
            slot = self._invertNumber
            self._connectButtonClicked(bttn, slot)

        if text in '+-*/^':
            slot = self._makeSlot(self._configLeftOp, text)
            self._connectButtonClicked(bttn, slot)

        if text == '=':
            slot = self._eq
            self._connectButtonClicked(bttn, slot)

    @Slot()
    def _makeSlot(self, func, *args, **kwargs):

        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot

    @Slot()
    def _insertTextToDisplay(self, text):
        newDisplayValue = self.display.text() + text

        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(text)

        self.display.setFocus()

    @Slot()
    def _clear(self):
        self._left = None
        self._right = None
        self._op = None
        self.equation = ''
        self.display.clear()

        self.display.setFocus()

    @Slot()
    def _configLeftOp(self, text):
        displayText = self.display.text()
        self.display.clear()

        self.display.setFocus()

        if not isValidNumber(displayText) and self._left is None:
            self._showError('Empty equation!')
            return

        if self._left is None:
            self._left = converToNumber(displayText)

        self._op = text

        self.equation = f'{self._left} {self._op} ??'

    @Slot()
    def _invertNumber(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            return

        number = converToNumber(displayText) * -1

        self.display.setText(str(number))

    @Slot()
    def _backspace(self):
        self.display.backspace()
        self.display.setFocus()

    @Slot()
    def _eq(self):
        displayText = self.display.text()

        if not isValidNumber(displayText) or self._left is None:
            return

        self._right = converToNumber(displayText)
        self.equation = f'{self._left} {self._op} {self._right}'

        result = 'error'
        try:
            result = eval(self.equation.replace('^', '**'))
        except ZeroDivisionError:
            self._showError('ERROR: You can\'t divide by zero!')
        except OverflowError:
            self._showError('ERROR: An overflow occurred!')

        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')

        try:
            self._left = converToNumber(result)
        except ValueError:
            self._left = None

        self._right = None

        self.display.setFocus()

    def _makeDialog(self, text):
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)
        return msgBox

    def _showError(self, text):
        msgBox = self._makeDialog(text)
        msgBox.setIcon(msgBox.Icon.Critical)

        msgBox.exec()
        self.display.setFocus()

    def _showInfo(self, text):
        msgBox = self._makeDialog(text)
        msgBox.setIcon(msgBox.Icon.Information)

        msgBox.exec()
        self.display.setFocus()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)