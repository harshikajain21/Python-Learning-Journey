'''membership operator'''
# pol_eng_dictionary = {
#     "zamek":"castle",
#     "woda":"water",
#     "gleba":"soil"
# }
# if "zmaek1" in pol_eng_dictionary:
#     print ("Yes zamek1 is present in the dictionary")
# else:
#     print("No zamek1 is present in the dictionary")




'''delete in dictionary'''
# print(pol_eng_dictionary)
# print(len(pol_eng_dictionary))

# del pol_eng_dictionary ["zamek"]
# print(pol_eng_dictionary)
# print(len(pol_eng_dictionary))

# pol_eng_dictionary.clear()
# print(pol_eng_dictionary)
# print(len(pol_eng_dictionary))

# del(pol_eng_dictionary)
# print(pol_eng_dictionary)




#problem 
'''loop'''
sd = {}
while True:
    name = input ("Enter students name:")
    if name == "":
        break
    score = int(input(f"Enter {name}'s score:"))   #f string or string concatination
    
    if score not in range(1,11):
        break
    if name in sd:
        sd[name] += (score,)
    else:
        sd[name]= (score,)

print(sd)

for name, mark in sd.items():
    sum = 0
    for m in mark:
        sum += m
    print(name, "-->", sum/len(mark))
