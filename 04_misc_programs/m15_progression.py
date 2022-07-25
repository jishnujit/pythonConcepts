# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

limit = 4
result = 0
value = int(input("Enter a number for computation of a+aa+aaa+aaaa: "))
for i in range(1, limit+1):
    print(i)
    temp = value ** i
    print(f"{value}**{i} = {value**i}")
    result += temp
print(result)

