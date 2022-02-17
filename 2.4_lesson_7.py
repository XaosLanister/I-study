Gen = input()

ind, res, alg = -1 * len(Gen), '', ''

while ind < 0:
    variab = 1
    if len(Gen) == 1:
        alg = Gen + str(variab)
        break
    while Gen[ind] == Gen[ind + 1] and ind < 0:
        res = Gen[ind] + str(variab)
        ind += 1
        variab += 1
    if Gen[ind] != Gen[ind + 1]:
        res = Gen[ind] + str(variab)
        ind += 1
    alg += res
print(alg)
