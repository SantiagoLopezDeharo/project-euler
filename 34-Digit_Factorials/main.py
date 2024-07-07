
# The key in this problem is to understand that beyond 7 digits numbers this is not possible, since 9! = 362880 that is a 6 digit number, so you wont be able to go further than that suming the factorial of digits

factorial = [1, 1, 2, 3*2, 4*3*2, 5*4*3*2, 6*5*4*3*2, 7*6*5*4*3*2, 8*7*6*5*4*3*2, 9*8*7*6*5*4*3*2]

ans = 0

for i in range(10, 1000000):
    istr = str(i)
    tempSum = sum([factorial[int(j)] for j in istr])
    
    if (tempSum == i):
        ans += i
        
print(ans)