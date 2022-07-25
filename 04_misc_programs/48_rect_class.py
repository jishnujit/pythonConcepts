# Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method
# which can compute the area.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def rect_area(self):
        area = self.length * self.width
        print(f"area of a rectangle with dimensions {self.length}cm x {self.width}cm is {area}cm**2")


obj = Rectangle(10, 10)
obj.rect_area()