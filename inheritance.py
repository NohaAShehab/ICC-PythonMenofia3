""""""
"""
    object oriented programming: software paradigm or design pattern ===>
     that organize the software design 
    around data or object rather than function and logic 
    
    ---> resuable code  ---> NEVER REPEAT YOUR SELF 
"""


# class Person:  # blueprint of the structure you want to create --->
#     # ## implicit create your own data type
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
#
#     def speak(self):
#         print(f"My name is {self.name}")
#
#
# class Employee:
#     def __init__(self, name, gender, email, dept):
#         self.name = name
#         self.gender = gender
#         self.email = email
#         self.dept = dept
# ################################### Inheritance

# Parent class, Super class
# class Person:  # blueprint of the structure you want to create --->
#     # ## implicit create your own data type
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
#
#     def speak(self):
#         print(f"My name is {self.name}")
#
#
# # derived class , # child class
# class Employee(Person):  # class Employee inherits from Class Person
#     pass
#
#
# # interpreter check if the class has __init__ method , if not ---> call the parent __init__ method.
# e = Employee("Noha", "Female")
# e.speak()

# ###################################### __init__
# class Person:  # blueprint of the structure you want to create --->
#     # ## implicit create your own data type
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
#
#     def speak(self):
#         print(f"My name is {self.name}")
#
#
# # derived class , # child class
# class Employee(Person):  # class Employee inherits from Class Person
#     def __init__(self, email, salary):
#         self.email = email
#         self.salary = salary
#
#
# # interpreter check if the class has __init__ method  will call it , if not ---> call the parent __init__ method.
# e = Employee("nshehab@gmail.com",80000)
# e.speak()  # error

# ################################ call the super constructor
# class Person:  # blueprint of the structure you want to create --->
#     # ## implicit create your own data type
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
#
#     def speak(self):
#         print(f"My name is {self.name}")
#
#
# # derived class , # child class
# class Employee(Person):  # class Employee inherits from Class Person
#     def __init__(self, name="", gender='' , email="", salary=""):
#         # get the super class --> Person
#         super().__init__(name, gender)
#         self.email = email
#         self.salary = salary
#
#
# # interpreter check if the class has __init__ method  will call it , if not ---> call the parent __init__ method.
# e = Employee("noha", "female","nshehab@gmail.com",80000)
# e.speak()  # error


# ######################### multiple inheritance
class Person:
    def __init__(self, name=""):
        self.name = name


class Employee:
    def __init__(self, email=''):
        self.email = email


class Engineer(Person, Employee):  # multiple inheritance
    def __init__(self):
        # super(Engineer, self).__init__()
        super().__init__()
        Employee.__init__(self)


e = Engineer()

# ################################# Polymorphism ---> overriding, overloading
#
# class Person:  # blueprint of the structure you want to create --->
#     # ## implicit create your own data type
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
#
#     def speak(self):
#         print(f"My name is {self.name}")
#
#
# # derived class , # child class
# class Employee(Person):  # class Employee inherits from Class Person
#     def __init__(self, name="", gender='', email="", salary=""):
#         # get the super class --> Person
#         super().__init__(name, gender)
#         self.email = email
#         self.salary = salary
#
#     ##################
#     def speak(self):  # override the speak method in the parent class
#         super().speak()
#         print(f"My email is {self.email}, salary= {self.salary}")
#
#
# # interpreter check if the class has __init__ method  will call it , if not ---> call the parent __init__ method.
# e = Employee("noha", "female", "nshehab@gmail.com", 80000)
# e.speak()
#  ################################## Polymorphism ===> overloading

""" the same method with the same name in the same class  ---> but different in attributes (numbers, types)"""

# class Person:  # blueprint of the structure you want to create --->
#     # ## implicit create your own data type
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
#
#     def speak(self, message="", day=0):
#         print(f"My name is {self.name}")
#         print(message, day)
#
#
# p = Person("Ahmed", "male")
# p.speak()
# p.speak("iti")
# p.speak("hi", 1)
