'''
> Helps in associating keys with values.
> In the example below, Rolf, Adam and Anne are keys and 24, 30, 27 are its values
> Accessing friend_age[0] is not allowed. Always access values using keys
> add values to dictionary - friend_age["Bob"] = 30
> Possible to create list of dictionaries line no.36. in this eg, each dictionary will have details of a friend. use index
  to get the value
> for accessing a dictionary, rather than a for loop as in line no. 19, it is always better to use the for loop as in
  line no.22 with dictionary_variable.items(). this actually returns keys and values and for loop can have 2 variables
  to accomodate this
> 'in' keyword can be used to check if a particular key is there in the dictionary as in line no.25
> all the values of the dictionary can be assigned to another variable (list) as in line no.30 and can be manipulated as per req.
  Same way all the keys can also be extracted and assigned to another variable
'''
friend_age = {"Rolf":24, "Adam":30, "Anne":27}
print("printing age of ann:", friend_age["Anne"])
friend_age["Zia"] = 30
print("after adding a new key: ", friend_age)
friend_age["Rolf"] = 29
print("updating age of rolf: ", friend_age)
print("================================================================================")
for friend in friend_age:
    print(f"Age of {friend} is {friend_age[friend]}")
print("================================================================================")
for name, age in friend_age.items():
    print(f"{name}:{age}")
print("================================================================================")
if "Anne" in friend_age:
    print(f"age of Anne is {friend_age['Anne']}")
else:
    print("Anne is not in the list")
print("================================================================================")
ages = friend_age.values()
avg_age = sum(ages)/len(ages)
print("ages: ", ages)
print("average age: ",avg_age)
print("================================================================================")
friends = [
    {"name": "Rolf", "Age": 25, "Profession": "Teacher"},
    {"name": "Adam", "Age": 26, "Profession": "Developer"},
    {"name": "Anne", "Age": 27, "Profession": "QA Analyst"},
    {"name": "Zia", "Age": 28, "Profession": "Data scientist"},
]

print("accessing first element of the list: ",friends[0])
print("Accessing name of first element of the list: ", friends[3]["name"])