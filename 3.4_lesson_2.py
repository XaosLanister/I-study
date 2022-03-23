import collections
from collections import Counter


def main(name):
    dataSet = open(name)
    fileText = Counter((dataSet.read().lower()).split()).most_common()
    fileText.sort()
    dataSet.close
    print(fileText)
    dic = []
    for i in fileText:
        if fileText[0][1] == i[1]:
            dic += i
    print(*dic)
main('test.txt')




"""             dic += i
        else:
            break    """