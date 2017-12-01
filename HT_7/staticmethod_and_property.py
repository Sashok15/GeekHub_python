class Human(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Human.count += 1

    @staticmethod
    def change_properties():
        Cup.capacity = 5
        Cup.color = 'black'

    @staticmethod
    def count_instance():
        return Human.count


class Cup(object):
    __capacity = 0
    __color = 'white'

    @property
    def capacity(self):
        return self.__capacity

    @property
    def color(self):
        return self.__color

    @capacity.setter
    def capacity(self, value):
        self.__capacity = value

    @color.setter
    def color(self, value):
        self.__color = value

    @color.getter
    def color(self):
        return self.__color


h1 = Human('dima')
print(Human.count_instance())  # 1 instance

h2 = Human('max')
print(Human.count_instance())  # 2 instance

c1 = Cup
print(Cup.capacity)  # <property object at 0x037E1F30>
print(Cup.color)  # <property object at 0x037E1F00>

h1.change_properties()  # change capacity and color via setter in class Human
print(Cup.capacity)  # 5
print(Cup.color)  # black