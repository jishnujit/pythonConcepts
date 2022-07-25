'''
> It means that functions are just variables and u can pass in as arguments to functions and use them in the same way
  that u would use any other variable
'''


def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0")

    return dividend / divisor


def calculate(*values, operator):
    return operator(*values)


result = calculate(10, 5, operator=divide)
print(result)
print("=============================================================================================================")

# another example


def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}")


friends = [
    {"name": "Rolf Smith", "age": 29},
    {"name": "Bhama", "age": 26},
    {"name": "Anne", "age": 25}
]


def get_friend_name(friend):
    return friend["name"]


print(search(friends, "Anne", lambda friend: friend["name"]))
print(search(friends, "Bob Smith", get_friend_name))
