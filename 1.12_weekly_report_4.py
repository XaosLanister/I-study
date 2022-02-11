figure = input()


if figure == "треугольник":
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c)/2
    s = (p*(p-a)*(p-b)*(p-c))**0.5
    print(s)

if figure == "прямоугольник":
    a = float(input())
    b = float(input())
    print(a * b)

if figure == "круг":
    r = float(input())
    r = ((r**2) * 3.14)
    print(r)