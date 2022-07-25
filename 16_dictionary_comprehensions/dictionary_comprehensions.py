# a list of user names and passwords. Each user data is a tuple
users = [
    (0, "Bob", "password"),
    (1, "Anne", "Anne123"),
    (2, "Zia", "Zia456")
]
# this will create a mapping of username to the entire tuple values
username_mapping = {user[1]: user for user in users}
print(username_mapping)

username_input = input("enter your username: ")
password_input = input("enter your password: ")

# destructuring variables for the username input user has entered
_, username, password = username_mapping[username_input]

# checking passwords
if password_input == password:
    print("your details are correct")
else:
    print("your details are incorrect")