from math import inf
data=open("DATA22.txt","r").read().split("\n")
for case in range(10):
    #print("Case:",case)
    Aw,Ah,Bx,By,Sx,Sy=(int(x) for x in data[case*6].split(" "))
    if Sx==0:
        print("MMMMM")
        continue
    targets=[(int(x),int(y),int(z)) for x,y,z in [data[case*6+i+1].split(" ") for i in range(5)]]
    if Sy!=0:
        m=[Sy/Sx]
        b=[By-Sy/Sx*Bx]
        maxX=[Bx,Sx*(Ah-By)/Sy+Bx]
        #generate functions that describe the balls path
        while maxX[len(maxX)-1]<Aw:
            #determine slope of this line
            #it alternates +/- Sy/Sx
            if len(m)%2==0:
                m.append(Sy/Sx)
            else:
                m.append(-Sy/Sx)
            #determine y-int of line
            if m[len(m)-2]>0:
                b.append(Ah-m[len(m)-1]*maxX[len(maxX)-1])
            else:
                b.append(-m[len(m)-1]*maxX[len(maxX)-1])
            #determine max X of new function
            if m[len(m)-1]>0:
                maxX.append((Ah-b[len(b)-1])/m[len(m)-1])
            else:
                maxX.append(-b[len(b)-1]/m[len(m)-1])
    else:
        m=[0]
        b=[By]
        maxX=[inf]
    #target hitting time babyyyyyyyy
    output=""
    for Th,Tx,Ty in targets:
        ind=0
        for ind,x in enumerate(maxX):
            if x>Tx:
                break
        y=m[ind-1]*Tx+b[ind-1]
        if Ty-Th<=y<=Ty:
            output+="H"
        else:
            output+="M"
    print(output)
        
