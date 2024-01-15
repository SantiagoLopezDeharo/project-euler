numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#First we generate 3 arrays containing all the numbers that we are gonna use, of eac amount of digits


digits2 = []

for n1 in numbers:
    aux = []
    for i in numbers:
        aux.append(i)
    aux.remove(n1)
    for n2 in aux:
        digits2.append(n1*10 + n2)

digits3 = []

for n1 in numbers:
    aux = []
    for i in numbers:
        aux.append(i)
    aux.remove(n1)
    for n2 in aux:
        aux2 = []
        for i in aux:
            aux2.append(i)
        aux2.remove(n2)
        for n3 in aux2:
            digits3.append(n1*100 + n2*10 + n3)

digits4 = []

for n1 in numbers:
    aux = []
    for i in numbers:
        aux.append(i)
    aux.remove(n1)
    for n2 in aux:
        aux2 = []
        for i in aux:
            aux2.append(i)
        aux2.remove(n2)
        for n3 in aux2:
            aux3 = []
            for i in aux2:
                aux3.append(i)
            aux3.remove(n3)
            for n4 in aux3:
                digits4.append(n1*1000 + n2*100 + n3*10 + n4)

# Now we simply see theproduct of every one of them with each other with digit2xdigit3 and numersxdigit4, since we want in total to have just 9 digits

# Once we have the product, we simply evaluate if it has the rest of the digits using a set, if it does we sum it, and add it to a set to keep record of the visited numbers and don't repeat it

visited = set()
conteo = 0

for n in digits2:
    for m in digits3:
        z = n*m
        if (visited & {z} == set()):
            es = True
            digitos = set()
            
            for i in str(n):
                digitos.add(int(i))
            
            for i in str(m):
                es = es and ( digitos & {int(i)} == set() )
                digitos.add(int(i))
            
            for i in str(z):
                es = es and ({int(i)} & digitos == set()) and (i != '0')
                digitos.add(int(i))
            if es:
                print(f"{n} {m} {z}")
                conteo += z
                visited.add(z)

for n in numbers:
    for m in digits4:
        z = n*m
        if (visited & {z} == set()):
            es = True
            digitos = set()
            
            for i in str(n):
                digitos.add(int(i))
            
            for i in str(m):
                es = es and ( digitos & {int(i)} == set() )
                digitos.add(int(i))
            
            for i in str(z):
                es = es and ({int(i)} & digitos == set()) and (i != '0')
                digitos.add(int(i))
            if es:
                print(f"{n} {m} {z}")
                conteo += z
                visited.add(z)

print(conteo)