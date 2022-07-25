# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple
# which contains every number.Suppose the following input is supplied to the program:

my_list = input("Enter comma separated numbers: ").split(",")
print(my_list)
my_tuple = tuple(my_list)
print(my_tuple)