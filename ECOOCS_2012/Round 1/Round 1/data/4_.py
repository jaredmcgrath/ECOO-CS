class Board:
    def __init__(self,raw):
        self.tiles=[raw[i*4:i*4+4] for i in range(4)]

    def locationsFromL(self,c):
        coords=[]
        for y in range(4):
            for x in range(4):
                if self.tiles[y][x]==c:
                    coords.append([x,y])
        return coords

    def adjTiles(self,x,y):
        tiles=[]
        for relY in range(-1,2):
            for relX in range(-1,2):
                if relX==0 and relY==0:
                    continue
                try:
                    tiles.append([x+relX,y+relY,self.tiles[y+relY][x+relX]])
                except:
                    continue
        return tiles

data=open("DATA41.txt","r").read().split("\n")
for case in range(10):
    score=0
    good=[]
    notFound=[]
    short=[]
    repeated=[]
    board=Board(x for i in data[:4] x+=i)
    N=int(data[4])
    for word in data[5:N]:
        for 
        if len(word) <3:
            short.append(word)
        elif word in good.append(short):
            repeated.append(word)
        elif 
    
    data=data[N+5:]
