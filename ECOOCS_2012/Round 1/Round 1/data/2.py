data=open("DATA22.txt","r").read().split("\n")
promoter="TATAAT"
count=1
def getTranscription(transcription):
    for termLen in range(6,int(len(transcription)/2)):
        for i in range(len(transcription)-(termLen*2)):
            testSeq = transcription[i:i+termLen]
            for j in range(i+termLen,len(transcription)-termLen):
                if testSeq == getComplimentaryBases(transcription[j:j+termLen],False)[::-1]:
                    return transcription[:i]

def getComplimentaryBases(bases,isRNA):
    newBases=[]
    for base in bases:
        if base == "A":
            if isRNA:
                newBases.append("U")
            else:
                newBases.append("T")
        elif base == "T":
            newBases.append("A")
        elif base == "C":
            newBases.append("G")
        elif base == "G":
            newBases.append("C")
    newBases="".join(newBases)
    return newBases

for strand in data:
    transcription=""
    for i in range(len(strand)):
        if strand[i:i+6] == promoter:
            transcription = strand[i+10:len(strand)]
            print(str(count)+":", getComplimentaryBases(getTranscription(transcription),True))
            count+=1

