class Shape:
    def calculate_area(self):
        pass

class Circle(Shape):
    def calculate_area(self):
        radius = float(input("Enter the radius of the circle: "))
        return 3.14 * radius * radius

class Rectangle(Shape):
    def calculate_area(self):
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        return length * width

class Triangle(Shape):
    def calculate_area(self):
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        return 0.5 * base * height

shape_type = input("Enter the type of shape (circle, rectangle, triangle): ")

if shape_type == "circle":
    shape = Circle()
elif shape_type == "rectangle":
    shape = Rectangle()
elif shape_type == "triangle":
    shape = Triangle()
else:
    print("Invalid shape type entered.")
    exit()

area = shape.calculate_area()
print("Area:", area)
