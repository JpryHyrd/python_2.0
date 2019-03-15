#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

import random
a = [5]
for i in range(10):
    c = random.randrange(10)
    if c not in a:
        a.append(c)
print(a)
b = -1
b1 = 777
c = 10
c1 = 777
r = 0
for i in a:
    if i > b:
        b = i
        b1 = r
    elif i < c:
        c = i
        c1 = r
    r += 1
a[b1] = c
a[c1] = b
print(a)










