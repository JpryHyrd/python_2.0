"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""

import random
def generation():
    dd = []
    a = []
    b = []
    for i in range(20):
        a.append(random.randint(0, 48))
    for i in range(20):
        b.append(random.randint(1, 99))
    r = 0
    for i in a:
        v = float(i)
        c = b[r] / 100
        dd.append(v + c)
        r += 1
    return dd

def merge_sort(orig_list):
    if len(orig_list) > 1:
        center = len(orig_list) // 2
        left = orig_list[:center]
        right = orig_list[center:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                orig_list[k] = left[i]
                i += 1
            else:
                orig_list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            orig_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            orig_list[k] = right[j]
            j += 1
            k += 1
        return orig_list

lst = generation()
print("Исходный массив: ")
print(lst)
print("Массив после сортировки: ")
print(merge_sort(lst))






