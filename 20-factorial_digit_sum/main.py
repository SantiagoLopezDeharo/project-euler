p = 1
for i in range(1, 101):
    p *= i
p = str(p)
s = 0
for i in p:
    s += int(i)
print(s)