meanings = [int(i) for i in input().split()]

a = ''
for i in meanings:
    if len(meanings) == 1:
        print(i)
    elif i == meanings[0]:
        a +=str(meanings[1] + meanings[-1]) + ' '
    elif i == meanings[-1]:
        a += str(meanings[0] + meanings[-2]) + ' '
        
print(a)