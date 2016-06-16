data=open("DATA20.txt","r").read().split("\n")
for case in range(5):
    print("case: " + str(case))
    print(data[case*3])
    print(data[case*3+1])
    print(data[case*3+2])
