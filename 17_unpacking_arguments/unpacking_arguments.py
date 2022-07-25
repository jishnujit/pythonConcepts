'''
'*' can be used as function parameter to allow it to take any number of arguments
'''


def mul(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg
    return total


print(mul(1, 3, 5))
print(mul(5, 10))
print("=============================================================================================================")
# '*' can be used while calling the function as well as given below. Here when calling add function, '*' is used.
# python will assign 3 to x and 5 to y, destructing num variables and splitting it out to multiple values


def add(x, y):
    return x+y


num = [3,5]
print(add(*num))
print("=============================================================================================================")
'''
> when '**' is used, python detects it as named arguments and tried to map the key of the dictionary to the parameters
  of the function. Note: both the key and parameter variables should be same for this to work
'''
nums = {"x": 15, "y": 25}
print(add(**nums))
print("=============================================================================================================")
'''
> writing a function to use both the above functions mul and add such that all the positional arguments into *args
  and have an named/keyword argument
'''


def apply(*args, operator):
    if operator == "*":
        return mul(*args) #check the explanation below
    elif operator == "+":
        return sum(args)
    else:
        return "no valid operator to apply()"


'''
> the below code prints the values 1,3,5 as a tuple. when u multiply 1 by a tuple it returns tuple
> when u print args in mul function it prints tuple of tuples. now when it is iterated over a for loop it actually takes
  the first tuple inside the tuple of tuples. This is because, in apply() the mul function call is sending a tuple and 
  the param in mul function is expecting an unpacked values but we send packed ones. We need to use * while calling mul
  in apply
'''
print(apply(1,3,5, operator="+"))
print(apply(1,3,5, operator="*"))