class A:

    def __init__(self):
        print("Inside Constructor of class A")

    def feature1(self):
        print("feature 1 of Class A")

    def feature2(self):
        print("feature 2 of Class A")


class D:

    def __init__(self):
        print("Inside Constructor of class D")

    def feature6(self):
        print("feature 6 of Class D")


class B(A):
    # class B inherits from class A

    def __init__(self):
        print("Inside Constructor of class B")

    def feature3(self):
        print("feature 3 of Class B")

    def feature4(self):
        print("feature 4 of Class B")


class C(B):
    # class C inherits from class B

    def __init__(self):
        print("Inside Constructor of class C")

    def feature5(self):
        print("feature 5 of Class C")


class E(A, D):
    # class E inherits from class A,D

    def __init__(self):
        print("Inside Constructor of class E")
        super().__init__()

    def feature7(self):
        print("feature 7 of Class E")


objA = A()  # objA can access init(), feature1() and feature 2(). prints the init statement first
objA.feature1()
objA.feature2()
print("==============================================================================")
'''-Class B is a sub class of class A. objB can access the methods of class B and class A
   -Since both the class A and class B has defined constructors, the precedence will be with constructor
   of class B. Now if B has no constructor defined, then precedence is with constructor of class A.
   -When both the classes has constructors defined and if you need to execute constructors from both A and B
   you need to use super().__init__(). calls both the constructor
'''
objB = B()
print("==============================================================================")
'''multilevel inheritance. C is subclass of B and B is subclass of A. Here c can access all the methods of 
   class B and class A 
'''
objC = C()
print("==============================================================================")
'''Multiple inheritance. E inherits both class A and class D. Object of E can access methods of class A and
   class D. when using super().__init__(self) for accessing constructors of class A and class D, only one 
   constructor gets invoked which is based on MRO (Method Resolution Order) which is from left to right.
   class E is defined as 'class E(A, D)', so according to MRO, constructor of class A gets invoked
'''
objE = E()