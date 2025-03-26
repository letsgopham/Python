answer = int(input('1. 수식 계산.  2. 두 수 사이 합 계산. :'))


if answer == 2:
    a = int(input('1st number: '))
    b = int(input('2nd number: '))
    if b < a:
        print('error')
    
    total = sum(i for i in range(a, b+1))
    print("입력하신 수 사의의 합은", total, "입니다.")


if answer == 1:
    c = input('수식을 입력하세요: ')
    d = eval(c)
    print("%s 결과는 %5.1f입니다." %(c, d))

else:
    print('error')
    
    
    

    


    
        

    
