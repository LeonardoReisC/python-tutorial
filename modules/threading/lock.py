from time import sleep

from threading import Thread
from threading import Lock


class Tickets():
    def __init__(self, storage) -> None:
        self.storage = storage
        self.lock = Lock()

    def buy(self, qty):
        self.lock.acquire()  # locks access to exclusive

        if self.storage < qty:
            print("Sorry, but we don't have enough tickets to sell")
            self.lock.release()
            return

        sleep(1)  # problem starts here

        self.storage -= qty
        print(f"You bought {qty} ticket(s).\n\tRemaining: {self.storage}")

        self.lock.release()


tickets = Tickets(10)

for i in range(1, 10):
    t1 = Thread(target=tickets.buy, args=(i,))
    t1.start()
