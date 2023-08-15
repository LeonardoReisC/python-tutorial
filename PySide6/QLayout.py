# PySide6: used to build user interfaces
# https://doc.qt.io/qtforpython-6/

from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout

app = QApplication()

button1 = QPushButton('Button 1')
button1.setStyleSheet('font-size: 80px;')

button2 = QPushButton('Button 2')
button2.setStyleSheet('font-size: 40px;')

# creates central widget and layout
central_widget = QWidget()
layout = QVBoxLayout()
central_widget.setLayout(layout)  # link them

# adding widgets
layout.addWidget(button1)
layout.addWidget(button2)

central_widget.show()
app.exec()  # application loop