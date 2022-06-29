"""
    all data structure in python ---> list , tuple , dict --> allow values with data types
    int , string , list ---> built in classes in python
    ---> all classes in python ---> extend object class
    --> has instance magic method __len__ ---> implement for this method --. return int
    ---> dictionary ---> OOP

"""

myinfo = ["noha", "python", 42, "Menofia"]  # list ---> index start 0

## represent data in more readable form
"""
    set ---> 
    ---> no data duplication
    --> unordered data structure 
    ---> no index to access elements 
    ---> you loop over it 
    --> mutable
"""

### vowels  --->
v = "aeiou"
v = ["a", "e", "i", "o", "u"]

## set
# vowels = {"a", "e", "i", "o", "u", "a"}
# vowels.add("x")  #
# vowels.pop()  # pop random element
# vowels.remove("e")
# print(vowels, type(vowels))
# ################################################
"""Dictionary 
    One of the basic data struncture in python 
    --> key value pair ((no index))
    --> you can access the elements using the key 
    --> no duplication in keys 
    --> dictionary ---> unordered ---> till python 3.6 
    from python 3.7 ---> dictionary is ordered in memory
"""

"1- define dic"
d = {}
print(type(d))

dic_info = {
    "name": "noha",
    "track": "python",
    "branch": "Menofia"
}

data = dict([("age", "30"), ("year", 2022)])

"2- access dic elememts"
print(dic_info["name"])
dic_info["name"] = "Noha Shehab"  # update
# add email to the info
dic_info["email"] = "nshehab@iti.gov.eg"  # add new key value pair to the dic

"3- get no of key-value pairs"
print(len(dic_info))

"4- delete key value pair from the dictionary  "
poped_val = dic_info.pop("track")  # popping the value of the certain key
print(poped_val)
print(dic_info)

""" del function delete any object(variable) from the memory """
del dic_info["email"]  # remove element form the dic

"""5- display keys, values of dictionary """

dic_info = {
    "name": "noha",
    "track": "python",
    "branch": "Menofia"
}

# dkeys = dic_info.keys()  # object from type dict_keys -->  can be casted to list or tuple
# print(dkeys, type(dkeys))
# # cast dkeys to list
# dkeys = list(dkeys)
# print(dkeys[0])


dvalues = dic_info.values()  # object from type dict_values -->  can be casted to list or tuple
print(dvalues, type(dvalues))
# cast dvalues to list
dvalues = list(dvalues)
print(dvalues[0])

################
"6- get keys and values in one step ? "
dic_items = dic_info.items()  # dict_items  ---> can be casted to list or tuple
# #################### contain each element in form of tuples
print(dic_items)
dic_items = list(dic_items)
print(dic_items)

########################
"7- loop over the dictionary"

# for i in dic_info:
#     print(f"----> {i}")  # keys

for i in dic_info:
    print(f"----> {i} , {dic_info[i]}")  # keys

for k, v in dic_info.items():
    print(f"----> {k} , {v}")  # keys

"8- update dictionary ---> check key not exists ---> will add it to the dic, if exists  --> update the value  "

mostafa_infoo = {"name": "Mostafa", "track": "python", "intake":42}
work = {"company": "Microsoft", "salary": 5000, 'intake': 41}
mostafa_infoo.update(work)
mostafa_infoo[10] = "iti"  # 10 here is considered as key
print(mostafa_infoo)

"9-check if the value exists in the dic  "
# if "Mostafa" in mostafa_infoo:  # check in the keys
#     print("found")
# else:
#     print("not found")

if "Mostafa" in mostafa_infoo.values():  # check in the keys
    print("found")
else:
    print("not found")


# dic_info.clear() ## remove all key-value pairs form the dic


"10 -- can we cast dict to list ? "

d = {'name': 'Mostafa', 'track': 'python', 'intake': 41, 'company': 'Microsoft', 'salary': 5000, 10:"iti"}
# d = list(d)  # return with the keys of the dictionary

""" enumerate  ---> create index for itertable """
for i in d:
    print(f"{i}, {d[i]}")
#
for k , v in enumerate(d):
    print(f"{k}, {v}, {d[v]}")

