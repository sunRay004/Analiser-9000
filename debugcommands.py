
def PTclear():    
    delet = open("ProssesedText.txt",'w')
    delet.close()

def PAclear():
    return []

def TTA(pa):
    ## Text to Array
    pa = []
    with open("ProssesedText.txt", "r") as activeFile:
        activeFile.seek(0)
        pa = activeFile.readlines()
        return pa

def ATT(paa):
    ## Array to Text
    with open("ProssesedText.txt", "a+") as activeFile:
        activeFile.writelines(paa)
