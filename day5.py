#Logical expressionn
 var = 10
 print (var ==0)
 print (not(var !=0))

 print(var>0)
 print(not(var <=0))



 numbers =[10, 32, 33,7,6,9]
 print(numbers)
 print(type(numbers))


# number[0] => numbers address =((number of bytes occupied * index)) => 0x0000 = 10
# number[1] => numbers address =((number of bytes occupied * index)) => 0x0002 = 5
# number[2] => numbers address =((number of bytes occupied * index)) => 0x000


#print("First element content:", numbers[0])
#print("second element content:", numbers[1])
# print("third element content:", numbers[2])
# print("Fourth element content:", numbers[3])
# print("Fifth element content:", numbers[4])

#update list
list=[8,6,3,7,9]

list.append(4)

list.insert(3,2)


# numbers[1] = numbers[4]
# print (numbers)

#length of list
print(numbers)
print (len(numbers))

# del numbers [3]
list=[8,6,3,7,9]
list.delete(2)


#negative index
#print (numbers[-1])


# list = [1, 2, 3, 4, 5]
# #print(list)
# print(len(list))
# #delete last element
# del list[len(list)-1]
# print(list)
# #update middle element
# list[len(list)//2] = int(input("Enter a number: "))
# print(list) 




# list=[1,2,3,4,5]
# print(list)
# list.append(6)
# print(list) 

# list.insert(0,10)
# print(list)

 #inserting in empty list
 list1 =[]
 list1.insert(0,10)
 print(list1)

