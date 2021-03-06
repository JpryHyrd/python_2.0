"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""
import random

def bubble_sort(orig_list):
    n = 1
    while n < len(orig_list):
        for i in range(len(orig_list)-n):
            if orig_list[i] < orig_list[i+1]:
                orig_list[i],orig_list[i+1] = orig_list[i+1],orig_list[i]
        n += 1
    return orig_list

orig_list = [random.randint(-100, 100) for _ in range(20)]
print("Исходный массив: ", end = "")
print(orig_list)
print("Массив после сортировки: ", end = "")
print(bubble_sort(orig_list))









