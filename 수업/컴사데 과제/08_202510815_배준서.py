bus_line = ['김수뭉', '이사슴', '박밀레']
bus_line.append('최자하')

bus_seat = ['구백년', '서교수']
bus_out = []

for i in range(len(bus_line)):
    print(bus_line[0], end=' ')
    print('탑승')
    bus_seat.append(bus_line.pop(0))
print()

for i in range(3):
    print(bus_seat[2], end=' ')
    print('하차')
    bus_out.append(bus_seat.pop(2))

print(bus_seat)