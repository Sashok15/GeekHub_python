"""Створіть за допомогою класів та продемонструйте свою реалізацію шкільної бібліотеки.
(включіть фантазію)

"""


class Building(object):
    def __init__(self, name, area, location):
        self.name = name
        self.area = area
        self.location = location


class Library(Building):
    def __init__(self, name, area, location, category_books, visitor):
        super().__init__(name, area, location)
        self.category = category_books
        self.visitor = visitor

    def show_info(self):
        return self.name, self.area, self.location, self.category, self.visitor


school_lib = Library(name="Library of 29 school", area='50', location="Cherkassy, Shevchenko street 23",
                     category_books='fiction, school books, scintific books', visitor="student")
print(school_lib.show_info())
