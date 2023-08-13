# created threads by passing arguments
from time import sleep

from threading import Thread


def wait(text, time):
    sleep(time)
    print(text)


t1 = Thread(target=wait, args=('Hello World! 1', 5))
t1.start()

t2 = Thread(target=wait, args=('Hello World! 2', 1))
t2.start()

t3 = Thread(target=wait, args=('Hello World! 3', 2))
t3.start()

for i in range(10):
    print(i)
    sleep(1)