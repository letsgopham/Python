select = int(input('입력 진수 결정(16, 10, 8, 2): '))
num = int(input('값 입력: '), select) # int(A, 16) ==> 뒤에 있는 수의 진법으로 변환.
num_hex = hex(num)
num_dec = num
num_oct = oct(num)
num_bin = bin(num)

print(f"16진수 ---> {num_hex}입니다.")
print(f"10진수 ---> {num}입니다.")
print(f"8진수 ---> {num_oct}입니다.")
print(f"2진수 ---> {num_bin}입니다.")