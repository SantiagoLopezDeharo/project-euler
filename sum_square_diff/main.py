n = 100

sum_square = 0

for i in range(n):
    sum_square = sum_square + (i + 1)**2

square_sum = 0

for i in range(n):
    square_sum = square_sum + i + 1
square_sum = square_sum**2

print(square_sum - sum_square)