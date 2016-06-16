data=open("DATA31.txt","r").read().split("\n")
for case in range(10):
    score=0
    N=int(data[case*2])
    numbers=[int(x) for x in data[case*2+1].split()]
    for n in numbers:
        i=numbers.index(n)
        score+=i
        for x in numbers[i:]:
            if x!=max(numbers):
                score=1
    print(score)
            
