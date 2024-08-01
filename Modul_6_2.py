class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    # new_color = 'vek'

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = 'Toyota Mark II'
        self.__engine_power = 500
        self.__color = 'blue'

    def get_model(self):
        print(f'Модель: {self.__model}')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        print(f'Цвет: {self.__color}')

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        self.new_color = new_color
        if self.new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = self.new_color
        else:
            print(f'Нельзя сменить цвет на {self.new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


if __name__ == '__main__':

    vehicle1 = Sedan('Fedos', 'blb', 'dfl', 33)
    vehicle1.print_info()
    vehicle1.set_color('Pink')
    vehicle1.set_color('BLACK')
    vehicle1.owner = 'Vasyok'
    vehicle1.print_info()












