class Rectangle:
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
    
    def __str__ (self):
         return f"Width: {self._width}, Height: {self._height}"
 
 
class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)
 
    @Rectangle.width.setter
    def width(self, value):
        self._width = value
        self._height = value
 
    @Rectangle.height.setter
    def height(self, value):
        self._width = value
        self._height = value
 
 
def use_shape(shape):
    saved_width = shape.width
    shape.height = 10
    expected_area = saved_width * 10
    actual_area = shape.area
    print(f"Expected area: {expected_area}")
    print(f"Actual area: {actual_area}")

r = Rectangle(2, 3)
use_shape(r)

s = Square(5)
use_shape(s) 

    
    


