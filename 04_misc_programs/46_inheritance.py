# Define a class named American and its subclass NewYorker.
class American:

    def __init__(self):
        print("Inside parent class")


class NewYorker(American):

    def __init__(self):
        super().__init__()
        print("Inside child class")


child_obj = NewYorker()
