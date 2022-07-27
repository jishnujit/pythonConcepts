'''
comparisons: ==, !=, >, <, >=, <=
key words like 'is' can also be used in booleans
'''
print(15 == 15)
print(25 > 25)
print(10 != 10)

'''
> when user defines a=20, python saves the value 20 in memory and name the memory space as 'a'.
> Now when we define another variable 'b' with value 20, python does not create a separate memory cell for the variable
  'b' instead, it uses the memory space of variable 'a' and give this memory space another label 'b'. Print the 
  id of both 'a' and 'b', you can see both are the same
> This is not the case while creating lists with same values
> Though 'list1' and 'list2' has same elements, the address in memory will be different. Because when you create a new list, python
  creates a memory for this new list. The elements will be stored somewhere else. The list itself has its own area in memory. Now 
  when you create 'list2', python creates another area in memory for 'list2'. The elements inside the lists were created separately
  and they could be the same between both lists but the lists themselves are different
> 'is' keyword checks if the two elements are exactly the same thing not whether they have exactly the same thing inside them or not
  whether they are similar, i.e. print(list1 is list2) returns false. 'is' keyword is not widely used
'''
a = 20
b = 20
print(id(a))
print((id(b)))
list1 = ["Bob", "Ann"]
list2 = ["Bob", "Ann"]
print(id(list1))
print(id(list2))
print(list1 is list2)
print(list1 is list1)
list3 = ["Bob", "Ann"]
list4 = list3
print(list4 is list3) #returns true as we did not create a new list but pointed the list4 to list3