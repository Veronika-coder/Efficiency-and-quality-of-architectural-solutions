class Square:
    def area(self, side):
        return side ** 2

class Circle:
    def area(self, radius):
        return 3.14 * radius ** 2

square = Square()
print("Area of square:", square.area(5))

circle = Circle()
print("Area of circle:", circle.area(3))
