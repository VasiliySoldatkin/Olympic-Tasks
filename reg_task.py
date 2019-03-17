a = int(input())
b = int(input())
c = int(input())

first = a + c - (a+c) % c    # Нахожу первый элемент последовательность, делящийся на c
second = b - (b-c) % c       # Нахожу последний элемент последовательность, делящийся на c
groups = (second - first)//c    # кол-во групп по (с-1) элементов на отрезке [first;second]

jumps = (c - 1) // 2            # Кол-во "прыжков" в одной группе на отрезке [first;second]
jump_first = (first-a)//2       # Кол-во "прыжков" на отрезке [a;first]
jump_second = (b-second)//2     # Кол-во "прыжков" на отрезке [second;b]

"""print('first ',first)
print('second ', second)
print('groups ', groups)
print('first_jump ', jump_first)
print('sec_jump ', jump_second)"""

if first > b and second < a: # Если на отрезке [a;b] нет чисел, делящихся на c
    print((b-a+1) // 2)
else:
    print(groups*jumps + jump_first + jump_second + (groups+1))     # (groups+1) - это кол-во прыжков между группами


