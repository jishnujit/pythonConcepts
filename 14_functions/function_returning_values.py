'''
> None is a special value in python that means No Value or Missing Value or Undeclared Value.
> When there is no return value specified for a function and if we print the function it prints 'None'
> return statement terminates the function and if any code is written after return statement in a function those lines
  of codes will not get executed
'''
def add(x, y):
    print(x+y)

add(10,5) #prints 15
result = add(10,5) #prints 15 and then returns default value 'None' to variable 'result' as there is no return statement declared
print(result) # prints 'None' which is stored in result variable when called in above statement
print("==============================================================================================")
print(add(10,5)) #prints 15 and None. code is same as line no. 9,10
print("==============================================================================================")
def sub(x,y):
    return x-y
print(sub(10,5))