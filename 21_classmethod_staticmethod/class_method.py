'''
In this class Book, when we create an object, it takes 3 params - name, book_type and weight. The user can give any text
when he instantiates an object for types but for us we have only 2 types, i.e hardcover and paperback.
We can make sure that we don't accept any other arguments for book type by defining classmethods, i.e. one for hardcover
and another for paperback. When calling these class methods, it creates an object of the class and in turn calls
__init__ method and since we have defined __repr__ method, it by default prints the object to us.
'''
class Book:
    types =("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, weight):
        return cls(name, cls.types[0], weight+100)  # we can use classname instead of cls in this stmt. prefer 'cls'

    @classmethod
    def paperback(cls, name, weight):
        return cls(name, cls.types[0], weight)


book = Book.hardcover("Harry Potter", 1500)  # we don't need an obj to call classmethods. can be called with clsname
light = Book.paperback("Python 101", 600)  # when we call hardcover, it in turn creates Obj of book which calls init
print(book)
print(light)
