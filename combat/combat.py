import time
import random

class Enemy():
    """класс описывает противника"""
    def __init__(self, health, atack):
        self.health=health
        self.atack=atack

    def be_atack(self, atack):
        """Метод атаки"""
        self.health=self.health - atack




enemy_1=Enemy(random.randint(80, 100), random.randint(20, 100))
enemy_2=Enemy(random.randint(80, 100), random.randint(20,100))

#Игровой цикл
while True:
    enemy_1.be_atack(enemy_2.atack)
    enemy_2.be_atack(enemy_1.atack)

    if enemy_2.health <= 0 and enemy_1.health <= 0:
        print("Ничья")
        print(f"У игрока два осталось {enemy_2.health} здоровья")
        print(f"У игрока два осталось {enemy_1.health} здоровья")
        print(enemy_1.atack, enemy_2.atack)
        break

    if enemy_1.health<0:
        print("Выиграл игрок #2")
        print(f"У игрока два осталось {enemy_2.health} здоровья")
        break

        
    if enemy_2.health<0:
        print("Выиграл игрок #1")
        print(f"У игрока два осталось {enemy_1.health} здоровья")
        break

    print(enemy_1.health, enemy_2.health)
    print(enemy_1.atack, enemy_2.atack)
    time.sleep(0.5)
