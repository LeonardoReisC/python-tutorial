# PySide6: used to build user interfaces
# https://doc.qt.io/qtforpython-6/

from PySide6.QtWidgets import QApplication, QPushButton

# creates the main application
app = QApplication()

# creates a button
button1 = QPushButton('Button Text')
button1.setStyleSheet('font-size: 40px; color: red;')  # qss
button1.show()  # add the widget and display on the window

button2 = QPushButton('Button Text')
button2.show()  # add it in a new window

app.exec()  # application loop