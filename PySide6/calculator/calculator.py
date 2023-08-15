from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

from MainWindow import MainWindow
from Display import Display
from Info import Info
from GridButton import GridButton

from env import WINDOW_ICON
from styles import setupTheme

if __name__ == '__main__':

    app = QApplication()
    setupTheme()
    window = MainWindow()

    # Icon
    icon = QIcon(str(WINDOW_ICON))
    window.setWindowIcon(icon)

    # Info
    info = Info('2.0 ^ 10 = 1024')
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    window.addWidgetToVLayout(display)

    # Grid
    bttnsGrid = GridButton(display, info, window)
    window.vlayout.addLayout(bttnsGrid)

    # Adjustments
    window.adjustFixedSize()

    # Execution
    window.show()
    app.exec()