#####
"1- to define list"
l  = []  # empty list
names = ["Shymaa", "Khaled", "Shokr", "Ahmed","Abdelrahman", "Monir", "Ayman", "Esraa", "Ahmed"]
myl=list(["python", "django", 20, names])
print(myl)

"1- get the length of the list"
print(len(names))
"2- access elements in the list --> print element , update element"
print(names[4])
names[3]="Ahmed"
print(names)
# names[10] = "Baraa fayez Soliman"  # IndexError: list assignment index out of range

"3- add new element to the list "
"3-1 add element at the end of the list"
names.append("Baraa fayez Soliman")
print(names)
"3-1 insert element at certain index"
names.insert(2, "Abdullah")
print(names)

"4- remove element from the list "
"####  pop"
popped=names.pop()  # remove the last element from the list, return with it.
print(names, popped)
'# remove element at certain index'
popped_item = names.pop(3)  # using index
print(names, popped_item)
" # remove element ---> I know the element itself"
x=names.remove("Ahmed")  # remove the first occurrence of the element. ## the element itself
print(names, x)

"4- sort the list elements"
names = ["Shymaa", "Khaled", "Shokr", "Ahmed","Abdelrahman", "Monir", "Ayman", "Esraa", "Ahmed"]
# names.sort()  # sort the names list ascending
# print(names)
names.sort(reverse=True)  # sort the names list ascending
print(names)

# ### sort only available with variables from same datatypes
# l = ["iti", "python", 2022]
# l.sort()  # TypeError: '<' not supported between instances of 'int' and 'str'

"5- reverse list elements"
l = ["iti", "python", 2022]
l.reverse()
print(l)

# ##################################
"6- extend list elements"
content = ["python history", "syntax", "variables"]
part2 = ["string", "integers", "lists", "tuples"]
content.extend(part2)
# print(content)

###################
"7- list concatenation"
newl = content + part2 + ["Ahmed", "Ali", "Abdallah"]
print(newl)


################
"8- check the membership"
if "Ahmed" in names:
    print("found")

#######################
"9- min , max ---> list items must be the same types"
vals = [33, 45, 67, 88, 98, 9]
print(min(vals))
print(max(vals))

########################
"10- loop over the list content "

for item in names:  # loop over the list elements
    print(f"item= {item}")


# i = 0
# for item in names:  # loop over the list elements
#     print(f"item {i}= {item}")
#     i+=1


# enumerate ---> create index for itertable
# enumerate(names) ===> enum object
mm = enumerate(names)
print(enumerate(names)) ## can be iterated using loops to --> index, value
# for index, item in enumerate(names):
#     print(f"{index}: {item}")


for abbas, fernas in enumerate(names):
    print(f"{abbas}: {fernas}")


print("--------------------------------")

