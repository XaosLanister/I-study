count_word = int(input())


def my_word(count_word):
    date_word = []
    for i in range(count_word):
        i = input().lower()
        date_word.append(i)
    return date_word
date_word = my_word(count_word)


count_str= int(input())


def my_str(count_str):
    date_str = []
    for i in range(count_str):
        i = input().lower().split()
        date_str += i
    return set(date_str)
date_str = my_str(count_str)


def check(date_word, date_str):
    for i in date_str:
        if i not in date_word:
            print(i)
check(date_word, date_str)