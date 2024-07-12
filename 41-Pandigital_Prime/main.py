import numpy as np

global ans
ans = -1

# We declare an eficient way of knowing if a specific number is prime or not

def primo(n):
    for i in range(int(np.trunc(np.sqrt(n)))):
        if ( (i+1 != 1) and (n % (i+1) == 0 )):
            return False
    return True

# We create function that iterates through all possible combinations of 1 to 7 digits, (since 1-9 will be always divisible by 3 since the sum of 1 to 9 is divisible by 3, and with 1-8 we have a similar problem)

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

# we print the asnwer
print(ans)