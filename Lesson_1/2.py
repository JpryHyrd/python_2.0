# 2. Выполнить логические побитовые операции "И", "ИЛИ" и др.
# над числами 5 и 6. Выполнить
# над числом 5 побитовый сдвиг вправо и влево на два знака.
"""
5^10 = 101^2
6^10 = 110^2
"""
a = "101"
b = "110"
c = ""
i = 0
#Побитовое И
for g in range(1000):
    if len(c) == len(a):
        print("Побитовое И чисел {} и {} равно {}" .format(a, b, c))
        break
    elif a[i] != "0" and b[i] != "0":
        c += "1"
    else:
        c += "0"
    i += 1

#Побитовое ИЛИ
i = 0
c = ""
for g in range(1000):
    if len(c) == len(a):
        print("Побитовое ИЛИ чисел {} и {} равно {}" .format(a, b, c))
        break
    elif a[i] != "0" or b[i] != "0":
        c += "1"
    else:
        c += "0"
    i += 1

#Побитовый сдвиг вправо
r = "00"
r += a
print("Побитовый сдвиг вправо числа 5", r)
#Побитовый сдвиг влево
a += "00"
print("Побитовый сдвиг влево числа 5", a)
        



