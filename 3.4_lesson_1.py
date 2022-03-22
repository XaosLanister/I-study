import re


def main(name):
    dataSet = open(name)
    file_read = re.split('(\d+)', dataSet.read())
    dataSet.close
    
    count = 0
    textOut = ''
    
    while count < len(file_read):
        if file_read[count] == '\n':
            break
        else:
            textOut += str(file_read[count] * int(file_read[count + 1]))
            count += 2

    fileOut = open('result.txt', 'w')

    for i in textOut:
        fileOut.write(i)
    fileOut.close

main('dataset_3363_2.txt')
