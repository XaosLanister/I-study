number_of_commands = int(input())
coordinate = [0, 0]

for i in range(number_of_commands):
    i = input().split()
    if i[0] == 'север':
        coordinate[1] += int(i[1])
    elif i[0] == 'юг':
        coordinate[1] -= int(i[1])
    elif i[0] == 'запад':
        coordinate[0] -= int(i[1])
    elif i[0] == 'восток':
        coordinate[0] += int(i[1])
print(coordinate)