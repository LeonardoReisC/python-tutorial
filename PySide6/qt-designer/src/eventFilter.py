from PySide6.QtCore import QObject, QEvent
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QMainWindow, QApplication

from window import Ui_MainWindow

from typing import cast


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.sendButton.clicked.connect(self.updateLabel)

        self.lineName.installEventFilter(self)  # gets all lineName's events

    def updateLabel(self):
        text = self.lineName.text()
        self.label1.setText(text)

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:

        # filtering an event
        if event.type() == QEvent.Type.KeyPress:
            event = cast(QKeyEvent, event)

            text = self.lineName.text()
            self.label1.setText(text + event.text())

        return super().eventFilter(watched, event)


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()

    window.show()
    app.exec()