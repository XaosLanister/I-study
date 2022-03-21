import collections
from collections import Counter

word = input().lower().split()


def counts(word):
    f = dict(Counter(word))
    for key,value in f.items():
        print(key, value)


counts(word)
