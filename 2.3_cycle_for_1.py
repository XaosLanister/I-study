a = int(input())
b = int(input())
c = int(input())
d = int(input())

for i in range(c, d + 1):
    print(f'\t{i}', end='')
for j in range(a, b + 1):
    print(f'\n{j}', end='')
    for f in range(c, d + 1,):
        print(f'\t{f * j}', end='')
print()