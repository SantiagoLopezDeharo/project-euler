def is_pandigital(num_str):
    return len(num_str) == 9 and set(num_str) == set("123456789")

def largest_pandigital():
    max_pandigital = 0
    for x in range(1, 10000):  # We iterate over possible values of x
        concatenated_product = ""
        n = 1
        while len(concatenated_product) < 9:
            concatenated_product += str(x * n)
            n += 1
        if len(concatenated_product) == 9 and is_pandigital(concatenated_product):
            max_pandigital = max(max_pandigital, int(concatenated_product))
    return max_pandigital

# Find the largest pandigital number
largest_pandigital_number = largest_pandigital()

print(largest_pandigital_number)
