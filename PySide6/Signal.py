# PySide6: used to build user interfaces
# https://doc.qt.io/qtforpython-6/

from PySide6.QtWidgets import (QApplication, QPushButton, QWidget, QVBoxLayout,
                               QMainWindow)
from PySide6.QtCore import Slot


@Slot()
def slot_example(status_bar):
    def inner():
        status_bar.showMessage('Action executed')
    return inner


@Slot()
def another_slot(checked):
    print(f'CHECKED? -> {checked}')


app = QApplication()
window = QMainWindow()
central_widget = QWidget()
layout = QVBoxLayout()

window.setCentralWidget(central_widget)
window.setWindowTitle('My window')

central_widget.setLayout(layout)

# widgets
button1 = QPushButton('Button 1')
button1.setStyleSheet('font-size: 80px;')

button2 = QPushButton('Button 2')
button2.setStyleSheet('font-size: 40px;')

# adding widgets
layout.addWidget(button1)
layout.addWidget(button2)

# status bar
status_bar = window.statusBar()
status_bar.showMessage('Showing status bar')

# menu bar
menu = window.menuBar()
first_menu = menu.addMenu('First Menu')

# actions
first_action = first_menu.addAction('First Action')
first_action.triggered.connect(slot_example(status_bar))

second_action = first_menu.addAction('Second Action')
second_action.setCheckable(True)
second_action.toggled.connect(another_slot)

button1.clicked.connect(lambda: another_slot(second_action.isChecked()))

window.show()
app.exec()  # application loop