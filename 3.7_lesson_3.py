count_word = int(input())
count_str= int(input())

def my_word(count_word):
    date = []
    for i in range(count_word):
        i = input().lower()
        date.append(i)
    return date
my_word(count_word)
