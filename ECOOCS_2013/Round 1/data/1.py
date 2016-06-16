data=open("DATA12.txt","r").read().split("\n")
take=0
serve=0
nextNumber=int(data[0])
for line in data:
    if line[0] == "T":
        take+=1
        nextNumber+=1
        if nextNumber > 999:
            nextNumber=1
    elif line[0] == "S":
        serve+=1
    elif line[0] == "C":
        print(take,take-serve,nextNumber)
        take=0
        serve=0
