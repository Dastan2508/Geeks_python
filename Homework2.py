
class Figure:
    unit = 'cm'

    def __init__(self):
        pass

    @classmethod
    def get_unit(self):
        return self.unit

    @classmethod
    def set_unit(self, new_unit):
        self.unit = new_unit



class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length  # Приватный атрибут

    def calculate_area(self):
        return self.__side_length ** 2

    def info(self):
        area = self.calculate_area()
        print(f"Square side length: {self.__side_length}{Figure.get_unit()}, area: {area}{Figure.get_unit()}")


class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length
        self.__width = width

    def calculate_area(self):
        return self.__length * self.__width

    def info(self):
        area = self.calculate_area()
        print(f"Rectangle length: {self.__length}{Figure.get_unit()}, width: {self.__width}{Figure.get_unit()}, area: {area}{Figure.get_unit()}")


if __name__ == "__main__":
    square1 = Square(5)
    square2 = Square(7)

    # Создание объектов прямоугольников
    rectangle1 = Rectangle(5, 8)
    rectangle2 = Rectangle(6, 9)
    rectangle3 = Rectangle(4, 10)

    figures = [square1, square2, rectangle1, rectangle2, rectangle3]

    for figure in figures:
        figure.info()
