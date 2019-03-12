"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
"""
def operations():
    def num(position):
        global answer
        answer = input("Введите {} число: " .format(position))
        return answer
    def oper():
        global operation
        operation = input("Введите операцию(+ - * /): ")
        if operation != "+" and operation != "-" and operation != "*" and operation != "/":
            print("Неверный знак операции!")
            oper()
    answer = input("Для выхода введите 0: ")
    if answer == "0":
        print("BB")
    else:
        first = num(1)
        second = num(2)
        oper()
        if operation == "-":
            print(first, operation, second, "=", int(first) - int(second))
            operations()
        elif operation == "+":
            print(first, operation, second, "=", int(first) + int(second))
            operations()
        elif operation == "*":
            print(first, operation, second, "=", str(int(first) * int(second)))
            operations()
        elif operation == "/":
            print(first, operation, second, "=", int(first) / int(second))
            operations()

operations()