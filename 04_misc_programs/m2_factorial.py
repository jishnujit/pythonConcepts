# Write a program which can compute the factorial of a given numbers.The results should be printed in a
# comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8 Then, the output
# should be:40320

limit = 8
fact = 1
for num in range(1, limit+1):
    fact = fact * num
    print(fact, end=",")
print(f"\nfactorial of {limit} is {fact}")
