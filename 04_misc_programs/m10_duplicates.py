# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing
# all duplicate words and sorting them alphanumerically.
my_list = input("Enter sequence of whitespace separated words: ").split(" ")
for word in my_list:
    if my_list.count(word) > 1:
        my_list.remove(word)
my_list.sort()
print(" ".join(my_list))