""""""

"""
    accessibility --> print , edit 
    
    access modifiers 
    public ---> the property can be accessed anywhere through the object
    private ---> the property can be accessed only in the class through the object
    
    protected ---> the property can be accessed in the class or the child classes 
    static --> property can be accessed using the class name   -in python class method, class variable -

    Developer is mature enough 
"""


# class Employee:
#     def __init__(self, name, email, sal):
#         self.name = name  # public property
#         # protected
#         self._email = email  # protected property ---> can be accessed anywhere
#         # private property
#         self.__salary = sal
#
#
# e = Employee("Ahmed", "ahmed@gmail.com", 100000)
# print(e.name)
# e.name = "Ahmed Mohamed"
# # print(e.__salary)
# print(e.__dict__)
#
# # ####################3
# class Engineer(Employee):
#     def __init__(self, name, email, dept):
#         super(Engineer, self).__init__(name, email, 10000)
#         self.dep = dept
#
#     def testprotected(self):
#         print(self._email, self.__salary)
# #
# #
# eng = Engineer("Mohamed", "moha@gmail.com", "os")
# # eng.testprotected()
# # # eng.id = 1000
# print(eng.__dict__)
# # eng._email = "updated@gmail.com"  # ethically not allowed
# # print(eng.__dict__)
# #################################
class Test:
    def __init__(self,id, name,sal):
        self.id = id
        self._name= name
        self.__salary = sal


t= Test(1,"Ahmed", 1000)
print(t.__dict__)
t._name = "Mohamed"
print(t.__dict__)
# ethically not allowed
t.__salary = 2000  # trying to modify the private property __salary
print(t.__salary)  # new  property __salary --> access modifier public









