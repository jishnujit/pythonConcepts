''' (1)
> in python brackets are not mandatory. here x is taken as a tuple even though brackets are not added. But if we need to
  create a list of tuples a or else python gets confused
'''
x = 5, 6
print(type(x))
print("===============================================================================================================")
''' (2)
> Python is intelligent to assign the values of tuple x to two diff variables when declaring a,b=x as seen in below code
> this is called destructuring variables
'''
a,b = x
print(f"a is {a}, b is {b}")
print("===============================================================================================================")
''' (3)
> creating dictionary and printing it
'''
friend_age = {"Rolf":24, "Adam":30, "Anne":27}
for name, age in friend_age.items():
    print(f"{name}:{age}")
'''
> when we call dict.items(), it returns tuples as seen below. Now these tuples can be assigned to diff variables, destructuring 
  variables. 
> This is what is happening in (3), i.e. the loop returns tuples and then these tuples are assigned to name and age variables
> Note: if there are not enough values in tuples to destructure, i.e. for e.g. if returned tuple has 2 values and the 
  number of assigned variable in the loop is 3, it gives a ValueError
'''
for age in friend_age.items():
    print(f"returned value from the for loop: {age}, type of the returned value: {type(age)}")
print("===============================================================================================================")
'''
> use of _(underscore). When a dev is not bothered of a particulat value, it can be assigned to '_'. Python community
  refers this value as not needed or not used value.
'''
person = ("Bob",42, "mechanic")
name, _, profession = person
print(name, profession)
print("===============================================================================================================")
'''
> A list can be converted into 2 lists by adding an '*' symbol
'''
myList = [1,2,3,4,5,6]
head, *tail = myList
print(f"head: {head}, tail: {tail}")
print(f"type of head, {type(head)}, type of tail, {type(tail)}")
*head, tail = myList
print(f"head: {head}, tail: {tail}")