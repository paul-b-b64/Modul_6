class Figure:
    sides_count = 0
    def __init__(self):
        self.__sides = [23]
        self.__color = [255, 255, 255] # по умолчанию фигура - белая
        self.filled = True



    def __is_valid_color(self, r, g, b):
        comp = True
        if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
            comp = False
        return comp

    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args):
        comp = False
        if len(args) == self.sides_count:
            for i in args:
                if isinstance(i, int) and i > 0:
                    comp = True
                else:
                    comp = False
        return comp

    def get_sides(self):
        return self.__sides

    def __len__(self):
        sum_ = sum(self.__sides)
        return sum_

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = [*new_sides]

class Circle(Figure):
    sides_count = 1

    def __init__(self, r, g, b, *new_sides):
        super().__init__()
        self.set_color(r, g, b)
        if len(new_sides) == self.sides_count:
            self.set_sides(*new_sides)
        else:
            self.set_sides(1)
        self.__radius = self.get_sides()[0]/3.14

    def get_square(self):
        square = (self.__radius ** 2) * 3.14
        return square


class Triangle(Figure):
    sides_count = 3

    def __init__(self, r, g, b, *new_sides):
        super().__init__()
        self.set_color(r, g, b)
        if len(new_sides) == self.sides_count:
            self.set_sides(*new_sides)
        else:
            self.set_sides(1, 1, 1)

class Cube(Figure):
    sides_count = 12

    def __init__(self, r, g, b, *new_sides):
        super().__init__()
        self.set_color(r, g, b)
        a = new_sides[0]
        self.set_sides(a, a, a, a, a, a, a, a, a, a, a, a)

        # if len(new_sides) == 1:
        #     self.set_sides(*new_sides)
        #     self.__sides = self.get_sides()
        #
        #     # self.set_sides(*new_sides)
        #     # self._super__sides = [new_sides] * 9
        # else:
        #     self._super__sides = [1] * 9
        # # a = self._super__sides
        # sides = self.get_sides()
        # self.sides_cube = []
        # if len(new_sides) == 1:
        #     self.set_sides(*new_sides)
        #     self.__sides = self.get_sides()
        #     for i in range(12):
        #         self.sides_cube[1] = new_sides
        #
        #     # self.set_sides(*new_sides)
        #     # self._super__sides = [new_sides] * 9
        # else:
        #     self._super__sides = [1] * 9
        # a = self._super__sides
        # sides = self.get_sides()




cub1 = Cube(200, 43, 23, 45)
print(cub1.get_sides())

