import collections
from typing import Counter

def main(name):
    dataSet = open(name)
    fileText = dataSet.read().lower()
    dataSet.close
    print(fileText)



main('test.txt')