import math
f = open("DATA41.txt", "r")
data = f.read().split()
masterlist = data
for i in range(0,10):
    houselist=[]
    objectlist=[]
    distancelist=[]
    olist=[]
    ttlist=[]
    demo=0
    end=301
    class House:
        def __init__(self, x, y ,p ):
            self.x = x
            self.y = y
            self.p = p
            

        def distance(self, xo, yo):
            d= math.sqrt((yo-self.y)**2+(xo-self.x)**2)
            return d

    x = masterlist[0]
    y = masterlist[1]

    hx=2
    hy=3
    hp=4
    while hp<=end:
        objectlist.append(House(int(masterlist[hx]), int(masterlist[hy]),
                                masterlist[hp]))
        hx+=3
        hy+=3
        hp+=3
    for i in objectlist:
        distancelist.append(i.distance(int(x),int(y)))

    for i in range(0, len(distancelist)):
                   olist.append(min(distancelist))
                   distancelist.remove(min(distancelist))
    third=olist[2]
    for i in olist:
        if i<=third:
            ttlist.append(i)
    total = len(ttlist)
    for i in objectlist:
        for k in ttlist:
            if i.distance(int(x),int(y))==k:
                if i.p == 'D':
                    demo+=1
                    ttlist.remove(k)
    del masterlist[0:end]
    print(round((demo/total*100), 1))


        
                            
