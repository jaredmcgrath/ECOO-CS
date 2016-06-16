import math
data=open("DATA22.txt","r").read().split("\n")
for case in range(int(len(data)/2)):
    W = int(data[case*2])
    words = data[case*2+1].split()
    currentWordIndex = 0
    output = []
    i = 0
    while currentWordIndex <= len(words)-1: #while we havent added all words
        if i==0 and len(words[currentWordIndex]) <= W: #if we're at the leftmost char and can fit the next whole word
            output.append(words[currentWordIndex]) #add word
            i+=len(words[currentWordIndex]) #move current line position
            currentWordIndex+=1 #move to next word
            
        elif len(words[currentWordIndex]) > W: # if the word doesnt fit on one line. if already on new line, blank one is left in and removed later
            #must loop through in case word doesnt fit on 2 or more lines
            #words that dont fit in one line begin on a fresh line
            wordPos=0 #current character index in the word
            for line in range(math.ceil(len(words[currentWordIndex])/W)): #while the current line is less than total number of lines needed
                try:
                    output.append("\n" + words[currentWordIndex][wordPos:W*(line+1)]) #move to new line, print W chars. will throw error on last line
                except:
                    output.append("\n" + words[currentWordIndex][wordPos:])#when last line doesnt print, just print remianing chars to new line
                    break #loop finishes here
                wordPos = W*(line+1)#update where we left off with the word after printing line
            i = len(words[currentWordIndex])%W #update the line character pointer
            if i == 0: #if word fits into lines evenly, i will be 0 but a linebreak needs to be inserted
                output.append("\n")
            currentWordIndex+=1 #move to next word
            
        elif len(words[currentWordIndex])+1 <= W-i: #if the remaining chars <= len(word) + 1 for a space
            output.append(" " + words[currentWordIndex]) #append space then word
            i+=len(words[currentWordIndex]) + 1 #adjust current line pos
            currentWordIndex+=1 # next word
            
        else: #under the condition len(word) + 1>W-i (word will fit on one line, but not enough room on this one)
            output.append("\n") #move to new line
            i = 0 #reset line char pointer
    output = "\n".join(filter(None, "".join(output).split("\n"))) #remove empty string and join the list into a single string for output
    print(output + "\n=====")
    
                
                
