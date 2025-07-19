import threading
import time
def asd():
    time.sleep(2.33)
    print("asd")
def dsa():
    time.sleep(1.9)
    print("dsa")
t= threading.Thread(target=asd)
t1= threading.Thread(target=dsa)
t.start()
t1.start()