inch = float(input("인치를 입력하십시오.: "))
cm = inch * 2.54
print(float(cm), 'cm 입니다.')

kilo = float(input("키로그램을 입력하십시오: "))
pound = kilo * 2.20462
print(float(pound), "파운드 입니다.")

ban = float(input("반지름을 입력하십시오.: "))
pi = 3.14
circle = ban ** 2 * pi
print("넓이는", float(circle), "입니다.")

answers = {'예', "네", "yes", "합격", "응", "넵"}
attempts = 0
while True:
    junseo = input("배준서는 컴퓨터과학과 학생회 인클루드에 합격했을까요?:")
    if junseo in answers:
        print("정답입니다.")
        break
    else:
       print("오답입니다. 다시 시도하세요.")
       attempts += 1

    if attempts >= 3:
        print("나중에 시도하십시오.")
        break
       