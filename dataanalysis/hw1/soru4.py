def problem4(x):
    file=open(x,'r')
    country='Turkey'
    lines=[]
    update=[]
    year=[]
    counter=-1
    for line in file:
        counter+=1
        lines.append(line)   #here we get all the lines in a lis
        if country in line:
            k=counter          #here we obtain line info of Turkey
    data=lines[k].split(";")  #we need data of k. line (Turkey)
    years=lines[0].split(";")  #we also need years' info

    for i in range(1,len(data)):
        update.append(float(data[i])) #here, from the first number data to the last, we got gdp info as float numbers
    #print(update)

    for i in range(1,len(years)):
        year.append(int(years[i]))  #here, we got years in a new list as int data
    #print(year)

    percent=[]
    for i in range(len(update)-1): #here, we got percentages of each year increase
        a=update[i+1]
        b=update[i]
        x=a-b
        result=(x*100)/b
        percent.append(result)
    #print(percent)

    "---------------------------"
    highest=percent[0]
    index=0
    start=-1
    for i in (percent):
        start+=1
        if i>highest:
            highest=i
            index=start
    print("the highest increase happened in the year",year[index+1])   #here, we first detected index of highest percentage increase, then using index info, we obtained year info
    #print(highest,index)

    dec=[]
    for i in range(len(update)-1):
        if update[i+1]<update[i]:  #here we get index info of decreased gdps
            a=i+1
            dec.append(a)
    #print(dec)


    dyear=[]
    for i in (dec):
        dyear.append(year[i])   #here using index info of decreased years, we printed years
    print("years that GDP per capita decreased compared to previous year:\n",dyear)

    file.close()

problem4('gdp_per_capita.csv')
