class people:
    def __init__ (self, name, age):
        self.name = name
        self.age = age

while True:
    try:
        name = input('Enter your name: ')
        if name == 'quit':
            break
        age = int(input('Enter your age: '))      
        person1 = people(name, age)

        if person1.age > 19:
            print(f'{name}, Welcome!')
            break
        else:
            print('Only adult!')
            break
    except:
        print('\033[92mSyntaxError!!!!!\033[0m')
        pass

    finally:
        print(f'{"":=^20}')