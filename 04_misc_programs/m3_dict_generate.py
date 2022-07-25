# With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an
# integral number between 1 and n (both included). and then the program should print the dictionary.Suppose the
# following input is supplied to the program: 8

limit = 8
reqd_dict = dict()
for i in range(1, limit+1):
    reqd_dict[i] = i**2
print(reqd_dict)

# dictionary comprehension
answer = {i: i**2 for i in range(1, limit+1)}
print(answer)