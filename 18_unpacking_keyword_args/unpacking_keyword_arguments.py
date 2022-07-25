'''
> '**kwargs' collects the keyword arguments and put it into a dictionary where the dictionary key is the name of the
  keyword argument
'''


def named(**kwargs):
    print(kwargs)


named(name="Bob", age=25)
print("=============================================================================================================")


def name(fname, age):
    print(fname, age)


details = {"fname": "Bob", "age": 25}
name(**details)  # unpacking dictionary
print("=============================================================================================================")


def both(*args, **kwargs):
    print(args)
    print(kwargs)


both(1, 3, 5, name="Anne", age=25)