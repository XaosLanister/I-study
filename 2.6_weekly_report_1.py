a = True
sum_meanings = 0
sum_square = 0

while a == True:
    meanings = int(input())
    if meanings != 0:
        sum_meanings += meanings
        sum_square += meanings ** 2
    elif sum_meanings == 0:
        a = False
print(sum_square)
    