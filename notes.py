# ask the user to enter 5 numbers

"""
    while condition {
        do something
    }

"""
# x = 0
# while x < 5:
#     print(x)
#     x+=1
#
"generate list of integers 1 to 10 "
# x = 1
# l= []
# while x < 11:
#     # print(x)
#     l.append(x)
#     x+=1

"Range function"

m = range(5)  # return with range object you can use it with loop --> return values from 0 to 4
# print(m)
# for i in m:
#     print(i)
#
# ## casted to a list
# m = list(m)
# print(m)
#
# n = list(range(100))
# print(n)


# n = range(1,10)
# print(list(n))

# n = range(1,10, 2)
# print(list(n))

# n = range(10, 1, -2)
# print(list(n))
# #################################
# for i in range(5):
#     print(f"{i}, hiiiii")

# #################---> reverse string
sentence = "Good morning shimaa"  ## casting to list
# sentence = list(sentence)
# sentence.reverse()
# sentence = "".join(sentence)
# print(sentence)
sentence = sentence[::-1]
print(sentence)
####################################

m = "Ahmed"
n = "_".join("Ahmed")  # ## join ---> accept itertable ---> string , list , tuple , set ---> join its elemets together
# with the seperator
print(n)
######################################################
# ask user to enter 5 elemnts in a list
# myinfo = []
# for i in range(5):
#     val = input("please enter your value ")  #
#     myinfo.append(val)


# ################## NEVER TRUST USER INPUT
# myinfo = []
# for i in range(5):
#     val = int(input("please enter your value "))  #
#     myinfo.append(val)
#
# """input function ---> always returns with string"""
# values = []
# for i in range(5):
#     while True:
#         val = (input(f"please enter your value {i+1}"))  #
#         if val.isdigit():
#             break
#     values.append(int(val))
#
#
# print(values)
#


# ####################################### loops
# for i in range(10):
#     if i ==4:
#          continue
#     print(f"{i}")
# else:
#     # this block will be executed if the loop completed ..
#     print("the loop iterations were completed successfully ")
#
#
# print("-------- loop ended --------------")
# for i in range(10):
#     if i ==4:
#         break
#     print(f"{i}")

# ###############################


for i in range(10):
    pass   # this only in the development branch 

print("000000000000000")
