number = ""

maxDigit = 1000000

# Since to compute until the one million diigit we dont need much iterations we will iterate until we get there (Notice it will be a lot less than one million iterations, since we weill be adding multiple digits in each iteration) 
i = 0
while len(number) <= maxDigit:
    number += str(i) # We create the irrational number until the maximum digit we are going to consult
    i += 1

ans = 1

for i in range(len(str(maxDigit))):
    ans *= int(number[10**i])   # We compute the answer for the challenge now that we have all the data needed

print(ans)