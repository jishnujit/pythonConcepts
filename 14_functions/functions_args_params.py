'''
> both positional and keywords args can be used.
> def fun(x, y) - x and y are parameters here. when calling fun like fun(10,20) - 10 and 20 are arguments
> possible to shuffle keyword args order
> combination of positional and keyword args possible - pos args followed by keyword args which is the rule
'''
def say_hello(name, surname, args_type):
    print(f"Hello {name} {surname}, Welcome to the show!")

say_hello("Adolf", "Hitler", "Positional Arguments") #positional arguments which mathces the position, i.e. Adolf to name and so on
say_hello(name="Michael", surname = "schumacher", args_type="Keyword Arguments")
say_hello(args_type="Keyword Arguments", name="Sachin", surname = "Tendulkar") #possible to shuffle keyword args order
say_hello("Virat", "Kohli", args_type="Keyword Arguments") #combination of positional and keyword args possible - pos args followed by keyword args
