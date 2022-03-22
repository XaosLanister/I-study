import re

dataSet = open('test.txt')
file_read = re.split('(\d+)', dataSet.read())

count = 0
s = ''
while count < len(file_read):
    if file_read[count] == '':
        break
    else:
        s += str(file_read[count] * int(file_read[count + 1]))
        count += 2
print(s)