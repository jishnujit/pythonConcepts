'''
> methods with 2 underscores on either side of method name is called magic methods, because python will call them for u
  in some situations. For e.g. python calls the __init__() method when an object of class is created and execute the code
  inside the __init__() method
> When we print the object(there is no str or repr methods defined) it prints out the physical loc of the object.
  Instead of print a default string we can make it print a nice string using __str__ method.
> __str__(self) gets called when you want to turn your object into a string. Representation of an object from user perspective
> __repr__(self) goal of this method is to be unambiguous, and if possible it should return a string that allows us to
  recreate original object very easily. i.e. it is the representation of an object from developer perspective
> __str__ method shadows __repr__ method. _str_ method gets printed
> They are used for representing an object
'''


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person {self.name} is {self.age} years old"

    def __repr__(self):
        return f"<Person('{self.name}', {self.age})>"


pers = Person("Bob",35)
print(pers)

items = []
item = {"name":"Bob", "age": 35}
item2 = {"name":"Zia", "age": 28}
items.append(item)
print(items)
items.append(item2)
print(items)
print(sum(item["age"] for item in items))