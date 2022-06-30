# ######### syntax errors
# def abc():
#     print("hiiiiiiiiiii")
#
# abc()
#
# print("iti"  # ## syntax error , parser
#
#
# print("good morning")
#
# x = 10

#  # run time error --> exceptions

# print("this an example of runtime error -----")
# print(x)  # NameError
#
# print("-----------------------")

"""
    Exception -->sudden event occurs while executing the python script, disturb the 
    normal flow of the script execution... 
    
    You must handle this exception
"""


#  ############### logical error  ---> unit-test script ((developer))

# def addnums(num1, num2):
#     return num1 * num2
#
#
# print(addnums(2, 2))
# print(addnums(10, 2))
# ####################################33 handle exception ((Run time error ))
# try:
#     print(name)
# except:
#     print("problem here ")
#
# print("---------------------------------")

# print(name)
# #### handle exception
# try:
#     print(name)
# except Exception as e:
#     print(f"'problem here ::: {e} ")
#     # name = "default"
#     # print(name)
#
# print("---------------------------------")

# ##############################3

course = "python"

try:
    print(course)
except Exception as e:
    print(e)
else:
    "code in this block will executed if there is no problem"
    print("------ the operation executed successfully ----")

finally:
    "code in this block will executed alaways"
    print("--------------------End of trying this operation -------------------")

















