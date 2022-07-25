# Define a class named American which has a static method called printNationality.

class American:

    @staticmethod
    def print_nationality():
        print("this is a static method")

    @classmethod
    def class_method(cls):
        print("this is a class method")

    def instance_method(self):
        print("this is an instance method")


obj = American()
obj.print_nationality()
obj.instance_method()
obj.class_method()

American.print_nationality()
American.class_method()
American.instance_method()

