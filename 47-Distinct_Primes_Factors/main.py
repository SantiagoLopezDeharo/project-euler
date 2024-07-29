def prime_factors_count(n):
    """ Return the number of distinct prime factors of n. """
    i = 2
    factors = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return len(factors)

def find_consecutive_numbers_with_prime_factors(target_count, consecutive_count):
    """ Find the first sequence of consecutive_count numbers each with target_count distinct prime factors. """
    n = 2  # Starting point
    consecutive_found = 0

    while True:
        if prime_factors_count(n) == target_count:
            consecutive_found += 1
            if consecutive_found == consecutive_count:
                return n - consecutive_count + 1
        else:
            consecutive_found = 0
        n += 1

# Find the first four consecutive integers to have four distinct prime factors each.
first_number = find_consecutive_numbers_with_prime_factors(4, 4)
print(first_number)
