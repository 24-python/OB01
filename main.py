class Warrior():

    # ЗАДАНИЕ СВОЙСТВ КЛАССА "ВОИН"

    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color
    # ЗАДАНИЕ МЕТОДОВ КЛАССА "ВОИН"

    def sleep(self):
        print(f"{self.name} лег спать")
        self.endurance += 2
    def eat(self):
        print(f"{self.name} ест")
        self.power += 2

    def hit(self):
        print(f"{self.name} наносит удар")
        self.endurance -= 6

    def walk(self):
        print(f"{self.name} гуляет")

    def info(self):
        print(f"Имя: {self.name}")
        print(f"Сила: {self.power}")
        print(f"Выносливость: {self.endurance}")
        print(f"Цвет волос: {self.hair_color}")

war1 = Warrior("Степан", 10, 10, "черный")
war2 = Warrior("Иван", 27, 6, "коричныевй")

print(war1.endurance)
print(war1.power)

war1.sleep()
war1.eat()
war1.hit()

print(war1.endurance)
print(war1.power)






