# Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

n = 5
sum = 0
for num in range(1, 5):
    sum += n/(n+1)

print(round(sum, 2))
