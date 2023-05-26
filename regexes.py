import re


def regex(exp):
    exp = input("lines containing ___ should be saved: ")
    return exp
   
def useex(savex):
    print("this may take between 10 sec to 621 hours \nno, the program has not crashed")
    paray = []
    with open("BrowserHistory.txt", "r", encoding='utf-8', errors='replace') as activeFile:
        allLines = []    
        allLines = activeFile.readlines()


    for line in allLines:
        if re.search(savex, line):
            paray.append(line.rstrip(r"',/n"))
            f = open("ProssesedText.txt", "a", errors='replace')
            f.write(line)
    activeFile.close()


    return paray


