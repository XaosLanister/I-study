a = int(input())
b = int(input())
h = int(input())

if a <= h <= b:
    print("Это нормально")
elif a <= h >= b:
    print("Пересып")
elif a >= h <= b:
    print("Недосып")