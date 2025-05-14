select = int(input('입력 진수 결정(16, 10, 8, 2): '))
num = int(input('값 입력: '), select) # int(A, 16) ==> 뒤에 있는 수의 진법으로 변환.
num_hex = hex(num)
num_dec = num
num_oct = oct(num)
num_bin = bin(num)

print("{0:=^33}".format('진수 변환 결과'))
print("16진수 --->" "{0:>20}".format(num_hex,), '입니다.')
print("10진수 --->" "{0:>20}".format(num,), '입니다.')
print("8진수  --->" "{0:>20}".format(num_oct,), '입니다.')
print("2진수  --->" "{0:>20}".format(num_bin,), '입니다.')