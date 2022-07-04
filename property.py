# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary
#
#     ## setter , getter functions
#     def setSalary(self, salary):
#         if isinstance(salary, int):
#             self.__salary = salary
#         else:
#             self.__salary = None
#
#     def getSalary(self):
#         return self.__salary
#
#
# # # apply validation on this data
#
# e = Employee("Ahmed", 1000)
# print(e.getSalary())
# # e.setSalary('iti')
# # print(e.getSalary())
# e.setSalary(30000)
# print(e.getSalary())
# ####################### Property decorator

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name  #
#         self.__salary = salary  # object property
#
#     @property
#     def salary(self):
#         return self.__salary
#
#     @salary.setter
#     def salary(self, salary):
#         if isinstance(salary, int):
#             self.__salary = salary
#         else:
#             self.__salary = None
#
#
# # # apply validation on this data
#
# e = Employee("Ahmed", 1000)
# # print(e.getSalary)
# # # e.setSalary(40000)
# # e.setSalary= 40000
#
# print(e.salary)
# e.salary = "60000"
# print(e.__dict__)
# ############################################
class Employee:
    def __init__(self, name, salary):
        self.name = name  #
        # self.__salary = salary  # object property
        self.salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if isinstance(salary, int):
            self.__salary = salary
        else:
            self.__salary = 0

    @property
    def netSal(self):
        print(self.__salary)
        return self.__salary * .86


# e = Employee("Ahmed", 1000)
# print(e.salary)
# e.salary = 6000
# print(e.__dict__)
# print(e.netSal)

e2 = Employee("Ahmed", "iti")  # apply the same condition ---> while create the object
print(e2.salary)
print(e2.netSal)