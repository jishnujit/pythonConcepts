'''
> Composition is counterpart to inheritance to build out classes to use other classes.
> In python, you are going to be using inheritance very little
> It allows classes to be simpler and allows to reduce the complexity of the code overall. Recommended
> See example below on how to use composition instead of inheritance
> Inheritance means a book is a bookshelf while composition means a bookshelf has many books
'''


class BookShelf:
    def __init__(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return f"BookShelf with {self.quantity} books"


shelf = BookShelf(200)
# print(shelf)

class Book(BookShelf):
    def __init__(self, name, quantity):
        '''
        For book class qty is not needed but if we want to invoke super class cons we need quantity here. We
        consider Book should be inherited from BookShelf as in real world, books are kept in bookshelf. So we inherit.
        Is there a way to overcome this? And it can be done through class composition
        Conceptually we say all books are bookshelves like when we say all animals are mammals
        Since actually we don't need inheritance here we can use class composition (since quantity is not needed in
        Book class and __str__ method overrides the __str__ method in the parent class. So we don't use any property of
        BookShelf class in Book class, i.e. there is no reason to inherit ig you are not gonna use that inheritance
        anywhere.). So this is where composition comes in. Composition is for when you wanna say something like a
        bookshelf has many books, i.e. a bookshelf is composed of many things and books


        '''
        super().__init__(quantity)
        self.name = name

    def __str__(self):
        return f"Book {self.name}"


book = Book("Harry Potter", 120)
print(book)  # prints - Book Harry Potter

print("===========================================================================================================")

# changing the above code in below way


class BookShelfNew:
    '''
    changing quantity to *books
    this will take a bunch ok book objects. Book class doesn't need to inherit from the BookShelf and so it doesn't
    need quantity or any super class. Now we have two simple classes. Now we can create 2 books and create a
    bookshelf and give it 2 books
    '''
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books."


class BookNew:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"


booknew1 = BookNew("Harry Potter")
booknew2 = BookNew("Python 101")
bookshelf = BookShelfNew(booknew1, booknew2)  # BookShelf with 2 books.
print(bookshelf)