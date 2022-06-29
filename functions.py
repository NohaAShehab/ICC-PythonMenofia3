"""functions"""


# # ### the function should be defined before calling
# def myfun():
#     pass
#
#
# myfun()
# ######################## function body , accept parameters and return with None

# def mysum(num1, num2):
#     res = num1 + num2
#     print(f"result = {res}")
#
#
# x = mysum(4,5)
# print(x)  # None object
#
# def mysum(num1, num2):
#     res = num1 + num2
#     print(f"result = {res}")
#     return
#
#
# x = mysum(4,5)
# print(x)  # None object

############################ function returns with value

# def mysum(num1, num2):
#     res = num1 + num2
#     print(f"result = {res}")
#     return res
#
#
# x = mysum(4,5)
# print(x)  # res object


# def mysum(num1, num2):
#     res = num1 + num2
#     print(f"result = {res}")
#     return num1, num2, res  # will return with data in form of tuple
#
#
# x = mysum(4,5)
# # print(x)  # res object


# ####################### specify argument types

# def mysum(num1: int, num2: int):  # specify the datatype of the argument
#     print(num1, num2)
#     res = num1+num2
#     print(res)
#
#
# mysum(4, 5)
# mysum("ahmed", "iti")
# mysum("ahmed", 8)
# print(x)  # res object

# #############################
# def mysum(num1: int, num2: int):  # specify the datatype of the argument
#     # # isinstance  --> check if the variable of the type it provides.
#     if isinstance(num1, int) and isinstance(num2, int):
#         print(num1, num2)
#         res = num1 + num2
#         return res  # ## don't complete the rest of function lines
#
#     return None
#
#
# x=mysum(4, 5)
# n= mysum("ahmed", "iti")

# ################################### Default arguments

# def summnum(num1, num2=0, num3=0):
#     print(num1, num2, num3)
#     if isinstance(num1, int) and isinstance(num2, int) and isinstance(num3, int):
#         res = num1 + num2+ num3
#         return res
#
#
# x=summnum(10, 20,30)
# y= summnum(10)


# ############### function =-> accept unknown number of arguments

# def myfun(*nums):  # arguments passed to the function can be zero or more
#     print(nums, type(nums))
#
#
# myfun()
# myfun(3,4)
# myfun("ahmed", "esraa", "shimaa", "Mostafa", "alaa", "nora", 'maha')

#
# def mytestfun(name, *args):
#     print(name, args)
#     for i in args:
#         print(i)
#
#
# mytestfun("noha")
# mytestfun("noha", "iti", "python", "l")


# ####################

# def myfun(id, name):
#     print(id,name)
#
#
# myfun(id=10, name="iti")
#
# myfun( name="Ahmed",id= 100)
# myfun("Ahmed", 100)
# temp = 'My name is {ccc}, id = {myid}'
# print(temp.format(ccc="Ahemd", myid=100))


# ############### function unknow keys , values  ---> ** ((function accept zero or more key-word pairs
# def myfun(**kwargs):
#     print(kwargs)  # accept the args into dictionary
def myfun(**abbas):
    print(abbas)  # accept the args into dictionary


myfun(name="Ahmed", id=10)
myfun(num1=2, num2=6, num3=555)
myfun(ahmed="iti")
