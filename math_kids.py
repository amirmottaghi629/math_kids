import itertools as it
import random as random
s_y=0
s_n=0
for each in range(10):
    x=random.randint(0,9)
    y=random.randint(0,9)
    z=x+y
    print('x'' +',y," = ",z)
    print("X=?")
    t=int(input())
    if t==x:
        print("yes")
        s_y+=1
    else:
        print("no")
        s_n+=1
print("yes = ",s_y)
print("no = ",s_n)