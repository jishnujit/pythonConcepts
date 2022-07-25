'''
What will you do to create a new list which has the elements in numbers multiplied by 2?
numbers = [1,5,10]
generally we write a for loop like below?
doubled = []
for num in numbers:
    doubled.append(num*2)
This can be achieved in python like below
> doubled[x * 2 for x in numbers] => x*2 represents the num*2 in above loop and the for loop is represented after this in this new way
  i.e. what you want to put in the new list followed by the for loop
'''
numbers = [1,5,10]
doubled = [x * 2 for x in numbers]
print(doubled)
'''
what will you do if you want to create a list with all the names starting with 'S'. We can use list comprehensions in this case too.
list=[what u want in the list followed by for loop followed by the condition]
'''
friends = ["Sam","Samantha","Saurav","Anna","Lenhardt"]
starts_wth_s = [friend for friend in friends if friend.startswith("S")]
print(starts_wth_s)

