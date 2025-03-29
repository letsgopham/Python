import time

answers = {'junseo', '준서', 'baejunseo', '배준서'}
attempts = 0

while True:
    question = input('나의 이름은?: ')
    if question in answers:
        print('정답.')
        break
    elif question == '존잘':
        input('계좌를 입력해주세요! ㅎㅎ: ')
        break
    else:
        print('오답.')
        attempts += 1

    if attempts >= 5:
        print('나중에 다시 시도해주세요.')
        time.sleep(60)