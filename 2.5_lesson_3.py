import collections
from typing import Counter


meanings = [i for i in input().split()]

a = Counter(meanings).most_common()
c = ''

for i in a:
    if i[1] == 1:
        pass
    else:
        c += i[0] + ' '
print(c)

"""Today I meet module 'collection'!!! It's realy cool module)"""
