class House:
    def __init__(self,year,colour,number,floors):
        self.year=year
        self.colour=colour
        self.number=number
        self.floors=floors
        self.open_window()
    def show_info(self):
        print(self.year,self.colour,self.number,self.floors)

    def open_window(self):
        print("Openning a window")
    def switch_in_light(self):
        print("Switching on light...")

house_1=House(1937,"red", 12, 7)
house_1.show_info()
house_2=House(2009,"white", 88, 6)
house_2.show_info()
house_2.switch_in_light()

House(year=1747,colour="orange",number=86,floors=8).open_window()