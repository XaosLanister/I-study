a = int(input())

if a == 0:
    print(str(a) + " программистов")
elif a % 100 >= 10 and a % 100 <= 20:
    print(str(a) + " программистов")
elif a % 10 == 1:
    print(str(a) + " программист")
elif a % 10 >= 2 and a % 10 <= 4:
    print(str(a) + " программиста")
else:
    print(str(a) + " программистов")