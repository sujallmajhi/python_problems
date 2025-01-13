#allows a class  to inherit attributes and methods from another class helps with code reusability and extensibility class child parent()
# class Animal:
#     num=0
#     def __init__(self,name):
#         self.name=name
#         self.alive=True
#         Animal.num+=1
#     def eat(self):
#         print(f"{self.name}is eating:")
#     def sleep(self):
#         print(f"{self.name}is sleeping")
#     def walk(self):
#         print(f"{self.name}is walking:")

# class dog(Animal):
#     def running(self):
#         print(f"{self.name}is running:")
# class cat(Animal):
#     def breed(self):
#         print(f"{self.name}is a big tiger Breed:")

# dog1=dog("Diwash")
# dog1.eat()
# dog1.sleep()
# dog1.walk()
# dog1.running()
# print(f"{dog1.alive}")

# cat1=cat("Bir")
# cat1.eat()
# cat1.sleep()
# cat1.walk()

# dog2=dog("dholu")
# dog2.sleep()
# print(f"total number of objects is {Animal.num}")

#types of inheritance multiple and multilevel

# class Animal:

#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f"{self.name} is eating")

#     def sleep(self):
#         print(f"{self.name} is sleeping")

# class Prey(Animal):
#     def flee(self):
#         print(f"{self.name} is fleeing")

# class Predator(Animal):
#     def hunt(self):
#         print(f"{self.name} is hunting")

# class Rabbit(Prey):
#     pass

# class Hawk(Predator):
#     pass

# class Fish(Prey, Predator):
#     pass

# rabbit = Rabbit("Bugs")
# rabbit.eat()
# rabbit.sleep()
# rabbit.flee()

#polymorphism
# poly=many and morphe=form 
#two ways to achieve polymorphism
#1.Inheritance=An object could be treated of the same type as a parent clas
#2.duck typing=object must have necessary attributes/methods


# from abc import ABC, abstractmethod

# class Shape(ABC):

#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side ** 2

# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def area(self):
#         return self.base * self.height * 0.5

# class Pizza(Circle):
#     def __init__(self, topping, radius):
#         super().__init__(radius)
#         self.topping = topping

# shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("pepperoni", 15)]

# for shape in shapes:
#     print(f"{shape.area()}cm²")


#duck typing: another way to achieve polymorphism besides inheritance object must have the minimum necessary attribute methods ,"if it looks like duck and quacks like a duck,it must be duck"

# class Animal:
#     alive = True

# class Dog(Animal):
#     def speak(self):
#         print("WOOF!")

# class Cat(Animal):
#     def speak(self):
#         print("MEOW!")

# class Car:
#     alive = True


#     def speak(self):
#         print("HONK!")

# animals = [Dog(), Cat(), Car()]

# for animal in animals:
#     animal.speak()
#     print(animal.alive)

#process of wrapping someinformation in a single entity
#-(protectec attribute)
#--(private attribute)

# class Employee:
#     def getdata(self):
#         self.name=input("Enter your name::") 
#         self.__salary=input("Enter your salary:")
#     def display(self):
#         print(f"your name is:{self.name}")
#         print(f"your salary is:{self.salary}")
#     def revised(self):
#         print(f"your salary is {self.__salary}") #can be accessed using self.__privetae variable
# e1=Employee()
# e1.getdata()
# e1.revised()

# class shape:
#     _length=10
#     _breadth=20
#     def display1(self):
#         print(f"{self.length}")
#     def display(self):
#         print(f"{self._length} and {self._breadth}")

# s1=shape()
# s1.display1() #cannot access
# s1.display()