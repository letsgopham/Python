inFp = None
inStr = ""

inFp = open("/Users/junseo/Desktop/plz-plz-plz/plz-plz-plz-1/수업/FileTest/data1.txt", "r", encoding='UTF8')

inList = inFp.readlines()
print(inList)

inFp.close()