data=open("DATA30.txt","r").read().split("\n")
for case in range(2):
    print("case: " + str(case))
    carNumber = (data[case*2])
    carNumber = int(carNumber)
    print(carNumber)
    train = (data[case*2+1])
    train = train.split()
    train2 = []
    for i in train:
        train2.append(int(i))
    print(train2)
    sortedCars = 0
    totalscore = 0
    index = 0
    for n in range(carNumber)-1:
        nextmove = 0
        for i in train2:
            if i > nextmove and i != carNumber:
                movescore = index
                nextmove = i
                print("move",nextmove)
            index+=1
        train2.remove(nextmove)
        train2=[nextmove].append(train2)
        totalscore+=index
        print(totalscore)
    print(train2)
    
