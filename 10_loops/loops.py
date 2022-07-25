''' WHILE AND FOR LOOPS
 while loop demonstration. guess the number game. Note: When we Y/n - any input other than 'n' will get defaulted to 'Y'
'''
number = 7
while True:
    user_input = input("would you like to play? (Y/n): ")
    if user_input == "n":
        break
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly. You WIN!")
    elif abs(number-user_number) == 1:
        print("You were off by one")
    else:
        print("Sorry, you are wrong!")
print("=====================================================================================")
'''
 For loop demonstration. 
'''
friends = ["Bob", "Anne", "Katy", "Scarlett"]

for friend in friends:
    print(f"{friend} is my friend")
print("=====================================================================================")
for a in range(4):
    print(f"{a} is a number")
print("=====================================================================================")
for a in range(4,10):
    print(f"{a} is a number in the range 4 to 10, 10 not included")
print("=====================================================================================")
for a in range(4, 10, 2):
    print(f"{a} is a number in the range 4 to 10, 10 not included and printed alternate numbers")
print("=====================================================================================")
grades = [65, 80, 83, 78, 98]
total = 0
length = len(grades)
print("grades list has 5 marks inside it")
for grade in grades:
    total += grade
print(f"printing total of grades in simple way sum(grades): {sum(grades)}")
print(f"total of all the marks in grades list is {total}")
print(f"Average of {length} subjects is {total/length}")
print("=====================================================================================")