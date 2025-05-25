inFp, outFp = None, None
inStr = ""

fname1 = input('소스 파일명 입력:')
fname2 = input('타깃 파일명 입력:')

inFp = open(fname1, "r")
outFp = open(fname2, "w")

inList = inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print("--- 파일이 정상적으로 복사되었음 ---")