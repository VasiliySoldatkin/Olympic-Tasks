from math import ceil
k = int(input())
x = int(input())
y = int(input())
maxx = x + k - 1 # Максимальный вес пакета
sec = ceil(y / x)*x # Минимальный вес контейнера при минимальном весе пакета
if y%x == 0: #Исключение варианта, при котором можно уложить в контейнер пакеты минимального веса, т.е. по x кг
     print(y)
     exit()
if ceil(y / x) - 1 < ceil(y/maxx) : 
     print(sec)
else:
     print(y) # Случай, когда контейнер может состоять из пакетов максимального веса для получения min_weight 
