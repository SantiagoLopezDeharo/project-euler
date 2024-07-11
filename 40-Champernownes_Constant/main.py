
maxDigit = 1000000

wantedDigits = [1, 10, 100, 1000, 10000, 100000, 1000000]

ans = 1

# Since to compute until the one million diigit we dont need much iterations we will iterate until we get there (Notice it will be a lot less than one million iterations, since we weill be adding multiple digits in each iteration) 
n = 1
indx = 1
while indx <= maxDigit:
    for i in str(n):
        if indx in wantedDigits: # if we arrived to a desired digit we multiply by it
            ans *= int(i)
        indx += 1
    n += 1

print(ans)

# Time complexity: O(n) with n begin the maximum digit to calculate to
# Memory complexity: O(1)