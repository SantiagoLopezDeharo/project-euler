import math

digits = 1000

result = round( ( (digits-1)*math.log(10) + 0.5*math.log(5) ) / math.log((1 + math.sqrt(5)) / 2))
print(f"The index of the first term in the Fibonacci sequence with 1000 digits is: {result}")
