inFp = None
inList, inStr = [], ""

inFp = open("/Users/junseo/Desktop/plz-plz-plz/plz-plz-plz-1/FileTest/data1.txt", "r")

inList = inFp.readlines()
for inStr in inList:
    print(inStr, end = "")

inFp.close()