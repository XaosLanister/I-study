import re

dataSet = open('test.txt')
file_read = re.split('(\d+)', dataSet.read())

counter = 0
for i in file_read:
    if counter < len(file_read):
        result = i[counter] * i[counter + 1]
    else:
        break
print(result)


