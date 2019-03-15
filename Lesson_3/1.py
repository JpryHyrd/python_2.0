# 1.	В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

a = 2
b = 0
list = []
while True:
    for i in range(8):
        print("Числа, кратные " + str(a) + ": ", end = "")
        for g in range(100):
            if g < 100 and g > 1 and g % a == 0:
                print(g, end = " ")

        print()
        a += 1
    break
