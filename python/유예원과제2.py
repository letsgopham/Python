import random

vocabulary = {}
voca_list = []

while True:

    ask = int(input("""(1) 영어단어 입력 (2) 퀴즈 (3) 종료
명령을 입력하세요: """))

    if ask == 1:
        voca = input("영어단어를 입력하세요: ")
        meaning = input("뜻을 입력하세요: ")
        if voca in voca_list:
            print("이미 존재하는 단어입니다.")
        else:
            vocabulary[voca] = meaning
            voca_list.append(voca)

    elif ask == 2:
        if len(voca_list) > 0:
            a = random.choice(voca_list)
            quiz = input(f"{a}의 뜻은?: ")
            if quiz == vocabulary[a]:
                print("정답입니다!")
            else:
                print(f"틀렸습니다! 정답은 {vocabulary[a]}입니다!")
    elif ask == 3:
        break
    else:
        print("잘못 입력하였습니다.")