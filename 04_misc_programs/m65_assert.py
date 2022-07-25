# Please write assert statements to verify that every number in the list [2,4,6,8] is even
#
# data = [2,4,5,6]
# for i in data:
#     assert i%2 == 0, "{} is not an even number".format(i)

# print(sum([i**2 for i in range(10)]))

class A:
    def __init__(self):
        self.calculate(30)
        print("i in Class A is", self.i)
    def calculate(self, i):
        self.i = 2*i

class B(A):
    def __init__(self):
        super().__init__()
        # print("i in Class B is", self.i)
    def calculate(self, i):
        self.i = 3*i

b = B()

# class A:
#     def __init__(self, i=0):
#         self.i = i
# class B(A):
#     def __init__(self, j=0):
#         super().__init__()
#         self.j = j
# def main():
#     b=B(50)
#     print(b.i)
#     print(b.j)
# main()

# class A:
#     def __init__(self, param):
#         self.a1=param
#
# class B(A):
#     def __init__(self, param):
#         self.b1=param
#
#         obj = B(100)
#         print("%d %d" % (obj.a1, obj.b1))

# class A:
#     def __init__(self, i=1):
#         self.i = i
# class B(A):
#     def __init__(self, j=2):
#         super().__init__()
#         self.j = j
#     def main():
#         b=B()
#         print(b.i, b.j)
# main()

# try:
#     fh = open("file","w")
#     fh.write("asdasd")
# else:
#     print("else")
# except:
#     print("excetion")
#
# finally:
#     print("closing")
#     fh.close()

# print(sum([[2,6],[4,3]],[]))

# k=[print(i) for i in 'hello' if i not in 'aeiou']

# var1 = [1,2,3]
# var2 = var1
# var1.append(4)
# print(var2)

# class A:
#     def __init__(self, x):
#         self.x = x
# a = A(100)
# a.__dict__['y'] = 50
# print(a.x + len(a.__dict__))

# i = [12, 9, 14]
# k = [7, 16, 11]
# for j in i[:]:
#     for m in k[:]:
#         if (j%m ==0):
#             j = j//2
#             m=m/2
#             print(j, m)
#         else:
#             j = j+m
#             m = m-j
#             print(j,m)

# class A:
# def __init__(self, x):
# self.x = x
# x = 44
# a = A(4)
# print(a.x)

# def abc(val, y=[]):
#     y.append(val)
#     return y
# print(abc(3))
# print(abc(4,[1,2]))
# print(abc(10))

# a = '-6.34'.zfill(7)
# print(a)

# x = "abcdef"
# i = "i"
# while i in x:
#     print(i, end=" ")

# def country(*abc):
#     if len(abc) == 1:
#         item = abc[0]
#         def f(obj):
#             return obj[item]
#     else:
#         def f(obj):
#             return tuple(obj[item] for item in abc)
#     return f
#
# selection = []
# selection = country(slice(2, None))('AUSTRALIA')
# print(selection)
