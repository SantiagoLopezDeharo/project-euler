import numpy as np

def divisores(n):
    div = []
    m = round(np.sqrt(n)) + 1
    for i in range(1,  m):
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

is_sum = set()
abundant_num = []
ans = 0

for i in range(1, 20162):
    if (is_sum & {i} == set()):
        ans += i
     
    s = suma_divisores(i)
    if (s > i):
        abundant_num.append(i)
        for j in abundant_num:
            is_sum.add(i+j)

print(ans)