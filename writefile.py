""""""


"""

    1- open file("filename", mode )
    
    mode --> write 
        w mode , when open file with mode write, 
        if file not exists  ---> python will create file -if the permissions allow this-
        ---> if the file exists  ---> will open file for writing starting from the first byte of the file 
        
    mode --> append 
     a mode , when open file with mode append, 
        if file not exists  ---> python will create file -if the permissions allow this-
        ---> if the file exists  ---> will open file for writing starting from the end of the file 

"""

# try:
#     fileobj = open("files/mycv.txt", "w")
# except Exception as e:
#     print(e)
# else:
#     print(fileobj)
#     # fileobj.write("My name is noha\n")  ###
#     # fileobj.write("I works at iti ")
#
#     #############################33
#     # wirtelines  ---> accept iterable object
#     fileobj.writelines(["name\n", "id\n", "python\n", "iti\n"])
#
#     fileobj.close()





# #################### append to the file

# try:
#     fileobj = open("files/mycv.txt", "a")
# except Exception as e:
#     print(e)
# else:
#     print(fileobj)
#     fileobj.write("My name is noha\n")  ###
#     fileobj.write("I works at iti ")
#
#     #############################33
#     # wirtelines  ---> accept iterable object
#     # fileobj.writelines(["name\n", "id\n", "python\n", "iti\n"])
#
#     fileobj.close()

#############################33 special case with write and appned

# try:
#     fileobj = open("files/mycv.txt", "w")
# except Exception as e:
#     print(e)
# else:
#     print(fileobj)
#     fileobj.write("My name is noha\n")  ###
#     fileobj.seek(2)
#     fileobj.write("########################")
#
#     fileobj.close()


try:
    fileobj = open("files/mycv.txt", "a")
except Exception as e:
    print(e)
else:
    print(fileobj)
    fileobj.write("My name is noha\n")  ###
    fileobj.seek(2)  # ### has no effect
    fileobj.write("########################")

    fileobj.close()