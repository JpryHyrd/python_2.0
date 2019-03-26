"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""
from pympler import asizeof

#Памяти выделено - 456
class Critter(object):
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1
    @property
    def mood(self):
        unhappines = self.hunger + self.boredom
        if unhappines < 5:
            m = "Very good"
        elif 5 <= unhappines <= 10:
            m = "Good"
        elif 11 <= unhappines <= 15:
            m = "Not bad"
        else:
            m = "Bad"
        return m
    def talk(self):
        print("My name - " + self.name + "\nMy state of health - " + self.mood)
    def eat(self, food = 4):
        print("Thanks!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()
    def play(self, fun = 4):
        print("Yaaaaa!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()
a = Critter("Anthon")
a.talk()
a.eat()
a.play()
a.talk()
print()
print(a.__dict__)
print("\n\n")
#Памяти выделено - 184
class Critter2(object):
    __slots__ = ["name", "hunger", "boredom"]
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1
    @property
    def mood(self):
        unhappines = self.hunger + self.boredom
        if unhappines < 5:
            m = "Very good"
        elif 5 <= unhappines <= 10:
            m = "Good"
        elif 11 <= unhappines <= 15:
            m = "Not bad"
        else:
            m = "Bad"
        return m
    def talk(self):
        print("My name - " + self.name + "\nMy state of health - " + self.mood)
    def eat(self, food = 4):
        print("Thanks!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()
    def play(self, fun = 4):
        print("Yaaaaa!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

b = Critter2("Anthon")
b.talk()
b.eat()
b.play()
b.talk()
print()
print(b.__slots__)
print()
print(asizeof.asizesof(a))
print(asizeof.asizesof(b))

#Вывод: при использовании слотов, класс занимает в 2.5 раза меньше памяти(в данном случае)

#______________________________________________________________________
def main():
    crit_name = input("Critter name: ")
    crit = Critter(crit_name)

    choice = None
    while choice != "0":
        print("""
        0 - Go out
        1 - Health
        2 - Feed
        3 - Play
        """)
        choice = input("Your choice: ")
        print()
        if choice == "0":
            print("Good by!")
        elif choice == "1":
            crit.talk()
        elif choice == "2":
            crit.eat()
        elif choice == "3":
            crit.play()
        else:
            print("Error!!! Type your choice again!")
#main()




