inFp = None
inStr = ""

inFp = open("C:\\Users\\Administrator\\OneDrive\\바탕 화면\\python실습\\.dist\\FileTest\\data1.txt", "r", encoding='UTF8')

inStr = inFp.readline()
print(inStr, end="")

inStr = inFp.readline()
print(inStr, end="")

inStr = inFp.readline()
print(inStr, end="")

inFp.close()