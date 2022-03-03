meaning = int(input())
counts = ''

for number_of_reps in range(meaning + 1):
    for i in range(number_of_reps):
        counts += str(number_of_reps) + ' '
print(counts)
    