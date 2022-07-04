# def addnums(x,y):
#     return x + y
#
# print(addnums(4,5))


#
# res = lambda x,y: x+y
# print(res)
# print(res(5,6))


### lists ,

## function return function

# def sumnum(num):
#     res = num + 10
#     print(res)
#     return lambda: num * num
#
#
# x = sumnum(10)
# print(type(x))
# print(x())


# ###################### mop

l = [34, 9, 1, 56, 7, 8, 4]


def multwo(element):
    return element * 2


print(l)
# for index, item in enumerate(l):
#     l[index] = multwo(item)
#
# print(l)


# myl =map(lambda x:x*2, l)  #map function --> apply functionality on iterable ,,,
# # retrun with map object ---> can be casted to a list
# print(myl)
# print(list(myl))


# filter
# print(l)
# myl = filter(lambda x: x % 2 == 0, l)  # map function --> apply functionality on iterable ,,,
# # retrun with map object ---> can be casted to a list
# print(myl)
# print(list(myl))

# ####################################################

l = ["Ahmed", "Mohamed", "Ali", "Omar", "Mostafa"]

# for n in l:
#     print(n)
# newl = iter(l)
# print(newl)  # list_iterator objects
# print("-----------------")
# print(next(newl))
# print(5+7)
# print("==============================")
# print(next(newl))
# print(next(newl))
# print(next(newl))
# print(next(newl))
# print(next(newl))


# # retrun with integer


# def myfun():
#     for i in range(5):
#         return i
#
#
# print(myfun())
# print(myfun())
# print(myfun())


def myfun():
    for i in range(100000000):
        yield i

g= myfun()
print(g)  # generator object

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
