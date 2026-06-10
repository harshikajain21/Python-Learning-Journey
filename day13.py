# print(mayur.gender)
# print(mayur.grade)

#or

class Student:
    def __init__(self, name, age, gender, grade):
        self.name = name   #class prop
        self.age = age
        self.gender = gender
        self.grade = grade 

    def printDetails(self):
        print("name:", self.name)
        print("age:", self.age)
        print("gender:", self.gender)
        print("grade:", self.grade)

mayur = Student("Mayur Valvi", 20, "Male", "10th")
print(mayur)

mayur.printDetails()
