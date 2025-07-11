class Shape:
    def __init__(self, colour, filled,):
        self.colour = colour
        self.filled = filled
        
    def describe(self):
        print(f"It is {self.colour} and {'filled' if self.filled is True else 'not filled'}")

class Circle(Shape):
    def __init__(self, colour, filled, radius):
        super().__init__(colour, filled)
        self.radius = radius
        
    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}cm^2")
        super().describe()

class Square(Shape):
    def __init__(self, colour, filled, width):
        super().__init__(colour, filled)
        self.width = width
        
    def describe(self):
        print(f"It is a square with an area of {self.width * self.width}cm^2")
        super().describe()

class Triangle(Shape):
    def __init__(self, colour, filled, width, height):
        super().__init__(colour, filled)
        self.width = width
        self.height = height
    def describe(self):
        print(f"It is a triangle with an area of { self.width * self.height / 2  }cm^2")
        super().describe()
        
        
circle = Circle("red", True, 5)
print(circle.colour)
print(circle.filled)
print(circle.radius)
circle.describe()
square = Square("Blue",False,6)
print(square.colour)
print(square.filled)
print(square.width)
square.describe()
triangle = Triangle("green",True,7,8)
print(triangle.colour)
print(triangle.width)
print(triangle.height)
print(triangle.filled)
triangle.describe()


