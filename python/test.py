answer, first_num, second_num, question, calculate, total = (0, 0, 0, "", 0, 0)

answer = int(input('1. 수식 계산.  2. 두 수 사이 합 계산. :'))

if answer == 2:
    first_num = int(input('1st number: '))
    second_num = int(input('2nd number: '))

    total = sum(i for i in range(first_num, second_num+1))
    print("입력하신 수 사의의 합은", total, "입니다.")


elif answer == 1:
    question = input('수식을 입력하세요: ')
    calculate = eval(question)
    print("%s 결과는 %5.1f입니다." %(question, calculate))
    
else:
    print('error!!!!\n1 or 2만 입력하세요!')