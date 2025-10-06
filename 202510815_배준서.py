def calc(x, y, op):
    try:
        if op=="+":
            return x+y
        elif op=="-":
            return x-y
        elif op=="*":
            return x*y
        elif op=="/":
            return x/y
        else:
            return x/0
    except:
        print("사칙연산 기호를 입력 해주세요.")

x=int(input("첫 번째 수 입력: "))
op=input("연산자 입력: ")
y=int(input("두 번째 수 입력: "))
print(f"사칙연산 결과: {calc(x, y, op)}")