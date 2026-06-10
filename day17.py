'''str'''
# class Super:
#     def __init__(self, name):
#         self.name = name
#     def __str__(self):         #__str__ is for end user(used for customisation)
#         return "My name is " + self.name + "."
# class Sub(Super):
#     def __init__(self, name):
#         Super.__init__(self, name)
# obj = Sub("Andy")
# print(obj)


'''super'''
# class Super:
#     def __init__(self, name):
#         self.name = name
#     def __str__(self):       
#         return "My name is " + self.name + "."
# class Sub(Super):
#     def __init__(self, name):
#         Super.__init__(self, name)
# obj = Sub("Andy")
# print(obj)


'''fun method'''
# class SuperA:
#     var_a = 10
#     def fun_a(self):
#         return 11
# class SuperB:
#     var_b = 20
#     def fun_b(self):
#         return 21
# class Sub(SuperA, SuperB):
#     pass
# obj = Sub()
# print(obj.var_a, obj.fun_a())
# print(obj.var_b, obj.fun_b())
# #output- 10 11
#       #  20 21



'''method overriding  - multilevel inheritance'''
# class Level1:
#     var = 100
#     def fun(self):
#         return 101
# class Level2(Level1):
#     var = 200                       #overrides Level1.var
#     def fun(self):                  #overrides Level1.fun()
#         return 201
# class Level3(Level2):
#     pass
# obj = Level3()
# print(obj.var, obj.fun())
# #output -   200 201





'''multilevel inheritance conflict'''
# #precedence from left to right
# class Left:
#     var = "L"
#     var_left ="LL"
#     def fun(self):
#         return "Left"
# class Right:
#     var = "R"                          #same as left
#     var_right ="RR"
#     def fun(self):
#         return "Right"
# class Sub(Left, Right):
#     pass
# obj = Sub()
# print(obj.var, obj.var_left, obj.var_right, obj.fun())





'''polymorphism - many forms'''

'''building hiearchy of class'''
# class One:
#     def do_it(self):
#         print("do_it from One")
#     def doanything(self):
#         self.do_it()
# class Two(One):
#     def do_it(self):
#         print("do_it from Two")

# one = One()
# two = Two()
# one.doanything()      #output;    do_it from One
# two.doanything()                  #do_it from Two    #bottom to up approach hoga : phele two check karega nhi milega toh one (parent) pea jayega




#MRO - METHOD RESOLUTION ORDER



'''ELSE BRANCH- EXCEPTION'''
def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("Divsion failed")
        return None
    else:
        print("Everything went fine")
        return n
print("----------")
print("reciprocal(2):", reciprocal(2))       #use else
print("----------")
print("reciprocal(0):", reciprocal(0))       
print("----------")





'''accesing exception objects'''
try:
    i = int("Hello!")
except Exception as e:
    print(e)
    print(e.__str__())



# def print_exception_tree(thisclass, nest = 0):
#     if nest > 1:
#         print("     |")
#         ......



'''zero divsion error'''
class MyZeroDivisonError(ZeroDivisionError):
    pass
def do_the_division(mine):
     if mine:
         raise MyZeroDivisonError("some worse news")
     else:
         raise MyZeroDivisonError("some bad news")
do_the_division(False)
do_the_division(True)




