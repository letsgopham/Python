modulo = int(input('Enter modulo: '))
num = int(input('Enter number: '))

for pow in range(1, 100):
    print(f'{num}^{pow:>3} = {num**pow%modulo:>3} (mod {modulo})', end = '   |   ')
    print(f'ind_{num}({num**pow%modulo:>3}) = {pow:>3}', end = '')
    if num**pow%modulo == 1:
        print(f'  |  ord_{modulo}({num}) = {pow}')
        if pow == modulo-1:
            print(f'{num} is primitive root in modulo {modulo}')
        break
    print()