# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated
# numbers

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_square_list = [x**2 for x in my_list if x % 2 != 0]
print(odd_square_list)
