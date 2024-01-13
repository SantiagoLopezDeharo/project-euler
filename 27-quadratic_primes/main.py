import numpy as np

# We pre-compute the first 1000 prime numbers, to choose b more precisely and to know if it calculates correctly the prime number, since we know it will never calculate a prime larger than 1000
max = 1000
primes = [2]
set_primes = set()
set_primes.add(2)
not_visited = [True] * max
for i in range(2, max, 2):
    not_visited[i] = False

# We loop through each value, and everytime we encounter a prime we mark all it´s multiplications as not prime, so we don´t have to take it into account in the sum ( We contruct the loop in such a way you will always encounter a prime in the if statement)
for i in range(3, max, 2):
    if( not_visited[i] ):
        primes.append(i)
        set_primes.add(i)
        for j in range(i, max, i ):
            not_visited[j] = False

ma = 0
mb = 0

max = 0
cont_max = 0
for a in range(-1000, 1000):
    for bi in range(-len(primes)+1, len(primes)-1):
        b = primes[np.abs(bi)]*np.sign(bi)
        n = 0
        while {n*n + a*n + b} & set_primes != set():
            n += 1
        if n > cont_max:
            max = a*b
            cont_max = n
            ma = a
            mb = b
print(max)
print(f"a: {ma} b: {mb}")