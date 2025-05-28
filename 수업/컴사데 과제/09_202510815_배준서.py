print('평균 학점과 총합 점수를 알려드립니다.')
math = int(input('수학 학점 입력: '))
eng = int(input('영어 학점 입력: '))
korea = int(input('국어 학점 입력: '))
science = int(input('과학 학점 입력: '))

print(f'평균 학점은{(math+eng+korea+science)/4}입니다. 총합 점수는 {math + eng + korea + science}입니다.')