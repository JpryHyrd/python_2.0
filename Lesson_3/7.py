"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""
import random
a = []
for i in range(7):
    a.append(random.randrange(10))
print(a)

g = 100
b = 110
p = 0
for i in a:
    if i < g:
        if g < b:
            b = g
        g = i
    elif i < b:
        b = i
print(g, b)
    


