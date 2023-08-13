from time import sleep

from threading import Thread


def wait(text, time):
    sleep(time)
    print(text)


t1 = Thread(target=wait, args=('Hello World! 1', 3))
t1.start()

# same as t1.join()
while t1.is_alive():
    print('Loading...')
    sleep(2)
