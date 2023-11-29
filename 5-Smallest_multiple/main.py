import numpy as np
a = 20

#   I create a procedure to see if a given number is a prime number or not
def primo(n):
    for i in range(int(np.trunc(np.sqrt(n)))):
        if ( (i+1 != 1) and (n % (i+1) == 0 )):
            return False
    return True

# I create a procedure to generate an array with all the given prime numbers between 1 and max
def prime_generator(max):
    primos = []
    for i in range(max):
        if( primo(i+1) ):
            primos.append(i+1)
    primos.remove(1)
    return primos

primos = prime_generator(a)
# Now I will make an array to keep what power each prime number should be
potencias = []

for i in range(len(primos)):
    potencias.append(0)

#   I create a procedure to get the prime descomposition of a given number with a given array of prime numbers

def factorization(primos, n):
    potencias = []
    for i in range(len(primos)):
        potencias.append(0)
    
    for i in range(len(primos)):
        while(n % primos[i] == 0):
            potencias[i] = potencias[i] + 1
            n = n/primos[i]
    return potencias

# Now I determine the maximum power of each prime number in each of the prime descompositions in the given range.

for i in range(a-1):
    aux = factorization(primos, i+2)
    for i in range(len(potencias)):
        if potencias[i] < aux[i]:
            potencias[i] = aux[i]

#   Finally I get the answer to the problem by calculating the value of the a number with the prime descomposition that we found

respuesta = 1
for i in range(len(primos)):
    respuesta = respuesta*(primos[i]**potencias[i])
print(respuesta)