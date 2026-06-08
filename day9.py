'''FUNCTION'''
#Fn is defined
# def message ():
#     print("Enter a value:")

# #Invocation/calling a fn
# message()
# a = int(input())


# message()
# b = int(input())


# message()
# c = int(input())




# def message():
#     print("Enter a value:")
# # message = 1

# print("We start here,")
# print(message)
# message()
# print("We end here.")
  



#fn returnn something 
# def message ():
#     print("Enter a value:")
#     temp = int(input())
#     return temp

# print("Step 1")
# a =message() 

# print("Step 2")
# b =message() 

# print("Step 3")
# c =message() 

# print("a:", a)
# print("b:", b)
# print("c:", c)


#type error
# def hi()
#     print("Hi")
#     hi(5)



'''Parameterized fn'''
# def hello(n): #defining a fn
#     print("Hello,",n) #body of fn 

# name = input("Enter your name:")
# hello(name) #calling a fn 




# def message(number):
#     print("Enter a number:",number)

# number = 1234
# message(1)
# print(number)



# def message(what,number):
#     print("Enter", what, "number", number)

# message("telephone",11)
# message(11,"telephone")
# message("price",5)
# message("number","number")


#positional fn
# def introduction(first_name, last_name):
#     print("Hello, my name is", first_name, last_name)

# introduction("Luke", "Skywalker")
# introduction("jesse", "quick")
# introduction("clark", "kent")






# #keyword argument (no need to have position)
# def introduction(first_name, last_name):
#     print("Hello, my name is", first_name, last_name)

# introduction("Luke", "Skywalker")
# introduction("jesse", "quick")
# introduction("clark", "kent")

# introduction(first_name = "James", last_name = "Bond")
# introduction(last_name = "Skywalker", first_name = "Luke")




# #mix - positional and keyword argumment
# def adding(a,b,c):
#     print(a,"+",b,"+",c, "=", a + b +c)

# adding(1, 2, 3) #Output => 1 + 2 + 3 = 6

# adding(c = 1, a = 2, b = 3) #Output => 2 + 3 + 1 = 6

# adding(3, c = 1, b = 2) #Output => 3 + 2 + 1 = 6

# adding(3, a = 1, b = 2)





# def happy_new_year(wishes = True):
#     print("Three...")
#     print("Two...")
#     print("One...")
#     if not wishes:
#         return
#     print("happy new year")
# happy_new_year(True)



#return not work 
# def boring_function():
#     print("'Boredom Mode' ON.")
#     return 123

# print("This lesson is intresting")
# boring_function()
# print("This lesson is boring....")



'''explisit giving none''' 
# def checkMyVar(variable):
#     if(variable == 10):
#         print("Variable is 10")
#     else:
#         print("Variable is not up to the mark")
    
#     print(checkMyVar (5))




# def list_sum (lst):
#     s = 0

#     for elem in lst:
#         s += elem 
#     return s
# print(list_sum([5 , 4 , 3]))




# def strange_list_fun(n):
#     strange_list = []
#     for i in range(0,n):
#      #strange_list.append(i+1)
#      strange_list.insert (0, i+1)
#     return strange_list
# print(strange_list_fun(5))
