'''
Создайте класс-фабрику.
○ Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
○ Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
'''
import animals as a

class Fabric:

    def __init__(self, name, feature):
        self.animal = a.BaseAnimal(name, feature)
        self.name = self.animal.get_name()
        self.feature = self.animal.get_feature()

    def get_name(self):
        return self.name
    
    def get_feature(self):
        return self.feature

animal1 = Fabric('Ворона', 'Неперелётная')
print(animal1.get_name())
print(animal1.get_feature())
