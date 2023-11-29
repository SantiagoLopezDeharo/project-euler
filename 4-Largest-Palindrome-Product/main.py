def palindrome(n):
    n = str(n)
    for i in range(int(len(n)/2)):
        if (n[i] != n[len(n)-1-i]):
            return False
    return True

def largest_palindrome():
    max_palindrome = 0
    for i in range(999, 100, -1):
        for j in range(i, 100, -1):
            product = i * j
            if palindrome(product) and product > max_palindrome:
                max_palindrome = product
    return max_palindrome

print(largest_palindrome())