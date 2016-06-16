data=open("DATA12.txt","r").read().split("\n")
for case in range(10):
    passers=0
    weight=[int(x) for x in data[0].split()]
    total=0
    for worth in weight:
        total+=worth
    N=int(data[1])
    for i in range(2,len(data[2:N+2])+2):
        marks=[int(x) for x in data[i].split()]
        avg=((weight[0]*marks[0])+(weight[1]*marks[1])+(weight[2]*marks[2])+(weight[3]*marks[3]))/total
        #print(avg)
        if avg>=50:
            passers+=1
    print(passers)
    data=data[N+2:]
    
