for i in range(2, 10):
    print(f'#  {i}단  #', end='\t')
print()

for i in range(1, 10):
    for j in range(2, 10):
        print(f'{j} x {i} = {i*j}', end='\t')
    print()