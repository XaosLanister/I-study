import collections
from collections import Counter

word = input().lower().split()

def counts(word):
    f = dict(Counter(word))
    for i in f:
        print(f)
        
counts(word)
