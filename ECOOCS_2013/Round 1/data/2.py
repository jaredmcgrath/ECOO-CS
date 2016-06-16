import math
cases=open("DATA22.txt","r").read().split("\n")
for case in cases:
    if case == "":
        continue
    output=""
    for baseNumStr in case.split():
        baseNumStr=baseNumStr[::-1]
        baseNumInt=0
        for num in [str(int(baseNumStr[i])*2) for i in range
                    (0,len(baseNumStr),2)]:
            for digit in num:
                baseNumInt+=int(digit)
        for num in [baseNumStr[i] for i in range(1,len(baseNumStr),2)]:
            baseNumInt+=int(num)
        output += str(int(math.ceil(baseNumInt/10)*10) - baseNumInt)
    print(output)
