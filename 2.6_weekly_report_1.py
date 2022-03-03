a = True
sum_meanings = 0
sum_square = 0

while a == True:
    if meanings != 0:
        meanings = int(input())
        sum_meanings += meanings
        sum_square += meanings ** 2
    else:
        a = False
print(sum_square)
    