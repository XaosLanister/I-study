meaning = int(input())
c = 0

a = [[0] * meaning for i in range(meaning)]
a[0] = [(col + 1) for col in range(meaning)]

for i in a:
    print(i)