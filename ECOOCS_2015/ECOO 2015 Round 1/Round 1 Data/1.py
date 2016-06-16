import math
data=open("DATA12.txt","r").read().split("end of box\n")
for case in data:
    r = 0
    o = [0,0,0,0,0,0,0]
    t=0
    colours = case.split()
    for colour in colours:
        if colour == "red":
            r+=1
        elif colour == "brown":
            o[0]+=1
        elif colour == "violet":
            o[1]+=1
        elif colour == "blue":
            o[2]+=1
        elif colour == "pink":
            o[3]+=1
        elif colour == "yellow":
            o[4]+=1
        elif colour == "green":
            o[5]+=1
        elif colour == "orange":
            o[6]+=1
    for x in o:
        t += 13*math.ceil(x/7)
    t+=16*r
    if t!=0:
        print(t)
