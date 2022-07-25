# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also, please include simple test function to test the class methods.

class Upper:

    def __init__(self):
        self.text = None

    def get_string(self):
        self.text = input("Please enter any string: ")

    def print_upper(self):
        print(f"text in uppercase - {self.text.upper()}")


obj = Upper()
obj.get_string()
obj.print_upper()
