ans = 0

for i in range(1, 1001):
    ans += i**i
    ans = ans % 10000000000

print(ans)