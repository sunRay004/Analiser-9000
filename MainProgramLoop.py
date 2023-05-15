import re

##file1 = open("C:\Analiser 9000\Text.txt","a+")
##print("start")
##for x in file1.readlines():
##    file1.read(x)



with open("C:\Analiser 9000\Text.txt","a+") as core:
    dung = re.sub(r",([^,\n]*,)?", r":\1", core.read())
    print(dung)

##file1.close

