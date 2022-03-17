meaning, date, column = input(), [], 0

while meaning != 'end':
    date += [[int(i) for i in meaning.split()]]
    meaning = input()
    column += 1
#print (date)
#print(column)
string = len(date[0])
#print(string)

[([print(date[i - 1][j] + date[i][j - 1] + date[i][(j + 1) % string] + date[(i + 1) % column][j], end=' ') for j in range(string)], print()) for i in range(column)]

"""
Ru comment
Делал первую часть сам, с выводом и подсчетом в матрице помогал знакомый к сожалению(((
Буду дальше читать и пытаться вникнуть, пока что матрицы мне даются не легко((((
    
    Eng comment
    I did the first part myself, unfortunately a friend helped with the output and calculation in the matrix (((
    I will continue to read and try to understand, so far the matrices are not easy for me ((((
"""