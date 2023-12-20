class Animal():
    """Описание животного"""
    def __init__(self, food, speed, colour):
        self.colour=colour
        self.speed=speed
        self.food=food

    def breath(self):
        print("Дышать")

class Deer(Animal):
    """Описание оленя"""
    def __init__(self, size_horns, food, speed, colour):
        super().__init__(food, speed, colour)
        self.size_horns=size_horns
        self.has_horns=True

    def eating_grass(self):
        print("Eating grass...")

class Lion(Animal):
    """Описание льва"""
    def __init__(self, food, speed, colour, size_mane):
        super().__init__(food, speed, colour)
        self.size_mane=size_mane

    def hunting(self):
        """Охота"""
        print("Охота")

deer=Deer("big horns", "grass", "20", "brown")
print(deer.has_horns)
print(deer.size_horns)
deer.eating_grass()
deer.breath()

lion=Lion("meet", "40", "beige", "big mane")
lion.hunting()
lion.breath()

        