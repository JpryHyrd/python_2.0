# 4.	Определить, какое число в массиве встречается чаще всего.
import random
a = []
g = 50
for i in range(g):
    a.append(random.randrange(10))
print(a)
b = 0
c = 0
r = 0
for i in range(10):
    for f in a:
        if i == f:
            b += 1
    if b > r:
        r = b
        c = i
    b = 0
print("Самое часто встерчаемое число в данном массиве -", c)

