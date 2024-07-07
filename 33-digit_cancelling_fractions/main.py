import numpy as np

# we load in memory the numbers we are gonna use, since they are a small amount we can do it

numbers =    [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
numbersStr = ["10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99"]

results = []

for i in range(len(numbers)):
    for j in range(i):
        if (numbersStr[i][0] == numbersStr[j][1] and numbersStr[i][1] != "0"): #If they share a digit
            if (int(numbersStr[j][0])/int(numbersStr[i][1]) == numbers[j] / numbers[i] ): # If we remove the digit that is the same, does it have the same value ?
                results.append([numbers[j], numbers[i]])

print(results)
res = [1, 1]

for i in results: # We multiply all the found fractions and we represent it as a vector
    res[0] *= i[0]
    res[1] *= i[1]

print(res)

max = int( np.trunc(np.sqrt(res[1])))
suma = 2
not_visited = []

for i in range(max+1):
    not_visited.append(True)
    
for i in range(2, max, 2):
    not_visited[i] = False

# We loop through each value, and everytime we encounter a prime we mark all it´s multiplications as not prime, so we don´t have to take it into account in the sum ( We contruct the loop in such a way you will always encounter a prime in the if statement)
primos = [2]
for i in range(3, max, 2):
    if( not_visited[i] ):
        primos.append(i)
        for j in range(i, max, i ):
            not_visited[j] = False


#   I create a procedure to get the prime descomposition of a given number with a given array of prime numbers

def factorization(primos, n):
    potencias = []
    for i in range(len(primos)):
        potencias.append(0)
    
    for i in range(len(primos)):
        while(n % primos[i] == 0):
            potencias[i] = potencias[i] + 1
            n = n/primos[i]
    return potencias

potenciasNumerator   = factorization(primos, res[0])
potenciasDenominator = factorization(primos, res[1])

answer = res[1]

# Using the prime descomposition we now can find the smalles expresion of the fraction by dividing them into the prime numbers that they share

for i in range(len(primos)):
    if (potenciasNumerator[i] < potenciasDenominator[i]):
        answer /= primos[i] ** potenciasNumerator[i]
    else:
        answer /= primos[i] ** potenciasDenominator[i]

print(f" The answer to the challenge is : {answer}")