class Car:
    color=""
    speed=0

    def upSpeed(self, value):
        self.speed += value
        if self.speed > 150:
            self.speed = 150

    def downSpeed(self, value):
        self.speed -= value

myCar1 = Car()
myCar1.color = 'Red'
myCar1.speed = 0

myCar2 = Car()
myCar2.color = 'Blue'
myCar2.speed = 0

myCar3 = Car()
myCar3.color = 'Yellow'
myCar3.speed = 0

myCar4 = Car()

myCar1.upSpeed(200)
print('자동차1의 색상은 %s이며, 현재 속도는 %dkm입니다.'%(myCar1.color, myCar1.speed))

myCar2.upSpeed(60)
print('자동차2의 색상은 %s이며, 현재 속도는 %dkm입니다.'%(myCar2.color, myCar2.speed))

myCar3.upSpeed(0)
print('자동차3의 색상은 %s이며, 현재 속도는 %dkm입니다.'%(myCar3.color, myCar3.speed))

myCar4.upSpeed(30)
print('자동차4의 색상은 %s이며, 현재 속도는 %dkm입니다.'%(myCar4.color, myCar4.speed))