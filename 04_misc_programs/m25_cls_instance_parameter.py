# Define a class, which have a class parameter and have a same instance parameter.
# Define an instance parameter, need add it in __init__ method.You can init an object with construct parameter
# or set the value later

class Car:
    name = "Car"

    def __init__(self, name=None):
        self.name = name


honda = Car("Honda City")
print("My %s name is %s" % (Car.name, honda.name))

tata = Car()
tata.name = "Tata Nexon"
print(f"My {Car.name} name is {tata.name}")
