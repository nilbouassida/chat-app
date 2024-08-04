import threading
import time

class myThread(threading.Thread):
    def __init__(self, iD, name):
        threading.Thread.__init__(self)
        self.iD = iD
        self.name = name

    def run():
        print(f'start {self.iD}')
        time.sleep(self.iD*3)
        print(f'beende {self.iD}')

t1 = myThread(1, "t1")
t2 = myThread(3, "t2")

t1.start()
t2.start()

print("beende")