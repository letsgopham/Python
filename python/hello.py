for i in range(1, 17):
    if 16 % i == 0:
        print(f"i = {i} ", end='> 6 = ')
        print(6**i%17, '(mod 17)')
    else:
        pass