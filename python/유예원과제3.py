def allMutiple():
    print("모든 구구단 출력")
    for i in range(2, 10):
        for j in range(1, 10):
            print(f"{i} x {j} = {j*i}")

def reverseAllMutiple():
    print("모든 구구단 역순 출력")
    for i in range(9, 1, -1):
        for j in range(9, 0, -1):
            print(f"{i} x {j} = {j*i}")

def multiple(number):
    print("구구단 {0} 단 출력".format(number))
    for i in range(1, 10):
        print(f"{number} x {i} = {(number)*i}")
allMutiple()
reverseAllMutiple()

n = int(input("구구단 단수를 입력해주세요: "))
multiple(n)