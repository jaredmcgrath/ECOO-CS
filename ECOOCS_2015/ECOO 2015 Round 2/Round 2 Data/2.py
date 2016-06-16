data=open("DATA21.txt","r").read()
class GameBoard:
    def __init__(self,raw):
        raw=raw.split("\n")
        self.board=[]
        for y in range(len(raw)):
            for x in range(len(raw[y])):
                
        
