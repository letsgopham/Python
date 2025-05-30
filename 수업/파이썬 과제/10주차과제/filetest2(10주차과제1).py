inFp = None
inStr = ""

inFp = open("/Users/junseo/Desktop/plz-plz-plz/plz-plz-plz-1/수업/FileTest/data1.txt", "r")
count = 0
while True:
    inStr = inFp.readline()
    if inStr == "":
        break
    print('%d: %s'%(count+1, inStr), end = "")
    count += 1

inFp.close()