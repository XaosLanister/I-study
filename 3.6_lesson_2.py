import requests

file_link = 'https://stepic.org/media/attachments/course67/3.6.3/'

with open('dataset_3378_3.txt') as file:
    file_name = file.readline().strip()
file_name = str(requests.get(file_name).text)

#counts = 1

while 'we'not in file_name:
    #print(file_name, counts)
    file_name = requests.get(file_link + file_name).text
    #counts += 1
print(file_name, file= open('result.txt', 'w'))
