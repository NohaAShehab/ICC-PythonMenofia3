# ########## python modules

import os
#
# print(os.getcwd())

# os.mkdir("test")
# os.rmdir("test")
# os.chdir("/home/noha")
# print(os.getcwd())
#
# os.system("ls -l")
# print(os.getlogin())
# ############################# Regular expressions ##################################
# import re
# regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# email = "nshehab@iti.gov.eg"
# res = re.match(regex,email)  ### match object
# if res:
#     print("email valid")
# else:
#     print("email not valid")
#########################################################
import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
email = "nshehab@iti.gov.eg@iti.gov.eg"

"""  re.match check if part of the string, statisfy pattern will return with
    the match object 
    
    re.fullmatch: check if all the string---> matches the expression or not 
"""
# res = re.match(regex,email)  ### match object
# res = re.fullmatch(regex, email)
# print(res)
# if res:
#     print("email valid")
# else:
#     print("email not valid")
# ############################
# import re
# " re.search "
#
# text = r"@"
# sentense = "we study at iti , iti , iti"
# print(re.search(text, sentense))

# #################################################################
#

# l = [3, 4, 56, 6]
# a,b,c,d = l
#
# print(a,c)

#
# l = [3, 4, 56,"iti", 88, 6]
# a, *b, c = l

#######################

# s = open("errors.py","r")
# print(s.read())
# s.close()

# with open("test.txt", "w") as myfile:
#     myfile.write("test message")

# ##################### list comperhsion

# r = range(10)
# r =list(r)
# print(r)

r = [i for i in range(100) if i % 3 == 0]
print(r)

# ######################## all , any
l = ["10", "44", True, None]
# check if the list contain Falsy value

print(all(l))
print(any(l))


## time --> libraru---> validate

