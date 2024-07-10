import numpy as np

MAX = 1000
ans = 0
max_count = 0
for p in range(MAX + 1):
    count = 0
    for a in range(1, p // 3):
        for b in range(a, (p-a) // 2):
            c = p - a - b
            if c*c == a*a + b*b :
                count += 1
    if count > max_count:
        max_count = count
        ans = p

print(ans)