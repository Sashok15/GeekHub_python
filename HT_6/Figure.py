"""Напишіть програму, де клас «геометричні фігури» (figure) містить властивість color з початковим значенням white
і метод для зміни кольору фігури, а його підкласи «овал» (oval) і «квадрат» (square) містять методи __init__
для завдання початкових розмірів об'єктів при їх створенні.

Видозмініть програму так, щоб метод __init__ мався в класі «геометричні фігури»
та приймав кольор фігури при створенні екземпляру, а методи __init__ підкласів доповнювали його
та додавали початкові розміри.

"""


class Figure(object):
    def __init__(self, color):
        self.color = color

    def change_color(self, color):
        self.color = color
        return color


class Oval(Figure):
    def __init__(self, large_axis, small_axis):
        Figure.__init__(self, color='Red')
        self.large_axis = large_axis
        self.small_axis = small_axis

    def show_all_info(self):
        return self.large_axis, self.small_axis, self.color


class Square(Figure):
    def __init__(self, side):
        Figure.__init__(self, color="Blue")
        self.side = side

    def show_all_info(self):
        return self.side,  self.color

# example for instance of class Oval
figure_1 = Oval(large_axis=50, small_axis=30)

print(figure_1.show_all_info())  # (50, 30, 'Red')

figure_1.change_color("white")
print(figure_1.show_all_info())  # (50, 30, 'white')

# example for instance of class Square
figure_2 = Square(side=10)

print(figure_2.show_all_info())  # (10, 'Blue')

figure_2.change_color("Black")
print(figure_2.show_all_info())  # (10, 'Black')

