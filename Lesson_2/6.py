"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
"""
import random
def z():
    def g(us, rel):
        m = 0
        if int(us) == rel:
            print("Угадал!")
            m = 1
        elif int(us) < rel:
            print("Больше")
        elif int(us) > rel:
            print("Меньше")
        return m
    a = input("Отгадай число от 0 до 100, играем? (0 - нет): ")
    if a == "0":
        print("BB")
    else:
        i = 0
        c = random.randint(0, 100)
        m = 0
        while i < 10 and m == 0:
            b = input("Предположения: ")
            m = g(b, c)
            i += 1
        print("Загаданное число - " + str(c))
        z()
z()











