# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.
def mat(s):
    if len(s) != 15:
        print("Error 4523643623")
    else:
        g = 0
        print("___________")
        print("|", end = "")
        for i in s:
            print(str(i) + "|", end = "")
            if g == 4:
                print()
                print("___________")
                print("|", end = "")
                g = 0
            else:
                g += 1
        r = 0
        for i in range(5):
            a = s[r]
            b = s[r + 5]
            c = s[r + 10]
            g = [a, b, c]
            m = min(g)
            print(str(m) + "|", end = "")
            r += 1
        print(" <= Минимальные числа в столбцах")
a = input("Введите 15 чисел матрици через пробел: ")
a = a.split()
g = 0
for i in a:
    a[g] = int(a[g])
    g += 1
mat(a)