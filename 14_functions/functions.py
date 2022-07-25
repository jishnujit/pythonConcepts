'''
> order of .py files -> functions.py / functions_args_params.py / default params.py / function_returning_values.py
> when python sees def keyword, it creates a variable 'hello'. This variable is not a variable which stores a value but
  is a callable variable. You need to call this variable inorder to get the statements inside it to execute
> Order of execution -
  line 10 gets executed, i.e. creates a function,
  followed by line 12 which is empty
  line 13 gets executed and it calls the function hello()
  print statement at line 11 gets executed
'''
def hello():
    print("Hello, this is my first function!")

hello()
print("===============================================================================================================")
'''
> do not reuse function names
> variables defined in global scope and function scope are different even though they have same name. python assigns 
  separate memory space for the variables inside function scope
> here we are shadowing friends variable from its outer scope by defining it again inside the function
> If the statement friends = friends + [friend_name] is changed to f = friends + [friend_name], then python will add the 
  new name to friends list in global scope
'''
friends = ["Rolf","Anne"]
print(id(friends))
def add_friend():
    friend_name = "James"
    friends = []
    print(print(id(friends)))
    friends = friends + [friend_name]
    print(friends)

add_friend()