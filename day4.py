#loop
if year < 1582:
    print("Not within the Gregorian calendar period")
elif year % 4 != 0:
    print("Common year")
elif year % 100 != 0:
    print("Leap year")
elif year % 400 != 0:
    print("Common year")
else:
    print("Leap year")



#Infinite loop
while True:
    print ("I am stuck in a loop")




 largestNumber = -99999999
 number= int(input ("Enter s number or type- 1 to stop:"))

 while number != -1:
     if number > largestNumber:
         largestNumber = number
     number =int(input ("Entera number or type- 1 to stop:"))

 print("The largest nuber is:", largestNumber)




#print no. from 1 to 50 from while loop
 i=1
 while i<=50:   
     print(int(i,),end=" ")
     i+=1




#Tell no. of even and odd numbers from user input until user enters 0
 number = int(input("Enter a number: "))
 count =1
 even= 0
 odd = 0
 while count <= number:
     if count % 2 == 0:
         even += 1
     else:
         odd += 1
     count += 1
 print("Even =", even)
 print("Odd =", odd)




 for counter in range(100):
     print("counter:",counter) 



 for counter in range (2, 8 ,3):   #3 is the gap
     print ("The value of counter is currently", counter)





 power = 1
 for expo in range(16):  
     print("2 to the power of",expo , "is", power)
     power *= 2




#break and continue statements
 print ("The break instructions")
 for counter in range (1, 6):
     if counter == 3:
         break
     print("Inside the loop", counter)
 print("Outside the loop")


# print ("The break instructions")
 for counter in range (1, 6):
     if counter == 3:
         continue
     print("Inside the loop", counter)
 print("Outside the loop")

 
