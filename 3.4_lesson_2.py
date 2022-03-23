import collections
from collections import Counter

def main(name):
    dataSet = open(name)
    fileText = Counter((dataSet.read().lower()).split()).most_common
    dataSet.close
    #fileText = Counter(fileText.split(' ')).most_common
    #fileText = Counter(fileText).most_common
    print(fileText)


main('test.txt')
