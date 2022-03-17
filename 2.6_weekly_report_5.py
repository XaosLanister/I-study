from statistics import mean


a = []
meaning = int(input())

for i in range(meaning):
    a.append([0] * meaning)
for i in a:
    for j in i:
        print(i[j], end = " ")
    print()