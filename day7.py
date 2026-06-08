'''Sorting a list with bubble sort'''
#wrong
# list = [8,10,6,2,4]
# while idx>idx+1:
#     list = [8,10,6,2,4]
# list[0],list[1] = list[1] ,list[0]
#  if idx>idx
#right one....
# my_list = [8,10,6,2,4]
# swapped = True #it's a little fake ,we need it to enter the while loop
# count=0
# index=0
# while swapped:
#     swapped = False #no swap 
#     for i in range(len(my_list) -1- index):
#         index = i
#         count += 1
#         if my_list[i] > my_list[i+1]:
#             swapped = True #swap occured
#             my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
# print(my_list)
# print(count)

# #or

# my_list = [8,10,6,2,4] #predefined method
# my_list.sort()
# print(my_list)



'''reversing a list'''
# my_list = [8,10,6,2,4]
# my_list.reverse()
# print(my_list)


'''slice'''
# list1 =[1]
# list2 = list1[:]
# list1 =2
# print=(list2)
# print=(list1)

# list = [10,8,6,4,2]
# new_list = list[1:3]
# print(new_list)

# list = [10,8,6,4,2]
# new_list = list[1:-1]
# print(new_list)

# list = [10,8,6,4,2]
# new_list = list[-5:3]
# print(new_list)



'''deleting'''
#delete element of list
ist = [10,8,6,4,2]
del list[1:3]
print(list)

#delete whole elements of list
del list[:]
print (list)




'''in and not in operators'''
list = [0,3,12,8,2]
print(5 in list) #false
print(5 not in list) #true
print (12 in list)  #true
