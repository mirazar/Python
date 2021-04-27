from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def consumption(self):
        return self.size / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def consumption(self):
        return self.height * 2 + 0.3


coat = Coat(400)
print(coat.consumption)

costume = Costume(55)
print(costume.consumption)
