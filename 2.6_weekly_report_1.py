sum_meanings = 0
sum_square = 0

while True:
    meanings = int(input())
    if meanings != 0:
        sum_meanings += meanings
        if sum_meanings != 0:
            sum_square += meanings ** 2
        if sum_meanings <= 0:
            break
print(sum_square)
    