# Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n
# in comma separated form while n is input by console.

def divisibility_generator(limit):
    for num in range(0, limit):
        if num % 5 == 0 and num % 7 == 0:
            yield num
        else:
            pass


inp = int(input("Enter the limit: "))
reqd_list = [num for num in divisibility_generator(inp)]
print(reqd_list)

