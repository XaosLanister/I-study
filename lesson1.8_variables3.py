x = int(input())
h = int(input())
m = int(input())

k = x + h*60 + m

print(k//60)
print(k%60)