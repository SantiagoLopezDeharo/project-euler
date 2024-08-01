from itertools import permutations

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Generate all 4-digit primes
primes = [i for i in range(1000, 10000) if is_prime(i)]

# Find permutations and check for arithmetic sequences
for prime in primes:
    perms = set(int(''.join(p)) for p in permutations(str(prime)) if int(''.join(p)) in primes)
    perms = sorted(perms)
    for i in range(len(perms)):
        for j in range(i+1, len(perms)):
            k = 2 * perms[j] - perms[i]
            if k in perms and k in primes:
                sequence = [perms[i], perms[j], k]
                if sequence[0] != sequence[1] != sequence[2]:
                    print(sequence)

# Note: The code will print potential sequences that meet the criteria
