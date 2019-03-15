"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
import random
a = []
for i in range(10):
    c = random.randrange(10)
    if c not in a:
        a.append(c)
print(a)
b = max(a)
b1 = a.index(b)
c = min(a)
c1 = a.index(c)

g = 0
if b1 < c1:
    for i in a[b1 + 1:c1]:
        g += i
elif b1 > c1:
    for i in a[c1 + 1:b1]:
        g += i

print("Cумма элеметов между большим и меньшим числами равна", g)

