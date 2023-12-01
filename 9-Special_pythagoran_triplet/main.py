a = 0
b = 1
c = 999

while ( a**2 + b**2 != c**2 ):
    a = a + 1
    c = c - 1
    if(b == a):
        b = b + 1
        c = 1000 - b
        a = 0
    if (b <= a):
        break

print("a = " + str(a) + " b = "  + str(b) + " c = " + str(c) )
print("El producto es: " + str(a*b*c))
