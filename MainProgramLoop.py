import regexes
import debugcommands
import ArrayCommands
import maths


saveExpression = r'"url":'
WebArray = []
ProssesedArray = []

## this desides what to call and what to do
## just a while loop
running = True
print("launched, type help to view commands")
while running:
    inp = input("imput: ")
    
    ## help printout
    if inp == "help" :
        print("------ regexes, use these first ------")
        print()
        print("regex: lets you select what to save to the prossesed array")
        print("useex: saves selected thing to the prossesed array (default saves website urls)")
        print()
        print("------ prossesing functions, use after regexes ------")
        print()
        print("findNames: finds domain names, needs prossesed array, creates the web array")
        print("count: counts websites, needs web array, creates export array")
        print("export: exports export array into a .txt file, for use in graphical analysis (use a spreadsheet lol, idk how to make python graphs)")
        print()
        print("------ math ------")
        print()
        print("mean: finds the mean")
        print("median: finds the median")
        print("mode: finds the mode")
        print("deviation: finds the standard deviation")
        print("gmean: finds the geometric mean")
        print()
        print("------ utility ------")
        print()
        print("clear: menu for clearing arrays")
        print("cleanWebArray: uses a regex expression to filter the web array")
        print("TTA: contents of prossesed text to prossesed array (usefull if useex was run and the program reloaded, saves time)")
        print("ATT: contents of prossesed array to prossesed text (does not clear prossesed text)")
    
    if inp == "regex" :
        saveExpression = regexes.regex(saveExpression)
        print("Done")
        
    if inp == "useex" :
        ProssesedArray = regexes.useex(saveExpression)
        print("Done")
    
    if inp == "count" :
        expArray = ArrayCommands.count(WebArray)
        print(expArray)
        print("Done")

    if inp == "TTA":
        ProssesedArray = debugcommands.TTA(ProssesedArray)
        print("Done")

    if inp == "ATT":
        debugcommands.ATT(ProssesedArray)
        print("Done")

    if inp == "findNames":
        WebArray = ArrayCommands.findNames(ProssesedArray)
        print("Done")

    if inp == "cleanWebArray":
        ArrayCommands.cleanWebArray(saveExpression, WebArray)
        print("Done")

    if inp == "export":
        ArrayCommands.exportWebArray(expArray)

    if inp == "deviation":
        print(maths.SD(expArray))
    
    if inp == "mean":
        print(maths.mean(expArray))
    
    if inp == "median":
        print(maths.median(expArray))

    if inp == "mode":
        print(maths.mode(expArray))

    if inp == "gmean":
        print(maths.gmean(expArray))
    
    if inp == "clear" :
        ## clears menu
        print("PT: clears the ProssesedText.txt document")
        print("PA: clears the ProssesedArray")
        print("ALL: clears everything")
        inp = input(":")

        if inp == "PT":
            debugcommands.PTclear
        if inp == "PA":
            ProssesedArray = debugcommands.PAclear
        if inp == "ALL":
            debugcommands.PTclear
            ProssesedArray = debugcommands.PAclear

        print("Done")
