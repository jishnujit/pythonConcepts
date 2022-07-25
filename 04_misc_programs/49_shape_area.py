# Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as
# argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

class Shape:
    def area(self):
        print("0")


class Square(Shape):
    def __init__(self, length=0):
        Shape.__init__(self)
        self.length = length

    def area(self):
        square_area = self.length * self.length
        print(f"area of the square is {square_area}")


sq_obj = Square(10)
sq_obj.area()
Square().area()