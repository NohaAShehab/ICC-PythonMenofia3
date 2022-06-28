"""tuple is built-in data type like list,

    tuple is immutable datatype

"""
"0- to define tuple"
t = ()
myt = ("Ahmed", "Ali", "Mahmoud")
courses = tuple(["Ahmed", "Ali", "Mostafa"])
print(type(myt))
"1- get the length of the tuple"
print(len(courses))

"2- access elements in the list --> print element , update element"
names = ("Shymaa", "Khaled", "Shokr", "Ahmed", "Abdelrahman", "Monir", "Ayman", "Esraa", "Ahmed")

print(names[4])
# names[3]="Ahmed"  #not valid operation
# # 'tuple' object does not support item assignment
# print(names)


"3- concatenation"
content = ("python history", "syntax", "variables")
part2 = ("string", "integers", "lists", "tuples")
myt = content + part2
print(myt)

"4- check the membership"
if "Ahmed" in names:
    print("found")

"5- min , max ---> tuple items must be the same types"
vals = (33, 45, 67, 88, 98, 9)
print(min(vals))  # iteratable
print(max(vals))

"6- loop over the list content "

for item in names:  # loop over the list elements
    print(f"item= {item}")

for index, name in enumerate(names):
    print(f"{index}: {name}")

"6- tuple of one element "

t = ("python",)  # tu# ple of one item ---> ,
print(type(t))

"7- casting between the tuple and list ? "

t = ("python", "django", "flask")
print(type(t))
"cast tuple to a list  "
t = list(t) # cast tuple into list
print(type(t))


"cast list to a tuple"
l = ["55","666", "fjsdf", True]
l = tuple(l)
print(type(l))

l1 = ["Ahmed", "Ali", "Hossam"]
l2 = l1  # refer to the same part in the memory

l1[0]=["Ahmed Mohamed"]
print(l1, l2)

########################
mm = 10 # value
nn = mm

mm = "iti"
print(nn, mm)




