'''indexing accesing in string'''
# city = 'Bhopal'

# print(city[0])
# print(city[2])

# print(city[-1])
# print(city[5])

# print(city[-3])
# print(city[3])


'''slicing in string'''
# name = 'Priya Sharma'
# print(name[0:5])                             #Priya
# print(name[6:])                              #Sharma
# print(name[:5])                              #Priya
# print(name[::2])                             #Pay hr (every 2nd character)
# print(name[::-1])                            #amrahS ayirP (reverse)




text = '     Hello Python World!     '
'''case'''
# print(text.upper())
# print(text.lower())
# print(text.title())                       #Give the tiltle 
# print(text.capitalize())                  #capitalize first letter of string

'''strip whitespace'''
# print(text.strip())                       #count whitespace before and after the  string start & complete

'''search'''
# print('Python' in text)                   #to search if the strring is present or not (in)
# print(text.find('Python'))                 
# print(text.count('l'))

'''replace'''
# print(text.replace('Python', 'AI'))              #1st letter to be replaced, 2nd the string with which it hass to replace

'''split & join'''
# csv  = 'Rahul,22,Bhopal,Engineer'
# parts = csv.split(',')
# print(parts)
# print(parts[0])
# rejoined = ' | '.join(parts)
# print(rejoined)

'''check content'''
# print('hello123'.isalnum())
# print('12345'.isdigit())
# print('Python'.isalpha())
# print('  '.isspace())

'''start/end check'''
# email = 'student@gmail.com'
# print(email.endswith('.com'))
# print(email.startswith('stu'))



'''f string'''
# name, marks, rank = 'Anita', 92.567, 3

'''basic'''
# print(f'Hello, {name}!')

'''format numbers'''
# print(f'marks: {marks:.2f}')               #upto 2 decimals lenge float value ka
# print(f'marks: {marks:.0f}')               # upto 0 lenge that means no decimal value
# print(f'marks: {1000000:,}')               #comma seprator

'''padding and alignment'''
# print(f'{name:<15}|{marks:>8.2f}|Rank:{rank}')         #left/right align          # ^ isse padding hogi  donno side karna ho toh.....
# #Anita          |     92.57|Rank:3       
# print(f'hello {name:^10}')
# print(f'hello {name:>10}')
# print(f'hello {name:<10}')
# print(f'hello {name:*^11}')                   #isse string/character bhi print ho jayega    

'''expression inside{}'''
# price, gst = 500, 0.18
# print(f'Price:Rs.{price} | GST:Rs.{price*gst:.2f} | Total:Rs.{price*(1+gst):.2f}')
# i =0
# string = "Hello, How are you doing today?"
# lower_string = string.lower
# vowels = ['a', 'e', 'i', 'o', 'u' ]
# for i in lower_string:
#     for i in vowels:
#         count+=1
# print(f'total vowel:{count}')

# #print you from string

# print(string[::-1])   #reverse

# #check if string is palidrome
# non_palin, palin = "abcdef", "axtta"



'''extra'''
#read a file that  already exist
with open("data.txt", "r") as  file:
    data = file.read()
print(data)

#write a file
with open('students.txt', 'w') as f:
    f.write('Rahul  Sharma,85,Bhopal\n')
    f.write('Priya Veerma,92,Indore\n')
    f.write('Amit Kumar,73,Jabalpur\n')

#append(data update hoga{add wto overwriting})
with open('students.txt', 'a') as f:
    f.write('Sneha Joshi,88,Bhopal\n')

#read entire file 
with open('students.txt', 'r') as f:
    content = f.read()
print(content)

#read line by line(memory efficient for large file)
with open('students.txt', 'r') as f:
    for line in f:
        name, marks, city, =  line.strip().split(',')
        print(f'{name:<15} | {marks:>5} | {city}')
        print("-----------")
