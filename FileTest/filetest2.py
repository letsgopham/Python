inFp = None
inStr = ""

inFp = open("/Users/junseo/Desktop/plz-plz-plz/plz-plz-plz-1/FileTest/data1.txt", "r")

while True:
    inStr = inFp.readline()
    if inStr == "":
        break
    print(inStr, end = "")

inFp.close()