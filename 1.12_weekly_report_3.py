num1 = float(input())
num2 = float(input())
operation = input()

if operation == "+":
    plus = num1 + num2
    print(plus)

elif operation == "-":
    minus = num1 - num2
    print(minus)

elif operation == "/":
    if num2 > 0:
        divide = num1 / num2
        print(divide)
    elif num2 == 0:
        print("Деление на 0!")

elif operation == "*":
    multiply = num1 * num2
    print(multiply)

elif operation == "mod":
    if num2 > 0:
        Mod = num1 % num2
        print(Mod)
    elif num2 == 0:
        print("Деление на 0!")

elif operation == "pow":
    pow = num1 ** num2
    print(pow)

elif operation == "div":
    if num2 > 0:
        div = num1 // num2
        print(div)
    elif num2 == 0:
        print("Деление на 0!")