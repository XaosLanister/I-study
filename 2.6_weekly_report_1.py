sum_meanings, sum_square = 0, 0

while True:
    meanings = int(input())
    if meanings != 0:
        sum_meanings += meanings
        sum_square += pow(meanings, 2)
    if sum_meanings == 0:
        break
print(sum_square)
    