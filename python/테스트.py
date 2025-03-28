import random

guess = int(input('1과 10 사이의 수를 선택해 주세요: '))
num = random.randint(1, 10)

if guess == num:
    print('축하합니다! 당신이 이겼습니다!')

elif guess >= 11:
    print('1과 10 사이의 숫자를 입력해주십시오.')

else:
    print('하하하하')