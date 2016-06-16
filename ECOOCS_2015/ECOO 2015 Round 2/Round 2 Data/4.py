class Rect:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.area =

data=open("DATA41.txt","r").read().split("\n")
lineNum=0
for i in range(10):
    rects=[]
    for j in range(int(data[lineNum])):
        size = data[lineNum+j+1].split()
        rects.append(Rect(int(size[0]),int(size[1])))
    
