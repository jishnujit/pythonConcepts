# Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_list = list(map(lambda num: num ** 2, my_list))
print(square_list)

# 42 - Write a program which can map() and filter() to make a list whose elements are square of even number
# in [1,2,3,4,5,6,7,8,9,10].

even_square_list = list(map(lambda num: num ** 2, filter(lambda num: num % 2 == 0, my_list)))
print(even_square_list)