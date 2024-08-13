class Figure:
    sides_count = 0

    def __init__(self):
        self.__sides = []
        self.__color = [255, 255, 255]  # по умолчанию фигура - белая
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
        self.__radius = self.get_sides()[0] / 3.14

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
        self.__height = [(self.get_square() * 2) / self.get_sides()[0] # высот в треугольнике три:
            , (self.get_square() * 2) / self.get_sides()[1]            # перпендикулярны каждой из сторон
            , (self.get_square() * 2) / self.get_sides()[2]]

    def get_square(self):
        half_perimeter = sum(self.get_sides()) / 2
        square = (half_perimeter
                  * (half_perimeter - self.get_sides()[0])
                  * (half_perimeter - self.get_sides()[1])
                  * (half_perimeter - self.get_sides()[2])) ** 0.5
        return square

    # def get_height(self):
    #     return self.__height

class Cube(Figure):
    sides_count = 12

    def __init__(self, r, g, b, *new_sides):
        super().__init__()
        self.set_color(r, g, b)
        if len(new_sides) == 1:
            a = new_sides[0]
            self.set_sides(a, a, a, a, a, a, a, a, a, a, a, a)
        else:
            self.set_sides(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)

    def get_volume(self):
        volume = self.get_sides()[0] ** 3
        return volume


circle1 = Circle(200, 200, 100, 10) # (Цвет, стороны)
cube1 = Cube(222, 35, 130, 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())


