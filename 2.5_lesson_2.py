meanings = [int(i) for i in input().split()]

di = ''

for meaning in range(len(meanings)):
    if len(meanings) == 1:
        di += str(meanings[0])
    else:
        a = meanings[meaning-1]+meanings[(meaning+1)%len(meanings)]
        di += str(a) + " "
print(di)