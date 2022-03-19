meaning = int(input())
count = meaning

a = [[0] * meaning for i in range(meaning)]
a[0] = [(i + 1) for i in range(meaning)]

st, col, cycle_length  = 0, meaning - 1, meaning

def all_count():
    global count
    count += 1
    a[st][col] = count

while count < meaning * meaning:
    cycle_length -= 1
    for i in range(cycle_length):
        st += 1
        all_count()
    for i in range(cycle_length):
        col -= 1
        all_count()
    cycle_length -= 1
    for i in range(cycle_length):
        st -= 1
        all_count()
    for i in range(cycle_length):
        col += 1
        all_count()
    if count >= meaning * meaning:
        break

for i in a:
    print(*i)