digitos =   [0, len("one"), len("two"), len("three"), len("four"), len("five"), len("six"), len("seven"), len("eight"), len("nine")]
ten =       [len("ten"), len("eleven"), len("twelve"), len("thirteen"), len("fourteen"), len("fifteen"), len("sixteen"), len("seventeen"), len("eighteen"), len("nineteen")]
decimales = [0, len("twenty"), len("thirty"), len("forty"), len("fifty"), len("sixty"), len("seventy"), len("eighty"), len("ninety")]
cientos =   [len("onehundredand"),len("twohundredand"),len("threehundredand"),len("fourhundredand"),len("fivehundredand"),len("sixhundredand"),len("sevenhundredand"),len("eighthundredand"),len("ninehundredand")]

f = 1000

sum = 0

for i in range(1, f, 1):
    n = str(i)
    if len(n) == 1:
        sum += digitos[i]
    elif len(n) == 2:
        if i < 20:
            sum += ten[int(n[1])]
        else:
            sum += decimales[int(n[0]) - 1]
            sum += digitos[int(n[1])]
    elif len(n) == 3:
        sum += cientos[int(n[0]) - 1]
        n = str(int(n[1:]))
        if n == '0':
            sum -= 3 
        elif len(n) == 1:
            sum += digitos[(int(n)%100)]
        elif len(n) == 2:
            if int(n) < 20:
                sum += ten[int(n[1])]
            else:
                sum += decimales[int(n[0]) - 1]
                sum += digitos[int(n[1]) ]
            
sum += len("onethousand")
print(sum)