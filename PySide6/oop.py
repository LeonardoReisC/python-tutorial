# PySide6: used to build user interfaces
# https://doc.qt.io/qtforpython-6/

from PySide6.QtWidgets import (QApplication, QPushButton, QWidget, QVBoxLayout,
                               QMainWindow)
from PySide6.QtCore import Slot


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.central_widget = QWidget()
        self.box_layout = QVBoxLayout()

        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('My window')
        self.central_widget.setLayout(self.box_layout)

        # widgets
        self.bttn1 = self.make_button('First Button')
        self.bttn1.clicked.connect(self.is_snd_action_checked)

        self.bttn2 = self.make_button('First Button')

        # adding widgets
        self.box_layout.addWidget(self.bttn1)
        self.box_layout.addWidget(self.bttn2)

        # status bar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Showing status bar')

        # menu bar
        self.menu = self.menuBar()
        self.first_menu = self.menu.addMenu('First Menu')

        # actions
        self.first_action = self.first_menu.addAction('First Action')
        self.first_action.triggered.connect(self.execute_action)

        self.second_action = self.first_menu.addAction('Second Action')
        self.second_action.setCheckable(True)
        self.second_action.toggled.connect(self.is_snd_action_checked)

    @Slot()
    def execute_action(self):
        self.status_bar.showMessage('Action executed')

    @Slot()
    def is_snd_action_checked(self):
        print(f'CHECKED? -> {self.second_action.isChecked()}')

    def make_button(self, text):
        button = QPushButton(text)
        button.setStyleSheet('font-size: 20px; color: goldenrod;')

        return button


if __name__ == '__main__':
    app = QApplication()
    window = MyWindow()

    window.show()
    app.exec()  # application loop