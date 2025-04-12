import random

def get_random():
    return random.randint(1, 45)
    
lotto = []
lotto_pick = []

while True:
    if len(lotto_pick) >= 6:
        break
    lotto_num = int(input('로또 번호를 입력하세요.: '))

    if lotto_num >= 46:
        print('45이하의 정수만 입력해주세요.')

    elif lotto_pick.count(lotto_num) == 0:
        lotto_pick.append(lotto_num)
        lotto_pick.sort()
    
    
    elif lotto_pick.count(lotto_num) != 0:
        print('중복된 숫자를 입력하실 수 없습니다.')

print("====로또 추첨을 시작합니다.====")

print('추첨된 로또 번호 ===>', end='\t')

while True:
    num = get_random()

    if len(lotto) >= 7:
        break

    elif lotto.count(num) == 0:
        lotto.append(num)
        lotto.sort()

for j in range(7):
    print(lotto[j], end=' ')

print()

match = len(set(lotto[:6]) & set(lotto_pick))
bonus = lotto[6] in lotto_pick

if lotto == lotto_pick:
    print("1등!")
elif match == 6:
    print("2등!")
elif match == 5 and bonus:
    print("3등!")
elif match == 5:
    print("4등!")
elif match == 4:
    print("5등!")
elif match == 3:
    print("6등!")
else:
    print("미당첨입니다.")