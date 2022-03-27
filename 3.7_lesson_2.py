intab, outtab, cipher, cipher_1 = input(), input(), input(), input()


def coder(intab, outtab,cipher):
    trantab = cipher.maketrans(intab, outtab)
    print (cipher.translate(trantab))
coder(intab, outtab, cipher)


def out_coder(intab, outtab,cipher_1):
    trantab_1 = cipher_1.maketrans(outtab, intab)
    print(cipher_1.translate(trantab_1))
out_coder(intab, outtab,cipher_1) 
