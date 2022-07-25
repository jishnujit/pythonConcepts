# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 _ C _ D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence
from math import sqrt

C = 50
H = 30
D = input("Enter comma separated values: ").split(",")
for d in D:
    Q = round(sqrt((2*C*int(d)) / H))
    print(Q)
