class Warrior():

    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color

    def sleep(self):
        print(f"{self.name} лёг спать")
        self.endurance +=2

    def eat(self):
        print(f"{self.name} сел кушать")
        self.power +=1

    def hit(self):
        print(f"{self.name} наносит удар")
        self.endurance -=1

    def run(self):
        print(f"{self.name} бежит")
        self.endurance -=1

    def info(self):
        print(f"Имя воина - {self.name}")
        print(f"Сила воина - {self.power}")
        print(f"Выносливость - {self.endurance}")
        print(f"Цвет волос - {self.hair_color}")

    