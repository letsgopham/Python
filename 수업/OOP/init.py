class Car():
    speed = 0
    def upSpeed(self, val):
        self.speed += val

        print(f'현재 속도(슈퍼클래스): {self.speed}')

class Sedan(Car):
    def upSpeed(self, val):
        self.speed += val

        if self.speed > 150:
            self.speed = 150

        print(f'현재 속도(서브 클래스): {self.speed}')

class Sonata(Sedan):
    pass

class Truck(Car):
    pass

sedan1, truck1, sonata1 = Sedan(), Truck(), Sonata()

print('트럭-->', end='')
truck1.upSpeed(200)

print('승용차-->', end='')
sedan1.upSpeed(200)

print('소나타-->', end='')
sonata1.upSpeed(200)