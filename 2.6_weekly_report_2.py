meaning, answer, meanings = int(input()), '', 1

for number_of_reps in range(meaning + 1):
    for i in range(number_of_reps):
        if meaning >= meanings:
            meanings += 1
            answer += str(number_of_reps) + ' '
        else:
            break
print(answer)
