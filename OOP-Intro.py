# emp = {"name": "Ahmed", "id": 1, "dept": "opensource"}
# emp2 = {"name": "Mohamed", "id": 2, "dept": "Python"}
# emp3 = {"empname": "Ahmed", "id": 1, "dept": "opensource"}
#
# print(type(emp3))

# 3########################### 1- empty Classes
"""
    class Test:
        pass

    print("----")
"""
# class Employee:
#     pass
#
#
# e = Employee()  # create instance from the class Employee
# print(e)
# print(type(e))

# class Employee:
#     def __init__(self):
#         pass
#
#
# e = Employee()  # create instance from the class Employee
# print(e)
# print(type(e))

# ############### add properties and functions to the classes

"""
    to define class 
    
    class ClassName:
        pass 
        
    this will create new class  --Empty class-- 
    c = ClassName()   # create new object from the class ---> using constructor 
    
    def __init__():
        pass

"""

# class Test:
#     def __init__(self):
#         pass
#
# t = Test()
#
#
# class ITI:
#     pass
#
# i =ITI()
"name, id , dept "

# class Employee:
#     # you can define the instance variable --properties in the __init__:
#     def __init__(self):  # represent the object in the memory
#         # this function will be called during  creating the object
#         print(self)
#         self.name = "Ahmed"
#         self.id = 10
#         self.dept= "Python"
#
#
# e = Employee()  # instnace
# print(e)
# e2 = Employee()

# ##################### customize object creation
# class Employee:
#     def __init__(self, empname, empid, deptname):  # represent the object in the memory
#         # print(self)
#         # ## name, id , dept ---> instance variables
#         self.name = empname
#         self.dept = deptname
#         self.id = empid
#
#
# e = Employee("Ahmed", 10, "python")  # instance
# # access and modify the instance variables
# # display employee name
# print(e.name)
# print(e.__dict__)
#
# # modify dept --->e
# e.dept = "IOS"
# e2 = Employee("Mahmmoud", 100, "php")
# # represent the object properties in form of dictionary
# print(e.__dict__)
#
# e3 = Employee("noha", 550, "Cloud")
# # loosely - dynamically typed lang
# e3.city = "Cairo"  # ## add new property to the object
#
# e4 = Employee(deptname="python", empname="Yostos", empid=100)

# ############################### add functionality to the class

# class Employee:
#     def __init__(self, empname, empid, deptname):  # represent the object in the memory
#         self.name = empname
#         self.dept = deptname
#         self.id = empid
#
#     # add functionality to class ==> instance method , instance function
#     # it depends on the caller object
#     def speak(self, message):
#         print(f"My name is {self.name}, works at {self.dept}, {message}")
#
#
# e = Employee("Ahmed", 10, "python")  # instance
# e.speak("Nice to meet you   ")
# ################################################
# class Employee:
#     # # __init__ special method called when you initiate or create new instance/object from the class
#     # you can add default values to the __init__ arguments
#     def __init__(self, empname, empid=1, deptname=None):  # represent the object in the memory
#         self.name = empname
#         self.dept = deptname
#         self.id = empid
#
#     # add functionality to class ==> instance method , instance function
#     # it depends on the caller object, can be defined with default argument
#     def speak(self, message=""):
#         print(f"My name is {self.name}, works at {self.dept}, {message}")
#
#
# e = Employee("Ahmed", 10, "python")  # instance
# e.speak("Nice to meet you ") # this function can be called only using the object --> instance
#
# e2 = Employee("Ali")  # this will call __init__ in the class
# print(e2.__dict__)
# e3 = Employee("Mostafa", 20)
# print(e3.__dict__)
# ###########################################  #############################
""" you need to define a common property that can be shared all instances taken from the class """


#
# class Employee:
#     location = "Cairo"  # class variable ===> class property shared between all the class instances
#
#     # this class variable can be  accessed and updated through the class name
#
#     def __init__(self, empname, empid=1, deptname=None):
#         self.name = empname
#         self.dept = deptname
#         self.id = empid
#
#     def speak(self, message=""):
#         print(f"My name is {self.name}, works at {self.dept}, {message}")
#         return self.name
#
#
# e = Employee("Ahmed", 10, "python")  # instance
# print(e.__dict__)
# e2 = Employee("Ali")  # this will call __init__ in the class
# print(e2.__dict__)
# e3 = Employee("Mostafa", 20)
# print(e3.__dict__)
#
# print(Employee.location)
# # modify the class variable
# Employee.location = "Alex"  # this will modify the location in all instance
# print("--------------------------")
# ########################## play with class variable
# ###################################  class Method ##################3

# class Employee:
#     location = "Cairo"
#     total_employees = 0
#
#     def __init__(self, empname, deptname):
#         self.name = empname
#         self.dept = deptname
#         self.id = Employee.total_employees + 1
#         Employee.total_employees += 1
#
#     def speak(self, message=""):
#         print(f"My name is {self.name}, works at {self.dept}, {message}")
#         return self.name
#
#     # class method ===> common behaviour can the class do , doesn't depend on the instance
#     # can be accessed through the class name
#     @classmethod  # interpreter --> understand that the upcoming function will not depend on the instance
#     def countEmployees(cls):
#         # print(cls)  # refer to the class methods is considered to be object factory?
#         print(cls.total_employees)
#
#     @classmethod
#     def createDefaultEmp(cls):  # work as object factory -->> You use it to create new object
#         # return new object with default
#         # return Employee("Adam", "default")
#         return cls("Ahmed", "python")
#
#
# Employee.countEmployees()
# print(Employee.total_employees)
#
# # create new default emp
# e3 = Employee.createDefaultEmp()
#
# e = Employee("Ahmed", "python")


# #####################################33


class Employee:
    location = "Cairo"
    total_employees = 0

    def __init__(self, empname, deptname, salary):
        self.name = empname
        self.dept = deptname
        self.salary = salary
        self.id = Employee.total_employees + 1
        Employee.total_employees += 1

    def speak(self, message=""):
        print(f"My name is {self.name}, works at {self.dept}, {message}")
        return self.name

    @classmethod
    def countEmployees(cls):
        print(cls.total_employees)

    @classmethod
    def createDefaultEmp(cls):
        return cls("Ahmed", "python")

    @staticmethod
    # is considered to be helper method --> doesn't depend on the class or the instance
    # can be accessed using the classname or the object
    def calNetSal(salary):
        return salary * .86


e = Employee("Ahmed", "opensource", 10000)
print(e.calNetSal(e.salary))
print(Employee.calNetSal(e.salary))

print(Employee.calNetSal(2000000000000))

# net salary --. salary *.14

# def calNetSal(salary):
#     return salary * .86
#
#
# empnet_sal = calNetSal(e.salary)
# print(empnet_sal)
#
# print(calNetSal(10000003))
