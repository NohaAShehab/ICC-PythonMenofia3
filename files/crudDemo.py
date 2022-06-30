""""""
"""
    registration system 
    name 
    email 
    password 
    -----> data saved in users.txt file 
    
    display all users 
    user ---> edit , delete his info
    
    login to the system 

"""
def displayAllusers():
    try:
        fileobj = open("users.txt","r")
    except Exception as e:
        print(e)
    else:
        users = fileobj.readlines()
        print("name:email:password")
        for user in users:
            print(user.strip("\n"))

        return users

def edituser():
    allusers = displayAllusers()  # list of users
    """ ask about the user your want to delete """""
    usertoedit = input("please enter the email of the user you want to edit : ")
    for l in allusers:
        user_info = l.strip("\n")
        user_info = user_info.split(":")
        print(user_info)
        if user_info[1] == usertoedit:
            print("userfound")
            ####################33 ask about edit
            part_to_edit = input("please choose n for edit name, e for edit email , p for password, a for all ")
            if part_to_edit == "n":
                newname = input("please enter your name ")
                user_info[0]= newname
            elif part_to_edit == "e":
                newemail = input("please enter your email ")
                user_info[1]= newemail
            elif part_to_edit == "p":
                password = input("please enter your password ")
                user_info[2] = password
            elif part_to_edit == "a":
                newname = input("please enter your name ")
                user_info[0] = newname
                newemail = input("please enter your email ")
                user_info[1] = newemail
                password = input("please enter your password ")
                user_info[2] = password

            print(user_info)
            updated_user=":".join(user_info)
            updated_user = f"{updated_user}\n"
            userindex = allusers.index(l)
            print(userindex)
            allusers[userindex] = updated_user
            break
    else:
        return edituser()

    w = open("users.txt", "w")
    w.writelines(allusers)
    w.close()




def deleteUser():
    allusers = displayAllusers()  # list of users
    """ ask about the user your want to delete """""
    usertodelete = input("please enter the email of the user you want to delete : ")
    print(usertodelete)

    for l in allusers:
        user_info= l.strip("\n")
        user_info = user_info.split(":")
        if user_info[1] == usertodelete:
            # # remove the user from the file
            print("userfound")
            # ## remove the line from the list --->
            allusers.remove(l)
            break
    else:
        return deleteUser()

    # # write the new list after delete
    w = open("users.txt", "w")
    w.writelines(allusers)
    w.close()







def displayloggedinMenu():
    choice = input("please enter your choice , d display all users, e edit user, x delete user ")
    if choice == "d":
        displayAllusers()
    elif choice == "e":
        edituser()
    elif choice == "x":
        deleteUser()

    else:
        displayloggedinMenu()


def register():
    name = input("please enter your name: ")
    email = input("please enter your email: ")
    password = input("please enter your password: ")

    ##### save in users.txt
    try:
        fileobj = open("users.txt", "a")
    except Exception as e:
        # return  register()
        print(e)
    else:
        # 1- prepare the data I need to save
        userinfo = f"{name}:{email}:{password}\n"
        fileobj.write(userinfo)
        fileobj.close()


def login():
    print("---- login-----")
    email = input("please enter your email: ")
    password = input("please enter your password: ")
    try:
        fileobj = open("users.txt", "r")
    except Exception as e:
        print(e)
    else:
        # read file content into list --->
        users = fileobj.readlines()  # all users in the list
        print(users)
        # split each line according seprator
        # # check if email, password ---> exists --> successeded
        for user in users:
            # split each line according seprator
            userdata = user.strip("\n")
            userinfo = userdata.split(":")
            # print(userinfo)
            if userinfo[1] == email and userinfo[2] == password:
                print("logged in successfully")
                displayloggedinMenu()
                break
        else:
            print("No such user , you can register here ")
            register()

        # compare field2 , 3 with email and password
