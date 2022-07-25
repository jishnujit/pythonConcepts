'''
> instance methods- When you wanna produce an action that uses the data inside the object that u created earlier on. or
  if you wanna call a method for modifying some data inside self or the object
> Class methods - are often used as factories
> Static methods - used to just place a method inside a class.
> Most of the time u will be using class method and instance method while static method is not used much
'''


class ClassTest:

    def instance_method(self):
        print(f"called instance method of {self}")

    @classmethod
    def class_method(cls):
        print(f"called class method of {cls}")

    @staticmethod
    def static_method():
        print("called static method")


obj = ClassTest()
obj.instance_method()
# ClassTest.instance_method("sd")  # posbl to use this way. Self take's obj of cls and in this stmt, we just pass a text
ClassTest.class_method()  # here python automatically passes "cls" inside the method
ClassTest.static_method()  # does not take or need any argument
