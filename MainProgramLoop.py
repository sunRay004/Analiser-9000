import re
import sys

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
        print("commands:")
        print("commands:")
        print("commands:")
        print("commands:")
        print("commands:")
    
    ## change regex
    if inp == "regex" :
        saveExpression = input("lines containing ___ should be saved: ")

    ## cleans the data
    if inp == "useex" :
        #makes allLines array, has all lines

        ## The people that insert emojis into their website titles deserve life in prison

        with open("BrowserHistory.txt", "r", encoding='utf-8', errors='replace') as activeFile:
            allLines = []    
            allLines = activeFile.readlines()

        ## I change my mind, it should be death

        for line in allLines:
            if re.search(saveExpression, line) != "" :
                ProssesedArray.append(line.rstrip("\n"))
                f = open("ProssesedText.txt", "a", errors='replace')
                f.write(line)
        print(ProssesedArray)
    
    ## clears the prossesed text
    if inp == "PTclear" :
        delet = open("ProssesedText.txt",'w')
        delet.close()
        ProssesedArray = []

