class BaseAnimal:

    def __init__(self, name, feature = None):
        self.name = name
        self.feature = feature
    

    def get_name(self):
        return self.name
    

    def get_feature(self):
        return self.feature


class Bird(BaseAnimal):

    def __init__(self, name, feature=None):
        super().__init__(name, feature)


class Fish(BaseAnimal):

    def __init__(self, name, feature=None):
        super().__init__(name, feature)


class Dog(BaseAnimal):

    def __init__(self, name, feature=None):
        super().__init__(name, feature)
