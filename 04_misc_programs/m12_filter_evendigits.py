# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of
# the number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line.

even_list = []
temp_list = []
for num in range(1000, 3001):   # 20
    flag = True
    if num % 2 == 0:
        for digit in str(num):
            if int(digit) % 2 != 0:
                flag = False
                break
            else:
                temp_list.append(digit)
        if not flag:
            temp_list.clear()
        else:
            even_list.append("".join(temp_list))
            temp_list.clear()
print(even_list)

# another method
# map() digits of each number with lambda function and check if all() of them even
# str(num) gives us opportunity to iterate through number by map() and join()
print(','.join([str(num) for num in range(1000, 3001) if all(map(lambda num: int(num) % 2 == 0, str(num)))]))

