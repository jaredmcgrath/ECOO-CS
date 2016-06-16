class Boggle:
    def __init__(self,gameData):
        self.board = gameData[0:4]
        self.letters = []
        for y in range(4):
            for x in range(4):
                self.letters.append(Letter(self.board[y][x],x,y))
        self.words = gameData[4:]
        self.good = []
        self.lost = []
        self.short = []
        self.repeat = []
        for word in words:
            if len(word) < 3:
                self.short.append(word)
            elif word in self.good or word in self.lost:
                self.repeat.append(word)
            elif not self.isWordFound(word):
                self.lost.append(word)
            else:
                self.good.append(word)

    def getNearbyLetters(self,letter):
        potentialRelativePositions = [[-1,-1],[0,-1],[1,-1],[-1,0],[1,0],[-1,1],[0,1],[1,1]]
        nearbyLetters = []
        for position in potentialRelativePositions:
            nextLetter=self.letterFromPosition(letter.x+position[0],letter.y+position[1])
            if nextLetter is not None:
                nearbyLetters.append(nextLetter.char)
        return nearbyLetters
    def lettersFromChar(self,char):
        letters=[]
        for letter in self.letters:
            if letter.char == char:
                letters.append(letter)
        return letters
    def letterFromPosition(self,x,y):
        for letter in self.letters:
            if letter.x == x and letter.y == y:
                return letter
    def isWordFound(self,word):
        #word=word[::-1]
        #method must be changed to call on itself recursively
        for i in len(word):
            for letter in lettersFromChar(word[i]):
                if word[i+1] in self.getNearbyLetters(letter)
            
class Letter:
    def __init__(self,char,x,y):
        self.char = char
        self.x = x
        self.y = y

data=open("DATA40.txt","r").read().split("\n")
games=[]
games.append(Boggle(data[0:4]+data[5:5+int(data[4])]))
lineNumber = len(games[len(games)-1].words)+5
for i in range(4):
    gameBoard = data[lineNumber:lineNumber+4]
    gameWords = data[lineNumber+5:lineNumber+5+int(data[lineNumber+4])]
    games.append(Boggle(gameBoard+gameWords))
    lineNumber+=len(games[len(games)-1].words)+5
for game in games:
    print("Your score:",game.score,"("+str(len(game.good)),"good,",
          len(game.lost),"not found,",len(game.short),"too short,",
          len(game.repeat),"repeated)")
