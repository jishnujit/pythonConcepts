'''
> self refers to itself, i.e. when an object is created, and when we call the methods inside the class, the object
  in turn takes self and all the assignments inside the methods happens through the self to object
'''
class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def mul(self):
        return self.x * self.y


calc = Calculator(10, 20)
print(calc.add())
print(calc.mul())
calc1 = Calculator(5, 6)
print(calc1.add())
print(calc1.mul())

