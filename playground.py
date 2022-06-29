# # calculator
# # ## function ask user to enter 2 numbers , enter operation
#
#
# # NEVER REPEAT YOURSELF
#
# def calculator():
#     res = 0
#     while True:
#         num1 = input("please  enter num1 : ")
#         if num1.isdigit():
#             break
#
#     while True:
#         num2 = input("please  enter num2 : ")
#         if num2.isdigit():
#             break
#
#     while True:
#         op = input("please enter operation like + - / * ")
#         if op in ["+", "-", "*", "/"]:
#             break
#
#     # print(f"{int(num1)} {op} {int(num2)}")
#     if op == "+":
#         res = int(num1) + int(num2)
#     elif op == "-":
#         res = int(num1) - int(num2)
#     elif op == "*":
#         res = int(num1) * int(num2)
#     elif op == "/":
#         if int(num2):
#             res = int(num1) / int(num2)
#         else:
#             res = None
#
#     return res
#
#
# print(calculator())
#############################################################
# def askforInt(msg):
#     while True:
#         num1 = input(f"{msg}")
#         if num1.isdigit():
#             return num1

# ## recursion

def askforInt(msg):
    num1 = input(f"{msg}")
    if num1.isdigit():
        return num1
    return askforInt(msg)


def askforoperator(messge):
    op = input(messge)
    if op in ["+", "-", "*", "/"]:
        return op
    return askforoperator(messge)


def calculator():
    res = 0
    op = askforoperator("please enter operation like + - / * ")
    num1 = askforInt("please enter num1 ")
    num2 = askforInt("please enter num2 ")
    if op == "/" and int(num2) == 0:
        return None
    if op == "+":
        res = int(num1) + int(num2)
    elif op == "-":
        res = int(num1) - int(num2)
    elif op == "*":
        res = int(num1) * int(num2)
    elif op == "/":
        res = int(num1) / int(num2)
    return res


print(calculator())
