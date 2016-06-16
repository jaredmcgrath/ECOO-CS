class BallTeam:
    teams=0
    sumBA=0
    sumSA=0
    def __init__(self,*teamData):
        self.name = teamData[0]
        self.gamesPlayed = int(teamData[1])
        self.atBats = int(teamData[2])
        self.runs = int(teamData[3])
        self.totalHits = int(teamData[4])
        self.twoHits = int(teamData[5])
        self.threeHits = int(teamData[6])
        self.homeRuns = int(teamData[7])

        self.oneHits = self.totalHits-self.twoHits-self.threeHits-self.homeRuns

        self.BA = self.totalHits/self.atBats
        self.SA = (self.oneHits+2*self.twoHits+3*self.threeHits+4*self.homeRuns)/self.atBats

        BallTeam.sumBA += self.BA
        BallTeam.sumSA += self.SA
        BallTeam.teams += 1

def output():
    print(data[0])
    print("="*20)
    for team in teams:
        print(team.name+":",format(team.BA, ".3f")[1:],format(team.SA, ".3f")[1:])
    print("="*20)
    print("Big 10 Av:",format(BallTeam.sumBA/BallTeam.teams, ".3f")[1:],format(BallTeam.sumSA/BallTeam.teams, ".3f")[1:])

data = open("DATA12.txt","r").read().split("\n")
teams = []
for i in range(1,len(data)):
    teams.append(BallTeam(*data[i].split()))
output()
