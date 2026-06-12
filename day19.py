'''comma seprated values (csv) file'''
# import csv
# records = [
#     ['Name','Marks','City','Grade'],
#     ['Rahul',85,'Bhopal','B'],
#     ['Priya',92,'Indore','A'],
#     ['Amit',73,'Jabalpur','B'],
# ]

# with open('studennts.csv','w', newline='') as f:
#     csv.writer(f).writerows(records)




'''reading a csv as dictionary row'''
# with open('studennts.csv', 'r') as f:
#     for row in csv.DictReader(f):
#         print(f'{row["Name"]}:{row["Marks"]} marks({row["City"]})')




'''Assignment'''

import csv
student_record = [
    ['Name', 'Age','Marks in Maths','Marks in science', 'Marks in English'],
    ['Harshika', 13, 96, 87,79],
    ['Bhumika', 14, 67, 79, 75],
    ['Harsh', 17, 96, 54 , 95],
    ['Monish', 19, 66, 56, 97],
]

with open('students.csv','w', newline='') as f:
    csv.writer(f).writerows(student_record)


#search record with name
# name = input("Enter name to search:") 

# with open('students.csv', 'r') as f:
#     for row in csv.DictReader(f):
#         if row["Name"] == name:
#             print(f'Found {name}') 
#             print(f'{row["Name"]}:{row["Marks in Maths"]} marks in maths, {row["Marks in science"]} marks in science, {row["Marks in English"]} marks in english')   
#             found = True
#             break
# if not found:
#     print("Student not found!")

# #averge and grade
# average = (student_record[1][2]+ student_record[1][3]+ student_record[1][4])/3
# print(average)
# if average >=90:
#     print ('Grade =A')
# elif average >=80:
#     print('Grade = B')
# elif average >=70:
#     print('Grade = C')
# else:
#     print('Grade = D')



