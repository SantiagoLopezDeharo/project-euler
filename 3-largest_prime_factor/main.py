import numpy as np
a = 600851475143

#   I create a procedure to see if a given number is a prime number or not
def primo(n):
    for i in range(int(np.trunc(np.sqrt(n)))):
        if ( (i+1 != 1) and (n % (i+1) == 0 )):
            return False
    return True

i = 2
max = 1
while( a != 1 ):
    if ( primo(i) ):
        max = i
        while( a % i == 0 ):
            a = a / i
    i = i + 1

print(max)