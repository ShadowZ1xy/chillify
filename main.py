from threading import Timer

import win32api

mbox = win32api.MessageBox(0, 'hello', 'title')
mbox.close()


def test():
    print("hello")


def close():
    mbox.close()


while True:
    b = Timer(4, close)
    b.run()
