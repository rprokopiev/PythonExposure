class Rectangle:

    def __init__(self, width, height=None) -> None:
        self.width = width
        self.height = height if height else width
        

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height
    
    def __add__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle((self.width) + (other.width), (self.height) + (other.height))
        raise TypeError

    def __sub__(self, other):
        if isinstance(other, Rectangle):
            a = 0
            b = 0
            if (self.width > other.width):
                a = (self.width - other.width)
            else:
                a = (other.width - self.width)
            if (self.height > other.height):
                b = (self.height - other.height)
            else:
                b = (other.height - self.height)
            return Rectangle(a, b)
        raise TypeError
    
    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        raise TypeError
    
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area() == other.area()
        raise TypeError
    
    def __le__(self, other):
        if isinstance(other, Rectangle):
            return self.area() == other.area() or self.area() < other.area()
        raise TypeError
    
    def __str__(self):
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

rect1 = Rectangle(4, 5)
rect2 = Rectangle(3, 3)

print(rect1)
print(rect2)

print(rect1.perimeter())
print(rect1.area())
print(rect2.perimeter())
print(rect2.area())

rect_sum = rect1 + rect2
rect_diff = rect1 - rect2

print(rect_sum)
print(rect_diff)

print(rect1 < rect2)
print(rect1 == rect2)
print(rect1 <= rect2)

print(repr(rect1))
print(repr(rect2))
        
