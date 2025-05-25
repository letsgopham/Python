inFp = None
inList, inStr = [], ""

inFp = open("/Users/junseo/Desktop/plz-plz-plz/plz-plz-plz-1/수업/FileTest/data1.txt", "r")

inList = inFp.readlines()
count = 0
for inStr in inList:
    print(f'{count+1}: {inStr}', end = "")
    count += 1

inFp.close()