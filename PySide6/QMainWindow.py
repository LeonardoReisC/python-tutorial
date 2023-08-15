# PySide6: used to build user interfaces
# https://doc.qt.io/qtforpython-6/

from PySide6.QtWidgets import (QApplication, QPushButton, QWidget, QVBoxLayout,
                               QMainWindow)

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
first_action = first_menu.addAction('First Action')

window.show()
app.exec()  # application loop