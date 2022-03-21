def f(meaning):
    p = meaning * meaning
    return p


valueStr = int(input())
meanings = dict()

for meaning in range(valueStr):
    meaning = int(input())
    if meaning in meanings:
        print(meanings[meaning])
    else:
        meanings[meaning] = f(meaning)
        print(f(meaning))
