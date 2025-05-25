class people:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        self.adult = self.age > 19
    
    def is_adult(self):
        return self.adult

    #def say(self):
        print(f'Hello my name is {self.name}, and {self.age} years old and work as a {self.job}.')


name = input('이름을 입력하세요: ')
age = int(input('나이를 입력하세요: '))

user = people(name, age)

if user.is_adult():
    print('가입이 완료되었습니다.')

else:
    print('성인만 가입할 수 있습니다.')