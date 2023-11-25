class Student:
    school_name="ABC School"
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=Student("Umayya",20)
print("Student :",s1.name,"\nAge :",s1.age)
print("School name :",Student.school_name)
s1.name="Hanoona"
s1.age=21
print("Student name : ",s1.name,"\nStudent age :",s1.age)
Student.school_name="XYZ Sxhool"
print("School name : ",Student.school_name)
