a = int(input())
b = int(input())
c = int(input())

x = a
if b > x:
    x = b
if c > x:
    x = c
print(x)

y = a
if b < y:
    y = b
if c < y:
    y = c
print(y)

if a < x and a > y:
    print(a)
elif b < x and b > y:
    print(b)
elif c < x and c > y:
    print(c)
elif a == b:
    print(a)
elif b == c:
    print(b)
elif a == c:
    print(c)