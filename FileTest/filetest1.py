inFp = None
inStr = ""

inFp = open("/Users/junseo/Desktop/plz-plz-plz/plz-plz-plz-1/FileTest/data1.txt", "r", encoding='UTF8')

inStr = inFp.readline()
print(inStr, end="")

inStr = inFp.readline()
print(inStr, end="")

inStr = inFp.readline()
print(inStr, end="")

inFp.close()