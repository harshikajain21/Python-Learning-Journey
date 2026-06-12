#Q1
# name = "Harshika"
# print("Name:", name)
# age = 20
# print("Age:", age)
# course = "B.tech in Computer Science and Engineering"
# print("Course:", course)




# #Q2
# name1 ="Arya"
# age1 = 20
# course1 = "BCA "

# name2 = "Karan"
# age2 = 21
# course2 = "BBA"

# name3 ="Riya"
# age3 = 19
# course3 = "B.Sc"

# print("Student1:", name1, age1, course1)
# print("Student2:", name2, age2, course2)
# print("Student3:", name3, age3, course3)



# #Q3
# a=10
# b=2
# print("Sum:", a + b)



# #Q4
# a= float(10.5)
# b= float(20.5)
# c = a * b
# print(c)



#Q5



#Q6
# a = 10
# b = 20  
# print("Sum of a and b:", a + b)



# #Q7
# a = 10  
# b = 20
# print("Difference of a and b:", a - b)


# #Q8
# a = 10
# b = 20
# print("Product of a and b:", a * b)     


# #Q9
# a = 10
# b = 20  
# print("Division of a and b:", a / b)


# #Q10
# #division floored value of both variables
# a = 10  
# b = 20
# print("Floor division of a and b:", a // b) 



# #Q11
# #print remainder of a and b
# a = 10  
# b = 20
# print("Remainder of a and b:", a % b)



# #Q12
# a = 2
# b = 3
# print("Power of a and b:", a ** b)




#q1
# 1. Square Hollow Pattern


# print("*"*6)
# print(("*" + " "*4 + "*\n") * 4, end="")
# print("*"*6)

# print()

# # 2. Square Fill Pattern

# print(("*"*7 + "\n") * 6)

# print()

# # 3. Hollow Rectangle

# print("#"*6)
# print(("#" + " "*4 + "#\n") * 3, end="")
# print("#"*6)

# print()

# # 4. Filled Square using #

# print(("#"*8 + "\n") * 6)

# print()

# # 5. Number Triangle Pattern

# print("1")
# print("2 "*2)
# print("3 "*3)
# print("4 "*4)
# print("5 "*5)
# print("6 "*6)
#or
# for i in range(1,7):
#     print(str(i)*i)

# # 6. Up Pointing Arrow

# print("    *")
# print("   * *")
# print("  *   *")
# print(" *     *")
# print("***   ***")
# print("  *   *")
# print("  *   *")
# print("  *****")


#assignment 3
# plant_name = input("Enter a plant name:")

# if plant_name == "Spathiphyllum":
#     print("Yes - Spathiphyllum is the best plant ever!")        
# elif plant_name == "spathiphyllum":
#     print("No , I want a big Spathiphyllum!")   
# else:
#     print("Spathiphyllum! Not ", plant_name+"!")
     

#assignment 4
#Print 1,.....,50
# for i in range(1, 51):
#  print(i)


#Print 1,t,3,t,5,.....,50
# for i in range(1, 51):    
#     if i % 2 == 0:
#         print("t", end=" ")
#     else:
#         print(i, end=" ")



#Print 1,2,t,4,5,t,7,8,t,10,.....,50
# for i in range(1, 51):    
#     if i % 3 == 0:        
#         print("t", end=" ")
#     else:
#         print(i, end=" ")

#1, 2, fiz, 4, buz, fiz, 7, 8, fiz, buz, 11, fiz, 13, 14, fizbuz, 16……50
# for i in range(1, 51):    
#     if i % 3 == 0 and i % 5 == 0: 
#         print("fizbuz", end=" ")
#     elif i % 3 == 0:
#         print("fiz", end=" ")
#     elif i % 5 == 0:
#         print("buz", end=" ")
#     else:
#         print(i, end=" ")



 
#assignment 5
# #tax calculator
# income = float(input("Enter your income: "))
# if income <= 85528:
#     tax = income * 0.18 - 556.02
#     if tax < 0:
#         tax = 0
# else:
#     income > 85528
#     tax = 14839.02 + (income - 85528) * 0.32
# print("Tax:", round(tax))



# #assignment 6
# year = int(input("Enter a year: ")) 
# if year < 1582:
#     print("Not within the Gregorian calendar period")
# elif year % 4 != 0:
#     print("Common year")
# elif year % 100 != 0:
#     print("Leap year")
# elif year % 400 != 0:
#     print("Common year")
# else:
#     print("Leap year")



# #assignment 7
# for i in range(1, 6):
#     print("Mississippi", end="\n")
# print("Ready or not, here I come!")





#assignment 8
# user_word = input("Enter a word:")
# user_word = user_word.lower()
# if user_word[0] in "aeiou":
#     print("The word starts with a vowel")



