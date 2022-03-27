count_word = int(input())
count_str= int(input())

def my_word(count_word):
    date = []
    for i in range(count_word):
        i = input().lower()
        date.append(i)
        #print(date)
    return date
my_word(count_word)

def my_str(count_str):
    date_str = []
    for i in range(count_str):
        i = input().lower().split()
        date_str += i
    #print(date_str)
my_str(count_str)
