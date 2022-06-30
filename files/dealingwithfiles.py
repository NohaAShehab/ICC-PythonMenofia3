
# file permissions r , w, x
""""""

"""
    --- when you deal with files  --> text files ---> (JSON)
    read  ----> 
    write ---> write form the starting (beginning of the file)
        ---> append to the file  
        
      ------------------------------- modes
      r : read file content
      w : write in the file starting from the first byte of it 
        -- file have data before ,,, erase content , overwrite --
      a : append at the end of the file 
      
         
"""
"""
        1- open the file 
            open("filename", mode of opening)
        2- do operation 
            read , readlines
            write, writelines
        3- close file 
            close
"""
" ------------------------ Read operation ---------------------------"
try:
    fileobj = open("files/names.txt", "r")
except Exception as e:
    print(e)
else:
    # if the file opened successfully
    print(fileobj)  # TEXTIOWRapper ,
    print(type(fileobj))

    # 2- to read file content into string
    # data = fileobj.read() # read file content in form of string
    # print(type(data))
    # print(data)
###########################################################################
    # read file content in to list ---> line by line
    # d = fileobj.readline()
    # print(d)
    # d = fileobj.readline()
    # print(d)
    # d = fileobj.readline()
    # print(d)
    #############################################################
    # read file content into a list .....
    # l =[]
    # for line in fileobj:
    #     # print(line)
    #     l.append(line)
    # print(l)
    ############################################33
    # lines = fileobj.readlines()
    ############################   read operation ##############################
    # ### at the end of the file
    mylines = fileobj.readlines()
    print(mylines)
    #### here we need to move the cursor to the beginning of the file
    fileobj.seek(0)
    data = fileobj.read()

    print(data)


    # 3- close the file
    fileobj.close()











