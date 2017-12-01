import os
from config import folder_path, file_txt_path


class Calc(object):
    """ This class have four methods:

    mult_num - makes multiplication of two numbers
    add_num - makes add of two numbers
    sub_num - makes substraction of two numbers
    div_num - makes division of two numbers

    """
    last_result = None
    operation = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mult_num(self):
        self.last_result = self.x * self.y
        self.operation = " * "
        return self.last_result

    def add_num(self):
        self.last_result = self.x + self.y
        self.operation = " + "
        return self.last_result

    def sub_num(self):
        self.last_result = self.x - self.y
        self.operation = " - "
        return self.last_result

    def div_num(self):
        self.last_result = self.x / self.y
        self.operation = " / "
        return self.last_result

    def add_result_in_file(self):
        if self.last_result:
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            with open(file_txt_path, 'a') as f:
                result_in_file = str(self.x) + str(self.operation) + \
                                 str(self.y) + " = " + str(self.last_result)+'\n'
                print(result_in_file)
                f.write(result_in_file)
        else:
            return None


calc = Calc(13, -4)

calc.add_num()
calc.add_result_in_file()
calc.div_num()
calc.add_result_in_file()
calc.sub_num()
calc.add_result_in_file()
calc.mult_num()
calc.add_result_in_file()