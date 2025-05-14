inFp, outFp = None, None
inStr = ""

inFp = open("/Users/junseo/Desktop/plz-plz-plz/plz-plz-plz-1/수업/FileTest/data2.txt", "r")
outFp = open("/Users/junseo/Desktop/plz-plz-plz/plz-plz-plz-1/수업/FileTest/data1.txt", "w")

inList = inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print("--- 파일이 정상적으로 복사되었음 ---")