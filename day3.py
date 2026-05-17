#decision making statement

Larger no. from 2 no.s with if else
number1 = int (input("Enter the first number:"))
number2 = int (input("Enter the second number:"))

if number1 > number2:
    larger_number = number1
else:
    larger_number = number2
print("The larger number is:",larger_number) 





number1 = int (input("Enter the first number:"))
number2 = int (input("Enter the second number:"))
number3 = int (input("Enter the third number:"))

larger_number = number1

if number2 > larger_number:
     larger_number = number2
 
if number3 > larger_number:
     larger_number = number3
 
print ("The larger number is:",larger_number)





number1 = int (input("Enter the first number:"))
number2 = int (input("Enter the second number:"))
number3 = int (input("Enter the third number:"))

largest_number  = max(number1, number2, number3)
lowest_number  = max(number1, number2, number3)

print("The largest number is:",largest_number)
print("The lowest number is:",lowest_number)



plant_name = input("Enter a plant name:")

if plant_name == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")        
elif plant_name == "spathiphyllum":
    print("No , I want a big Spathiphyllum!")   
else:
    print("Spathiphyllum! Not ", plant_name+"!")
     

Print 1,.....,50
 for i in range(1, 51):
 print(i)


Print 1,t,3,t,5,.....,50
 for i in range(1, 51):    
     if i % 2 == 0:
         print("t", end=" ")
     else:
         print(i, end=" ")



Print 1,2,t,4,5,t,7,8,t,10,.....,50
 for i in range(1, 51):    
     if i % 3 == 0:        
         print("t", end=" ")
     else:
         print(i, end=" ")

1, 2, fiz, 4, buz, fiz, 7, 8, fiz, buz, 11, fiz, 13, 14, fizbuz, 16……50
 for i in range(1, 51):    
     if i % 3 == 0 and i % 5 == 0: 
         print("fizbuz", end=" ")
     elif i % 3 == 0:
         print("fiz", end=" ")
     elif i % 5 == 0:
         print("buz", end=" ")
     else:
         print(i, end=" ")



 
