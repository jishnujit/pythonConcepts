# A website requires the users to input username and password to register. Write a program to check the validity of
# password input by users.
#
# Following are the criteria for checking the password:
#
# At least 1 letter between [a-z]
# At least 1 number between [0-9]
# At least 1 letter between [A-Z]
# At least 1 character from [$#@]
# Minimum length of transaction password: 6
# Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above
# criteria. Passwords that match the criteria are to be printed, each separated by a comma.
import re
digit_flag = False
upper_flag = False
lower_flag = False
spl_char_flag = False
password_list = input("Enter a sequence of comma separated passwords: ").split(",")
accepted_password = []
for password in password_list:
    lower_flag = True if re.search("[a-z]", password) else False
    upper_flag = True if re.search("[A-Z]", password) else False
    digit_flag = True if re.search("[0-9]", password) else False
    spl_char_flag = True if re.search("[$#@]", password) else False
    if lower_flag and upper_flag and digit_flag and spl_char_flag and 6 <= len(password) <= 12:
        accepted_password.append(password)
print("accepted passwords are: ", ", ".join(accepted_password))