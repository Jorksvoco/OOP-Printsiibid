from abc import ABC, abstractmethod


class Shape(ABC):
    @property
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self._width = width
        self._height = height

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

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f"Width: {self._width}, Height: {self._height}"


class Square(Shape):
    def __init__(self, size):
        self._size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    @property
    def area(self):
        return self._size * self._size

    def __str__(self):
        return f"Size: {self._size}"


if __name__ == "__main__":
    r = Rectangle(2, 3)
    s = Square(5)

    print(r)
    print(s)
    print(f"Rectangle area: {r.area}")
    print(f"Square area: {s.area}")