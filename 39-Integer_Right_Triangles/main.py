import numpy as np

MAX = 1000
ans = 0
max_count = 0
for p in range(MAX + 1):
    count = 0
    for a in range(1, p // 3):
        for b in range(a, (p-a) // 2):  # we iterate throw all the possible values of a and b
            c = p - a - b # We force that c has the required value for the perimeter
            if c*c == a*a + b*b : # If C also achives the pythagoras ecuation then it can be counted
                count += 1
    
    # If I found a higher count for a parameter I remember it
    if count > max_count:
        max_count = count
        ans = p

print(ans)