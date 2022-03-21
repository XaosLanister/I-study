import collections
from collections import Counter

word = input().lower().split()


def counts(word):
    dictWord = dict(Counter(word))
    for key,value in dictWord.items():
        print(key, value)


counts(word)
