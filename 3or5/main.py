numbers = []
registro = set()
i = 1
while ( (3*i < 1000) or (5*i < 1000 )):
    if ((3*i < 1000) and (registro & {3*i} == set())):
        numbers.append(3*i)
        registro.add(3*i)
    if ((5*i < 1000) and (registro & {5*i} == set())):
        numbers.append(5*i)
        registro.add(5*i)
    i = i + 1
s = 0
for n in numbers:
    s = s + n
print(s)
