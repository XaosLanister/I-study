"""Doc."""


gen = input()
Sum = 0

for i in gen:
    Sum += 1
nucl = gen.lower().count('g') + gen.lower().count('c')
res = (nucl / Sum) * 100

print(res)
