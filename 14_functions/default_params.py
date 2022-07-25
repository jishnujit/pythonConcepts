'''
function params can be passed with default values so that if user does not pass any value for this parameter, the python
compiler takes this default parameter as variable value
'''
def add(x, y=5):
    print(x+y)

add(10, 20) # positional args - default value is overridden by 20
add(10) # positional args - default value of y is taken here
#add(y=10) #error as value for x is missing
add(x=10, y=20) #keyword args
add(x=20) #keyword args
add(y=10, x=1) #keyword args
# add(x=5, 5) # positional argument follows keyword argument
