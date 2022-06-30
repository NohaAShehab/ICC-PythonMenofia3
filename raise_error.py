def askfornum(message):
    num  =input(message)
    if num.isdigit():
        return num

    return askfornum(message)


def divnums():
    num1 = int(askfornum("please enter num1 : "))
    num2 = int(askfornum("please enter num2 : "))
    if not num2:
        raise Exception("Cannot divide by zero, Please start the application ")

    print(f"num1 = {num1}, num2={num2}..... ")
    print("---------------------------")
    print("--------------------------------------------")
    # res = num1 / num2
    return num1 / num2


x=divnums()
print(x)

