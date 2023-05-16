import re
import sys
from collections import Counter

saveExpression = "title"
ProssesedArray = []

## this desides what to call and what to do
## just a while loop
running = True
while running:
    inp = input("launched, type help to view commands, imput here: ")
    
    ## help printout
    if inp == "help" :
        print("regex: lets you change the regular expresion that transfers files from")
        print("useex: uses the given or default regular expresion to set up the files")
        print("PTclear: clears the ProssesedText.txt file")
        print("PAclear: clears the Prossesed array")
        print("allclear: clears all prossesed files")
        print("commands:")
        print("commands:")
        print("commands:")
    
    ## change regex
    if inp == "regex" :
        saveExpression = input("lines containing ___ should be saved: ")

    ## cleans the data
    if inp == "useex" :
        #makes allLines array, has all lines

        with open("BrowserHistory.txt", "r", encoding='utf-8', errors='replace') as activeFile:
            allLines = []    
            allLines = activeFile.readlines()

        for line in allLines:
            if re.search(saveExpression, line) != "" :
                ProssesedArray.append(line)
                f = open("ProssesedText.txt", "a", errors='replace')
                f.write(line)
        print(ProssesedArray)
        activeFile.close()
    
    ## clears stuff that i dont want
    if inp == "PTclear" :
        delet = open("ProssesedText.txt",'w')
        delet.close()

    if inp == "PAclear" :
        ProssesedArray = []

    if inp == "allclear":
        delet = open("ProssesedText.txt",'w')
        delet.close()
        ProssesedArray = []

    #sorts websites in asending order
    if inp == "count" :
        Counter(ProssesedArray)
        print(ProssesedArray)
        print(Counter(ProssesedArray))

    ## transfers text betwen the two
    if inp == "TTA":
        with open("ProssesedText.txt", "r") as activeFile:
            ProssesedArray = activeFile.readlines()
            activeFile.close()
    
    if inp == "ATT":
        with open("ProssesedText.txt", "a+") as activeFile:
            activeFile.writelines(ProssesedArray)
    