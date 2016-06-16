def encode(data):
    words=data.split()
    n=0
    for word in words:
        n+=len(word)
    outputSeq=""
    splitSeq=[]
    i=0
    while len(outputSeq) < n:
        for word in words:
            if not len(word) < i+1:
                outputSeq+=word[i]
        i+=1
    for word in words:
        splitSeq.append(outputSeq[:len(word)])
        outputSeq=outputSeq[len(word):]
        #print(outputSeq)
    return " ".join(splitSeq)

def decode(data):
    words=data.split()
    data="".join(words)
    output=[]
    for i in range(len(words)):
        output.append(data[i])
    data=list((data[len(words):])[::-1])
    while data != []:
        for i in range(len(output)):
            if len(output[i]) < len(words[i]):
                output[i]+=data.pop()
    return " ".join(output)
                
data=open("DATA12.txt","r").read().split("\n")
for i in range(10):
    if data[i*2] == "encode":
        print(encode(data[i*2+1]))
    else:
        print(decode(data[i*2+1]))
