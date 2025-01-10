# class car:#class name
#     def __init__(self,model,year,color): #constructor name
#         self.model=model #instance attribute name
#         self.year=year
#         self.color=color

# # car 1 is object and car is class name and mustang 2020 blue are values name
# car1=car("Mustang",2020,"Blue")
# #object.attribute
# print(car1.model,car1.year,car1.color)  
#arguments passed   
# car2=car("Ferari",1998,"Gray")
# print(car2.model,car2.year,car2.color) 
   
# class car:#class name
#     def __init__(self,model,year,color): #constructor name
#         self.model=model
#         self.year=year
#         self.color=color
#     def drive(self): #method name
#         # Accessing the instance variables using "self"
#         print(f"Details of car 1:{self.model},{self.year},{self.color}")
        
# car1=car("fereari",1997,"Green")
# print(car1.drive())

# #without self python would not know which object attribute or methods you are referring to because,a class could have many objects each with their own data
# *******************************************************
# class variable=shared among all instances of a class
# Defined outside the constructor
# allow you to share data among all objects created from that class
# class variable =accessing through class name

class student:
    class_batch=2020
    student_num=0
    def __init__(self,name,age):
        self.name=name #self after created student 1 becomes student1.name and vice versa
        self.age=age
        student.student_num+=1

student1=student("sujal",20)
student2=student("Bir",26)   
student3=student("diwash",17)
print(student1.name,student1.age,student.class_batch)    #class_batch is a variable and accessing through class name instead of object 
print(student2.name,student2.age,student.class_batch)
print(f"batch of students:{student.class_batch},and total num:{student.student_num}")