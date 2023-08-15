from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # setting up basic layout
        self.cw = QWidget()
        self.vlayout = QVBoxLayout()

        self.cw.setLayout(self.vlayout)
        self.setCentralWidget(self.cw)

        # title
        self.setWindowTitle('Calculator')

    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetToVLayout(self, widget: QWidget):
        self.vlayout.addWidget(widget)

    def makeMsgBox(self):
        return QMessageBox(self)
