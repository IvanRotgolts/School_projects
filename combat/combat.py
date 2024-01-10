class Enemy():
    """класс описывает противника"""
    def __init__(self, health, atack):
        self.health=health
        self.atack=atack

    def be_atack(self, atack):
        """Метод атаки"""
        self.health=self.health - atack

    
enemy_1=Enemy(100, 50)
enemy_2=Enemy(80, 25)

