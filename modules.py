"""

Any python file is considered to be a module

"""

""" import another module """
# import messages  # import all file content in the current module
# # you can access the variable, function from the module using module name
# print(messages.x)
# messages.sayhello("Nice to meet you ")


# """ alias for the module name """
# import  messages as msg
# print(msg.x)
# msg.sayhello("jkhjkdfh")


""" import part of the module """
from messages import  x, sayhello
print(x)
sayhello("cfff")