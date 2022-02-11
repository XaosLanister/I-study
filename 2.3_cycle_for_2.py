a = int(input())
b = int(input())

c, j = 0, 0

for i in range(a, b + 1):
    if i % 3 == 0:
        c += i
        j += 1
print(c / j)