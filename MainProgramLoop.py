saveExpression = "title"

## this desides what to call and what to do
## just a while loop
running = True
while running:
    inp = input("launched, type help to view commands, imput here: ")
    
    ## help printout
    if inp == "help" :
        print("RegEx: lets you change the regular expresion that transfers files from")
        print("useEx: uses the given or default regular expresion to set up the files")
        print("commands:")
        print("commands:")
        print("commands:")
        print("commands:")
        print("commands:")
        print("commands:")
    
    ## RegEx adjustment to set the expression
    if inp.lower == "regex" :
        saveExpression = input("lines containing ___ should be saved: ")

    ## UseEx uses the expression given to 
    if inp.lower == "useex" :
        #makes allLines array, has all lines
        with open("BrowserHistory.txt", "r") as activeFile:
            allLines = activeFile.readlines()

        ProssesedArray = []

        for line in allLines:
            if saveExpression in line:
                ProssesedArray.append(line.rstrip("\n"))
                f = open("ProssesedText.txt", "a")
                f.write(line)