def problem6():
    import random
    def creatematris():  #this funtion inside the main problem6() function is for creating random matrices to be used
        a=[]
        for i in range(4):
            b=[]
            for j in range(4):
                x=random.randint(1,4)
                b.append(x)
            a.append(b)
        return a
#print(creatematris())
    
    "----------------"
    def check():                  #this function put all the rows, columns and diagonals summations in a list (mylist)
        mylist=[]
        matrix=creatematris()
        #print(matrix)
        dleft=0
        dright=0
        for i in range(4):
            dleft+=matrix[i][i]
            dright+=matrix[i][3-i]
            rnum=0
            cnum=0
            for j in range(4):
                rnum+=matrix[i][j]
                cnum+=matrix[j][i]
            mylist.append(rnum)
            mylist.append(cnum)
        mylist.append(dleft)
        mylist.append(dright)
        return mylist,matrix
        #print(mylist)

    "-------------------"
    counter=0
    while True:       #here, all th data in the mylist should be equal, so order to check that we look repeats of the first element in mylist.
        counter+=1
        mylist,matrix=check()
        number=mylist.count(mylist[0])
        number2=len(mylist)
        if(number!=number2):    #if first element's repeats is not equal to the length of the list, our matrix is not magic matrix
            continue
        else:
            break
    print("the number of random matrices created:",counter)   
    print("the magic square found is",matrix)


problem6()
