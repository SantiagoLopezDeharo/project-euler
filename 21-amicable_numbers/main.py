n = 10000
import numpy as np

def divisores(n):
    div = []
    for i in range(1, round(np.sqrt(n)) + 1 ):
        if n % i == 0:
            div.append(i)
            if (i**2 != n) and i!=1:
                div.append(n // i)
    return div

def suma_divisores(n):
    div = divisores(n)
    sum = 0
    for i in div:
        sum += i
    return sum

# I create a set to keep record of the already visited numbers
visited = set()

sum_amicables = 0

for i in range(1, n):
    if (visited & {i} == set()):
        visited.add(i)
        s1 = suma_divisores(i)
        s2 = suma_divisores(s1)
        if (i == s2) and (i != s1):
            sum_amicables += i + s1
            visited.add(s1)
print(sum_amicables)
            
    


