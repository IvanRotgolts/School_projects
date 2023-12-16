class Transport():
    """Описание транспорта"""
    def __init__(self, colour, speed, passangers):
        self.colour=colour
        self.speed=speed
        self.passangers=passangers

    def __str__(self):
        return f"type:{self.type}"

    def show_info(self):
        print(self.colour,self.speed,self.passangers)

    def start(self):
        """Запускает двигатель"""
        print("Start engine")

    def stop(self):
        """Останавливает двигатель"""
        print("Stop engine")

class Train(Transport):
    def __init__(self, colour, speed, passangers, length):
        super().__init__(colour, speed, passangers)
        self.length=length

    def bell(self):
        print("Позвонить в звонок")

train=Train("blue", "80", 200, 500)
train.start()
train.bell()