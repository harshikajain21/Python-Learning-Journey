age = 4
print(age)

myNameVariable - Camel casin 
my_name_variable - snake casing

#DataTypes in Python
x=5 #integer
print(type(x))
y=5.5 #float
print(type(y))
z="Harshika" #string
print(type(z))
a = True #boolean
print(type(a))  
b=1j #complex
print(type(b))
c = None #NoneType
print(type(c))

string1 = "Hello, World!" #string
print(string1)
list1 = [1, 2, 3, 4, 5] #list
print(type(list1))
tuple1 = (1, 2, 3, 4, 5) #tuple
print(type(tuple1))     
 
dict1 = {"name": "Harshika", "age": 4} #dictionary  
print(dict1)
print(type(dict1))

range1 = range(0, 10) #range
print(type(range1))
 
set1 = {1, 2, 3, 4, 5} #set
print(type(set1))
frozenset1 = frozenset({1, 2, 3, 4, 5}) #frozenset  
print(frozenset1)

bytes1 = b"hello" #bytes
print(bytes1)
bytesarray1 = bytearray(b"Hello") #bytearray
print(bytesarray1)

memoryview1 = memoryview(bytes1) #memoryview
print(memoryview1)


#Operators in Python
#Arithmetic operators
a =2
b=3
c = a + b   
d= a-b
e = a * b
f = a / b
g = a // b
h = a % b
i = a ** b
print(c, d, e, f, g, h, i)

#Assignment operators
a = 5  
b += 3 
c -= 2
d *= 4  
e/= 2
f //= 2 
g %= 3
h **= 2 
i &= 2
print(c, d, e, f, g, h, i)

#Comparison operators
a = 5
b = 10
c = a == b
d = a != b
e = a > b
f = a < b
g = a >= b
h = a <= b
print(c, d, e, f, g, h)

#Logical operators
a = True
b = False   
c = a and b
d = a or b  
e = not a
print(c, d, e)
#also
#Logical operators
x=4
y=5
z = (x > 3) and (y < 10)    
a = (x < 3) or (y > 10)
b = not (x > 3)
print(z, a, b)


print(x ==1)
print(x ==2)

print(x !=1)
print(x !=2)    


x=4
print(x< 5 and x<10)
print(x> 5 or x>10)
print(x>5 or x>10)
print(not(x>5 and x>10))


#Identity operators
#(type of variable and variable is bothh checked)
x =10
y =20
print(x is y)
print(x is not y)

#Pratice of identity operators
x = ["Maruti" ,"BMW"]
y = ["Maruti" ,"BMW"]
z=x
print(x is y)
print(x is z)   
print(y is z)
print(x is not y)
print(x is not z)
print(y is not z)


#Membership operators
x = ["apple", "cherry"]
y = "apple"
print(y in x) #true
print(y not in x) #false



#Bitwise operator 
#AND operator
a = 5      # 0101
b = 3      # 0011
print(a & b) #Output: 1 (0001)

#OR operator
a = 5      # 0101
b = 3      # 0011
print(a | b) #Output: 7 (0111)

#XOR operator
a = 5      # 0101
b = 3      # 0011
print(a ^ b) #Output: 6 (0110)

#NOT operator
a = 5      # 0101
print(~a)   #Output: -6 (1010)  

#Left Shift operator
a = 5      # 0101
print(a << 1) #Output: 10 (1010)

#Right Shift operator
a = 5      # 0101   
print(a >> 1) #Output: 2 (0010)



#Input Function
#name = input("Enter your name: ")   
#print("Hello",name)

x = (input("Enter first value for sum: "))
y = (input("Enter second value for sum: "))
#z = x + y   [error because input function returns string]
#print("Sum:", z) 

#{you can also use int before the input function to convert the input to integer}

#or

#Type Casting
z = int(x) + int(y)
print("Sum:", z)
