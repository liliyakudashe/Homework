import threading
import time


def numbers():
    for i in range(1, 11):
        print(i)
        time.sleep(1)


def letters():
    for i in 'abcdefghij':
        print(i)
        time.sleep(1)


t1 = threading.Thread(target=numbers())
t2 = threading.Thread(target=letters())

t1.start()
t2.start()

t1.join()
t2.join()
