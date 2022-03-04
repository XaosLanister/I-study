lst, meaning, answer = [int(i) for i in input().split()], int(input()), ''

for i in range(len(lst)):
    if lst[i] == meaning:
        answer += str(i) + ' '
if answer == '':
    answer = 'Отсутствует'
print(answer)