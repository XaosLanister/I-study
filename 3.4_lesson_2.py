import collections
from collections import Counter


def main(name):
    dataSet = open(name)
    fileText = Counter((dataSet.read().lower()).split()).most_common()
    dataSet.close
    dic = ''
    for i in fileText:
        if fileText[0][1] == i[1]:
            dic += i[0] + ' '+ str(i[1]) + ' '
    fileOut = open('result.txt', 'w')
    fileOut.write(dic)
    fileOut.close 

    print(dic)
main('dataset_3363_3.txt')
