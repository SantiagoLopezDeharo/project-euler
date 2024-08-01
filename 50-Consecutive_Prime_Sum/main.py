max_limit = 1000000

# Sieve of Eratosthenes to generate prime numbers up to max_limit
is_prime = [True] * (max_limit + 1)
is_prime[0] = is_prime[1] = False

for start in range(2, int(max_limit**0.5) + 1):
    if is_prime[start]:
        for multiple in range(start*start, max_limit + 1, start):
            is_prime[multiple] = False

primes = [num for num, prime in enumerate(is_prime) if prime]

# Find the prime which can be written as the sum of the most consecutive primes
max_length = 0
answer = 0

# To store the prefix sums of primes
prefix_sums = [0]
for prime in primes:
    prefix_sums.append(prefix_sums[-1] + prime)

# Check each combination of primes[i:j] to see if it sums to a prime
for i in range(len(primes)):
    for j in range(i + max_length, len(primes)):
        if prefix_sums[j + 1] - prefix_sums[i] > max_limit:
            break
        if is_prime[prefix_sums[j + 1] - prefix_sums[i]]:
            max_length = j - i + 1
            answer = prefix_sums[j + 1] - prefix_sums[i]

print(answer)
