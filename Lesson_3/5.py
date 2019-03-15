#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.


import random
a = []
for i in range(15):
    a.append(random.randrange(-10, 10))
print(a)

b = -300
for i in a:
    if i < 0 and i > b:
        b = i
print("Наибольшее отрицательное число в массиве:", b)




