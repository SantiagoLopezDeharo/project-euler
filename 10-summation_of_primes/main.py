max = 2000000

suma = 2
not_visited = [True] * max
for i in range(2, max, 2):
    not_visited[i] = False

# We loop through each value, and everytime we encounter a prime we mark all it´s multiplications as not prime, so we don´t have to take it into account in the sum ( We contruct the loop in such a way you will always encounter a prime in the if statement)

for i in range(3, max, 2):
    if( not_visited[i] ):
        suma = suma + i
        for j in range(i, max, i ):
            not_visited[j] = False
print(suma)
