# Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and
# the values are square of keys.
my_dict = {num: num**2 for num in range(1, 21)}
print(my_dict)
print(my_dict.keys())
