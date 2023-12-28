from itertools import permutations

# Generate permutations of the digits 0-9
permutations_list = list(permutations('0123456789'))

# Find the millionth lexicographic permutation
millionth_permutation = ''.join(permutations_list[999999])

print("The millionth lexicographic permutation is:", millionth_permutation)

