n = 1001

sum = 0
i = 1
add = 2
tics = 0
while i <= n*n:
    sum += i
    i += add
    tics += 1
    if tics == 4:
        tics = 0
        add += 2

print(f"The sum is: {sum}")