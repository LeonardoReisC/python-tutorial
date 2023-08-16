import time

from PySide6.QtCore import QObject, Signal, QThread
from PySide6.QtWidgets import QApplication, QWidget

from workerUI import Ui_MyWidget


class Worker1(QObject):
    started = Signal(str)
    progressed = Signal(str)
    finished = Signal(str)

    def run(self):
        value = '0'
        self.started.emit(value)
        for i in range(5):
            value = str(i)
            self.progressed.emit(value)
            time.sleep(.5)
        self.finished.emit(value)


class MyWidget(QWidget, Ui_MyWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.button1.clicked.connect(self.hardWork1)
        self.button2.clicked.connect(self.hardWork2)

    def hardWork1(self):
        self._worker = Worker1()
        self._thread = QThread()

        worker = self._worker
        thread = self._thread

        # move worker to thread
        worker.moveToThread(thread)

        # run
        thread.started.connect(worker.run)
        worker.finished.connect(thread.quit)

        thread.finished.connect(thread.deleteLater)  # clear memory
        worker.finished.connect(worker.deleteLater)  # clear memory

        worker.started.connect(self.worker1Started)
        worker.progressed.connect(self.worker1Progressed)
        worker.finished.connect(self.worker1Finished)

        thread.start()

    def worker1Started(self, value):
        self.button1.setDisabled(True)

        self.label1.setText(value)

    def worker1Progressed(self, value):
        self.label1.setText(value)

    def worker1Finished(self, value):
        self.button1.setDisabled(False)
        self.label1.setText(value)

    def hardWork2(self):
        self._worker2 = Worker1()
        self._thread2 = QThread()

        worker = self._worker2
        thread = self._thread2

        # move worker to thread
        worker.moveToThread(thread)

        # run
        thread.started.connect(worker.run)
        worker.finished.connect(thread.quit)

        thread.finished.connect(thread.deleteLater)  # clear memory
        worker.finished.connect(worker.deleteLater)  # clear memory

        worker.started.connect(self.worker2Started)
        worker.progressed.connect(self.worker2Progressed)
        worker.finished.connect(self.worker2Finished)

        thread.start()

    def worker2Started(self, value):
        self.button2.setDisabled(True)

        self.label2.setText(value)

    def worker2Progressed(self, value):
        self.label2.setText(value)

    def worker2Finished(self, value):
        self.button2.setDisabled(False)
        self.label2.setText(value)


if __name__ == '__main__':
    app = QApplication()
    widget = MyWidget()

    widget.show()
    app.exec()
