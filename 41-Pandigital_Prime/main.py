import numpy as np

global ans
ans = -1

def primo(n):
    for i in range(int(np.trunc(np.sqrt(n)))):
        if ( (i+1 != 1) and (n % (i+1) == 0 )):
            return False
    return True

def find_pandigital_prime(digits, prefix=''):
    global ans
    if len(digits) == 0:
        it = int(prefix)
        if(primo(it) and it > ans):
            ans = it            
    else:
        for i in range(len(digits)):
            new_digits = digits[:i] + digits[i+1:]
            find_pandigital_prime(new_digits, prefix + digits[i])

digits = '1234567'
find_pandigital_prime(digits)

print(ans)