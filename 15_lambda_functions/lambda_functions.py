'''
> functions which does not have a name and is only used to return values
> lambda functions are exclusively used to operate on inputs and return outputs. Never used to perform actions
> Not used widely as it is hard to read and keep track of , especially when the programs grow
> map returns an object. to print the elements inside we need to convert it into a list - list(map(definition))
'''
def add(x, y):
    return(x+y)
print(add(10,20))
'''
> the above functions is now changed to lambda function as below
> we specify the keyword 'lambda' then the list of parameters it takes (x, y) and then the return value (x+y)
> it is not needed to specify return statement. When interpreter sees the keyword 'lambda' it knows there will be a value returned
> lambda functions doesnt have any name, so we generally assign it to any variable
> to use lambda functions directly, the lambda fn and the input needs to be in parenthesis. (lambda x,y: x+y)(10,10) takes
  10, 10 as input
'''
a = lambda x,y: x+y
print(a(5,7))
print((lambda x,y: x+y)(10,10))
print("===============================================================================================================")


def double(x):
    return x * 2


sequence = [1, 5, 9, 11, 15]
# to create a list with all the values in the sequence multiplied by 2
# method 1 - list comprehension
doubled_list_comprehension = [double(x) for x in sequence]
print("doubled - using list comprehension: ",doubled_list_comprehension)
# method 2 using map function
doubled_map = list(map(double, sequence))
print("doubled using map function: ",doubled_map)
# method 3- using lambda functions
doubled_lambda = [(lambda x: x * 2)(x) for x in sequence]
print("doubled using lambda function: ", doubled_lambda)
# method 4 - using lambda and map functions
doubled_map_lambda = list(map(lambda x: x * 2, sequence))
print("doubled using map and lambda: ", doubled_map_lambda)