numbers = []

for n in range(2, 1000000):
    sn = str(n)
    m = 0
    for i in sn:
        m += int(i)**5
    if m == n:
        numbers.append(n)

print(numbers)
suma = 0
for i in numbers:
    suma += i
print(f"La suma de estos numeros es: {suma}")