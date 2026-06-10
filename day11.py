# my_tuple = (1, 10, 100)
# t1 = my_tuple + (1000, 10000)
# t2 = my_tuple * 3
# print(len(t2))
# print(t1)
# print(t2)
# print(10 in my_tuple)
# print(-10 not in my_tuple)




# my_tuple = (10, 100, 1000)
# my_tuple += (10000, 100000)
# print(my_tuple) #tuple merges




# tuple_1 = (1, 2, 3)
# for elem in tuple_1:
#     print(elem)

# tuple_2 = (1, 2, 3, 4)
# print(5 in tuple_2)
# print(5 not in tuple_2)

# tuple_3 = (1, 2, 3, 4)
# print(len(tuple_3))
# print(5 not in tuple_3)

# tuple_4 = tuple_1 + tuple_2
# tuple_5 = tuple_3 * 2 
# print(tuple_4)
# print(tuple_5)



# my_tuple = tuple((1, 2, "string"))
# print(my_tuple)
# print(type(my_tuple))

# my_list = [2, 4, 6]
# print(my_list) # outputs: [2, 4, 6]
# print(type(my_list)) # outputs: <class 'list'>
# tup = tuple(my_list)
# print(tup) # outputs: (2, 4, 6)
# print(type(tup)) # outputs: <class 'tuple'


# var = 123
# t1 = (1, )
# t2 = (2, )
# t3 = (3, var)
# t1, t2, t3 = t2, t3, t1
# print(t1, t2, t3)



'''Dictionary'''

# dictionary = {
# "cat":"chat",
# "dog":"chien",
# "horse":"cheval"
# }
# phone_numbers = { 'boss':535882278 , 'suzy':6583775875}
# empty_dictonary ={}

# print(dictionary)
# print(type(dictionary))
# print(phone_numbers)
# print(type(phone_numbers))
# print(empty_dictonary)
# print(type(empty_dictonary))


# #accessing dictonnary 
# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
# phone_numbers = {'boss' : 5551234567, 'Suzy' : 22657854310}
# empty_dictionary = {}



# #key error
# print(phone_numbers['president'])




# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
# words = {'cat','lion','horse'}
# for word in words:
#     if word in dictionary:
#         print(word,"-->", dictionary[word])
#     else:
#      print("-----",word,"is not in dictionary", "------")  #console




# for key , value in dictionary.items():
#    print(key, "-->", value)



pol_eng_dictionary = {
    "zamek":"castle",
    "woda":"water",
    "gleba":"fbhjs"
}
print("pol_eng_dictionary:", pol_eng_dictionary)
copy_dictionary =pol_eng_dictionary.copy()

print("copy_dictionary:",copy_dictionary)

#updating dictionary
pol_eng_dictionary["zamek"]="lock"
item = pol_eng_dictionary["zamek"]
print(item)





phonebook ={} #an empty dictionary 
print(phonebook)

phonebook["Adam"]= 935798355 #create or add a key value pair
print(phonebook) #output ('Adam': 935798355)

del phonebook ["Adam"]
print(phonebook)

   






# popitem()
pol_eng_dictionary = {"kwiat": "flower"}

pol_eng_dictionary.update({"gleba": "soil"})
print(pol_eng_dictionary) # outputs: {'kwiat': 'flower', 'gleba': 'soil'}

pol_eng_dictionary.popitem()
print(pol_eng_dictionary) # outputs: {'kwiat': 'flower'
