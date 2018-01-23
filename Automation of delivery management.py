from math import ceil
k = int(input())
x = int(input())
y = int(input())
maxx = x + k - 1
sec = ceil(y / x)*x
if y%x == 0:
     print(y)
     exit()
if ceil(y / x) - 1 < ceil(y/maxx) :
     print(sec)
else:
     print(y)
