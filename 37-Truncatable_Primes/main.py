max = 1000000

primes = set() #Its crucial for the runtime that we can quickly find if an element is in the collection, so we will use Set that has O(log(n)) for search
primes.add(2)


not_visited = [True] * max
for i in range(2, max, 2):
    not_visited[i] = False

# We loop through each value, and everytime we encounter a prime we mark all it´s multiplications as not prime, so we don´t have to take it into account in the sum ( We contruct the loop in such a way you will always encounter a prime in the if statement)

for i in range(3, max, 2):
    if( not_visited[i] ):
        primes.add(i)
        for j in range(i, max, i ):
            not_visited[j] = False

not_visited = [True] * max

truncable_primes = 0

ans = 0

for i in primes:    # O( n * log(n) ) being n the amount of prime numbers under 1000000
    if not_visited[i] and len(str(i)) > 1:
        flag = True # We keep a flag for knowing if the prime in cuestion have the desire properties
        p = str(i)
        not_visited[i] = False
        
        for j in range(len(p)-1):
            aux = p[1:]  # We remove the first digit
            not_visited[int(aux)] = False
            flag = flag and (int(aux) in primes) # O(log(n))
            p = aux
            if not flag:
                break
        p = str(i)

        for j in range(len(p)-1):
            aux = p[:len(p)-1]  # We remove the last digit
            not_visited[int(aux)] = False
            flag = flag and (int(aux) in primes) # O(log(n))
            p = aux
            if not flag:
                break
        if flag:
            truncable_primes += 1 # We keep count of the truncable primes we find
            ans += i

print(f" The amount of truncable primes under {max} is: {truncable_primes} and their sum is: {ans}")