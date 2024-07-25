def is_pentagonal(x):
    """Check if a number x is a pentagonal number"""
    n = (1 + (1 + 24 * x) ** 0.5) / 6
    return n == int(n)

def pentagonal(n):
    """Generate the n-th pentagonal number"""
    return n * (3 * n - 1) // 2

def find_min_pentagonal_pair():
    pentagonals = []
    n = 1
    # We brute force the answer
    while True:
        P_n = pentagonal(n)
        pentagonals.append(P_n)
        for P_j in pentagonals[:-1]:
            P_k = P_n
            if is_pentagonal(P_k - P_j) and is_pentagonal(P_k + P_j):  # The first one to be find will be the minimized one since the difference will only grow while we iterate
                return P_k - P_j
        n += 1

D = find_min_pentagonal_pair()

print("The answer is: " + str(D))