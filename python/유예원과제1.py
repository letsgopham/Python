import random

a = []

while True:
    ask  = int(input("생성할 숫자의 갯수를 입력하세요 (1~20): "))

    if ask > 20:
        print("숫자를 다시 입력해주세요.")
    elif ask < 0:
        print("숫자를 다시 입력해주세요.")
    else:
        break
for i in range(ask):
    num = random.randint(1, 100)
    a.append(num)
print("생성된 숫자 리스트")
print(a)
print("가장 큰 숫자: ", end="")
print(max(a))