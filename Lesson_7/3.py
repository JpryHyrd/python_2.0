"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""
print()
import random
def generation():
    m = random.randint(20, 100)
    b = (2 * m) + 1
    lst = []
    for i in range(b):
        a = random.randint(1, 100)
        if a not in lst:
            lst.append(a)
    if len(lst) % 2 == 0:
        del(lst[0])
    return lst


def medium(lst):
    print("Исходный массив: ")
    print(lst)
    a = int(len(lst) / 2 - 0.5)
    t = 0
    for i in range(len(lst)):
        c = 0
        ls1 = []
        ls2 = []
        for j in lst:
            if i > j:
                c += 1
                ls1.append(j)
            elif i < j:
                ls2.append(j)
        if c == a:
            t = i
            big = ls2
            small = ls1

#        Traceback (most recent call last):
#        File "3.py", line 58, in <module>
#        medium(generation())
#        File "3.py", line 51, in medium
#        print(small)
#        UnboundLocalError: local variable 'small' referenced before assignment

#Если не вставить это условие, то иногда выскакивает ошибка, описанная выше 
    if t == 0: 
        medium(generation())
        return " "

    print()
    print("Медиана массива - " + str(t))
    print()
    print("Числа, меньше медианы: ")
    print(small)
    print()
    print("Числа, больше медианы: ")
    print(big)            
#    print(len(big), len(small), len(lst))


medium(generation())
