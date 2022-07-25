class TooManyPagesReadError(ValueError):
    pass


class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self):
        return (
            f"<Book {self.name}, read {self.pages_read} pages out of {self.page_count}>"
        )

    def read(self, pages: int):
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesReadError(
                f"You have read {self.pages_read + pages} pages, but this book has only {self.page_count} pages"
            )
        self.pages_read += pages
        print(f"You have read {self.pages_read} pages out of {self.page_count}")


python101 = Book("Python 101", 50)
python101.read(20)  # without any error block - You have read 20 pages out of 50
python101.read(50)  # without any error block - You have read 70 pages out of 50
# we can create custom error to overcome this scenario. adding an if stmt that raises TooManyPagesReadError. If we don't
# create TooManyPagesReadError class by inheriting either Exception class or any other error like ValueError, TypeError
# we can even surround python101.read(20), python101.read(50) inside a try except block to get nice and user-friendly
# error message instead of all the tracebacks
