#this program is a lost cause and a waste of 5 hours of my life. kill me
class Game:
    def __init__(self, initData):
        initData = initData.split()
        self.length = eval(initData[4]+"e"+initData[5])
        self.pins = [Pin(eval(initData[0]+"e"+initData[1]),
                         eval(initData[2]+"e"+initData[3]),1)]
        self.N = int(initData[6])
        
        self.calcPins()

    def calcPins(self):
        xint = self.pins[0].x
        yint = self.pins[0].y
        
        xDiff = 0.5*self.length/3
        yDiff = 3**0.5/2*self.length/3

        for depth in range(1,4):
            y = yDiff*depth+yint
            for i in range(depth+2):                   
                x = (-depth)*xDiff+xDiff*i*2+xint
                self.pins.append(Pin(x,y,len(self.pins)+1))
            
    def pinNumFromPos(self,posStr):
        d2 = posStr.split()
        for i in range(len(d2)):
            d2[i] = float(d2[i])
        for pin in self.pins:
            d1 = pin.roundedPos(self.N).split()
            for i in range(len(d1)):
                d1[i] = round(float(d1[i]),len(str(abs(d2[i]))[2:]))
            print(d1,d2)
            if getDiff(d1[0],d2[0]) < eval("10e"+str(-len(str(d1[0]))-5)) and getDiff(d1[2],d2[2]) < eval("10e"+str(-len(str(d1[2]))-5)) and d1[1]==d2[1] and d1[3]==d2[3]:
                return pin.num

class Pin:
    def __init__(self,x,y,num):
        self.x = x
        self.y = y
        self.num = str(num)

    def roundedX(self,N):
        return roundPos(self.x,N)
    
    def roundedY(self,N):
        return roundPos(self.y,N)

    def roundedPos(self,N):
        return self.roundedX(N)+" "+self.roundedY(N)

def roundPos(n,N):
    form = "{:0."+str(N)+"e}"
    m = n
    n = form.format(n)
    if n[len(n)-3] == "-":
        if m>=0:
            n = n[:N+2]+" "+str(int(n[len(n)-3:]))
        else:
            n = n[:N+3]+" "+str(int(n[len(n)-3:]))
    else:
        if m>=0:
            n = n[:N+2]+" "+str(int(n[len(n)-2:]))
        else:
            n = n[:N+3]+" "+str(int(n[len(n)-2:]))
    return n

def getDiff(n1,n2):
    if n2 < n1:
        return n1-n2
    else:
        return n2-n1

data=open("DATA31.txt","r").read().split("\n")
for i in range(0,10):
    game = Game(data[i*6])
    output=[]
    for j in range(1,6):
        output.append(game.pinNumFromPos(data[i*6+j]))
    print(output)
    output=" ".join(output)
    print(output)
        
