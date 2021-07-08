# Liskov Substitution Principle
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height

    def __str__(self) -> str:
        return f'Width : {self._width} Height: {self._height}'

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


class Square(Rectangle):
    def __init__(self, width):
        super().__init__(width, width)

    @Rectangle.width.setter
    def width(self, width):
        self._width = self._height = width

    @Rectangle.height.setter
    def height(self, height):
        self._height = self._width = height


def use_it(rc: Rectangle):
    w = rc.width
    rc.height = 10
    expected = w * 10
    print(f'Expected area of {expected}, got {rc.area}')


rc = Rectangle(3, 2)
use_it(rc=rc)

# Take parameter is_square in rectangle class another solution
sq = Square(5)
use_it(sq)
