# sử dụng hướng đối tượng xây con mèo nha Anh Lực
# Anh không rõ nên thêm method gì nên tạo random nha, anh dùng inheritance trong class Animal với class Cat để inherit method với attributes của nó
class Animal():
    def __init__(self,weight,color,name):
        self.name = name
        self.weight = weight
        self.color = color
    pass

    def Print_info(self):
        print (f"Name: {self.name}")
        print (f"Color: {self.color}")
        print(f"Weight: {self.weight}")

    def Say_something(self):
        print('Each animal makes different sound')

    def Ability(self):
        print('Animals have unique ability that disinguish themselves')

class Cat(Animal):
    def __init__(self,weight,color,name):
        super().__init__(weight,color,name)
        self.type_animal = "Cat"
    pass

    def Say_something(self):
        print(f"{self.name} says 'Meow Meow'")

    def Ability(self):
        print(f"{self.name} can climb tree and fall on his/her feet")
