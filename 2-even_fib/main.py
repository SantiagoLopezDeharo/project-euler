evens = []
a = 1
b = 2
evens.append(2)
while(a+b < 4000000):
    c = a+b
    a = b
    b = c
    if (c%2 == 0):
        evens.append(c)

s = 0
for n in evens:
    s = s + n
print(s)
