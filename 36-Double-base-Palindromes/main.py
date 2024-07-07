import numpy as np

# first we generate al palindroms under one million in base 10

max = 1000000

palindroms = []

for i in range(10):
    palindroms.append(i)

bound = 10 ** int(np.trunc(len(str(max)) / 2) + 1)


for i in range(1, bound):
    if (int( str(i) + str(i)[::-1] ) < max):
        palindroms.append(int( str(i) + str(i)[::-1] ))
        if (2*len(str(i)) + 1 <= len(str(max))):
            for j in range(10):
                palindroms.append(int( str(i) + str(j) + str(i)[::-1] ))

# then we generate al palindroms under one million in base 2

binaryPalindromes = set() # Important to use Set here since we will be using this collection to find things, and set find in O(log(n))

for i in range(2):
    binaryPalindromes.add(str(i))

for i in range(1, bound):
    if (int( str(i) + str(i)[::-1] ) < max):
        binaryPalindromes.add(( str(bin(i))[2:] + str(bin(i))[2:][::-1] ))
        if (2*len(str(bin(i))[2:]) + 1 <= len(str(bin(max)[2:]))):
            for j in range(2):
                binaryPalindromes.add( str(bin(i))[2:] + str(j) + str(bin(i))[2:][::-1] )



ans = 0
for i in palindroms: # O ( n * log(m) ) with n + len(palindroms) and m = len(binaryPalindromes) , note that m >>> n, so it is smart to make it this way rather than the other way arround
    binary = str(bin(i))[2:]
    if binary in binaryPalindromes: # O ( log(m) )
        ans += i

print(ans)