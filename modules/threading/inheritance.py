# created threads by class inheritance
import time

from threading import Thread


class MyThread(Thread):
    def __init__(self, text, time) -> None:
        self.text = text
        self.time = time

        super().__init__()

    def run(self):
        time.sleep(self.time)
        print(self.text)


t1 = MyThread('Thread 1', 5)
t1.start()

t2 = MyThread('Thread 2', 3)
t2.start()

t3 = MyThread('Thread 3', 2)
t3.start()

for i in range(10):
    print(i)
    time.sleep(1)