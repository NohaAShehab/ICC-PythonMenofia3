"""   -------------------  lexical scopes -----------"""
""" any variable in the python script is considered to be defined in the global scope of the script ==== module 
    You can access and modify value of the variable anywhere in the script 
    :except in the function , you can modify the global variable -- in case you use the global key word

"""
# x = 10  # global variable
# print("hiii")
# y = "python"  # global variable
# print(x)
# x = "updated"
# print(x)

""" -------- access global variable from the function ---> read  """
# track = "python"
#
#
# def testglobal():
#     print(f"inside the function ---> {track}")
#
#
# testglobal()
""" -------- local scope ------  """
# track = "python"
#
#
# def testglobal():
#     # any variable defined in the function ----> is considered to have local scope
#     # local variable can be accessed only in the function block
#     track = "fullstack using python"  # local scope
#     print(f"inside the function ---> {track}")
#
#
# testglobal()
# print(track)


""" ---- modify the global variable form the function """
# track = "python"
#
#
# def testglobal():
#     global track
#     track = "fullstack using python"  # local scope
#     print(f"inside the function ---> {track}")
#
#
# testglobal()
# print(track)


"""  ------------------- function inside a function --------------"""

""" local variable can be accessed ((read)) anywhere in the function and the inner functions """

# def outerfunction():
#     salary = 10000 # local variable inside the function "outer "
#
#     def calnetsal():
#         print(salary*.86)
#
#     calnetsal()
#
#
# outerfunction()

""" --- modify the local variable from the inner function """

#
# def outerfunction():
#     salary = 10000  # local variable inside the function "outer "
#
#     def calnetsal():
#         salary = 20000  # create new local variable for the cal-net salary
#         print(salary * .86)
#
#     calnetsal()
#     print(f"updated sal {salary}")
#
#
# outerfunction()


# def outerfunction():
#     salary = 10000  # local variable inside the function "outer "
#
#     def calnetsal():
#         nonlocal salary  # this inner function uses the outer function variable ---> salary
#         salary = 20000  # create new local variable for the cal-net salary
#         print(salary * .86)
#
#     calnetsal()
#     print(f"updated sal {salary}")


# outerfunction()
# ################################################
""" ---- use global variable inside inner function """

name = "noha"

""" use global key word ---> when you need to modify any global variable"""
# def outerfunction():
#     # global name
#     # name = "Alaa"
#     #
#     def innerfunction():
#         global name
#         name = "Alaa"
#         print(name)
#     innerfunction()
#
#
# outerfunction()
# print(name)

#########################################
# """ global and nonlocal"""
# name = "Noha"   # global
#
#
# def outerfunction():
#     track = "python"  # local
#
#     def innerfunction():
#         global name
#         name = "Alaa"
#         nonlocal track
#         track = "full stack python"
#         print(name, track)
#
#     innerfunction()
#
#
# outerfunction()
# print(name)
#############################################
name = "Mohab"

def outerfunction():
    global name
    name = "Mohab seif"

    def innerfunction():
        # nonlocal name
        name = "Ahmed"
    innerfunction()

outerfunction()
print("fffffffffff")










