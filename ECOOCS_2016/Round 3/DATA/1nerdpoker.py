data=[(int(y[0]),int(y[1])) for y in [x.split(" ") for x in open("DATA12.txt","r").read().split("\n") if x != ""]]
for case in data:
    N=case[0]
    S=case[1]
    count=0
    while N>1.5:
        N=N-N/S
        count+=1
    count+=S
    print(count)
