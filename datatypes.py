#   Conversion between different types


x = 10 # int
"""  1- convert form integer to string """
print(type(x))
x = str(x)
print(type(x))

"""1- convert from bool to int or to string """
y = False  # True, False
print(type(y))
# y = int(y) #0
y = str(y)  #string representation of the y

"""2- covert from string to int --> valid if the value in the string is numeric"""
year = "2022"
year = int(year)
print(year)


# day = "Tuesday"
# day = int(day)    #runtime error, this is not valid operation.

"""python provide built-in fucntions --->"""

x = "99nn" # check if the x -> string contian numeric value
if x.isdigit():   #isnumeric()
    print("Valid number")
else:
    print("not valid")
# ########################## Operators #######################
x = 10
x +=5   # x = x+5
print(x)
# ############################ strings
course = "python"
print(len(course))
print(course[5])
"get part of the string "
print(course[2:4])

mystring = "iti iti iti test"
print(mystring.count("i"))
print(mystring.count("iti"))

" concatnetation"
fname= "Noha "
midName= "AbdElhady "
lname= "Shehab"

fullname = fname + midName +midName + lname  ## concate strings ---> make
print(fullname)

"interpolation"
fullname = fname + midName*2 + lname
print(fullname)
m= 2022
# s = "iti" + m
# print(s)
# ###########################################
"capitalize "
name = "ahmed"
print(name.capitalize())

# format string
course = "python"
track = "fullstack"
month = "june"
year = 2022

temp = "I teach .... for .... during june "

"1- using replace --> replace specified pattern with given value, replace string with only string"
print(temp.replace("....", course))  # replace all occurance int the string with the course

"2- format function "

temp = "############3I teach {} for {} track during {}."
# temp = "############3I teach {0} for {1} track during {2}."
print(temp.format(course, track, month))
print(temp.format(track, month, course))


temp = "I teach {coursename} for {trackname} track during {monthname}  {year}."
print(temp.format(trackname=track, monthname=month, coursename=course ,year=year))

"f- format style"
#to define template string
mytemp = f"I teach {course} for {track} during {month} {year}"
print(mytemp)

# ################## string validation  #################
"1- make sure that string consists only form char "

name = "Ahmed"
if name.isalpha():
    print("this string consists of only set of chars ")

"2- make sure that string is only spaces"

mystring = "            " # Truly value

if mystring.isspace():
    print("this string consists of only spaces")
if mystring:
    print("hii")
else:
    print("bye")

print("" and 1)  # "" --> false value








# 12345677  # arabic numbers isdigit
# # isnumeric --> numbers with different lang. representation

# ################  check the status
msg = "THE LECTURE IS INTERESTING."
print(msg.isupper())
print(msg.islower())
print(msg.lower())
#  ########## #################### strim the string
sentnece = "             Python            is        easy.              $"
print(len(sentnece))
# newstr= sentnece.strip() # remove the spaces from left and write edges
# print(newstr)

newstr= sentnece.strip("$ .") # remove the specified characters for the string edges
print(newstr)

# newstr= sentnece.lstrip() # remove the spaces from left
# print(newstr)


newstr= sentnece.rstrip() # remove the spaces from left
print(newstr)


# # get the index of the char in the string
std = "Alaa"
print(std.index("a"))
# ############################## numbers ######################################
temp = 32.6
print(round(temp))


# #### complex
c1 = 10+5j
print(type(c1))

c2 = complex(3,4)
print(c2)





