import numpy as np
def primo(n):
    for i in range(int(np.trunc(np.sqrt(n)))):
        if ( (i+1 != 1) and (n % (i+1) == 0 )):
            return False
    return True

i = 0
n = 1
while (i != 10001):
    n = n + 1
    if (primo(n)):
        i = i + 1
print(n)