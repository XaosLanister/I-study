import requests


with open('dataset_3378_2.txt') as link:
    url = link.read().strip('\n')
    
with open('658.txt', 'a+') as text:
    url = requests.get(url)
    st = url.text
    text.write(str(len(st.splitlines())))