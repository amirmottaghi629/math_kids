import itertools as it
import random as random
from threading import Timer
s_y=0
s_n=0
timeout = 10
t = Timer(timeout, print, ['Sorry, times up'])
for each in range(10):
    t.start()
    x=random.randint(0,9)
    y=random.randint(0,9)
    z=x+y
    print('x'' +',y," = ",z)
    print("X=?")
    te=int(input())
    if te==x:
        print("yes")
        s_y+=1
    else:
        print("no")
        s_n+=1
    t.cancel()
print("yes = ",s_y)
print("no = ",s_n)