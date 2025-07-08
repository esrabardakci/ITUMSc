names = ["David", "Michael", "John", "James", "Greg", "Mark", "William", "Richard", "Thomas", "Steven", "Mary", "Susan", "Maria", "Karen", "Lisa", "Linda", "Donna", "Patricia", "Debra", "Eric"]
scores = [99, 87, 78, 86, 68, 94, 76, 97, 56, 98, 76, 87, 79, 90, 73, 93, 82, 69, 97, 98]

def problem5(names,scores):
    mylist=[]
    namelist=[]
    name=[]
    grade=[]
    n=[0] #this will be used for indexing at the end
    scores,names=zip(*sorted(zip(scores,names),reverse=True)) #here, we sorted 2 list according to the scores, keeping the index info between two lists

    for i in scores:
        a=i
        mylist.append(a)      #here, we convert tuple to list

    for i in names:
        a=i
        namelist.append(a)


    for j in range(3):
        highest=mylist[0]        #this part is for getting top 3 grades with names
        index=0
        start=-1
        for i in mylist:
            start+=1
            if i>highest:
                highest=i
                index=start
        name.append([namelist[index],highest])
        namelist.remove(namelist[index])
        mylist.remove(highest)
        "---------------------------------"

        a=mylist.count(highest)
        k=[]
        if a!=0:                        #in case of repeats of the same grades, we have a check point here
            for i in range(len(mylist)):
                if mylist[i]==highest:
                    highest=mylist[i]
                    name.append([namelist[i],highest])
                    k.append(i)
    
        for i in range(len(k)):
            namelist.remove(namelist[0])  #our list is already sorted so, each time we remove an element, next will be new zero index and we will do this until we reach the number of highest elements of that step
            mylist.remove(highest)   #each time, we delete corresponding score of removed names

        n.append(len(name)) #this will be used for indexing, while printing top 3

#this part for outputs  
    m=0
    p=[]
    for i in range(3): #this always print top 3, taking in the consideration of the possible repeats of top 3 grades
        h=[]
        s=[]
        p.append(name[n[m]:n[i+1]]) #here, each time, we slide ranges to be printed
        c=abs(n[m]-n[i+1])
        
        while (c!=0):
            h.append(p[i][c-1][0])
    
            c-=1
        s.append(p[i][c-1][1])
        print("rank",i+1,h,"score: ",s[0])
        m+=1


problem5(names,scores)
