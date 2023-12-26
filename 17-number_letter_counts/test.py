digitos =   [ "", "one" ,  "two" ,  "three" ,  "four" ,  "five" ,  "six" ,  "seven" ,  "eight" ,  "nine" ]
ten =       [ "ten" ,  "eleven" ,  "twelve" ,  "thirteen" ,  "fourteen" ,  "fifteen" ,  "sixteen" ,  "seventeen" ,  "eighteen" ,  "nineteen" ]
decimales = [0,  "twenty" ,  "thirty" ,  "forty" ,  "fifty" ,  "sixty" ,  "seventy" ,  "eighty" ,  "ninety" ]
cientos =   [ "onehundredand" , "twohundredand" , "threehundredand" , "fourhundredand" , "fivehundredand" , "sixhundredand" , "sevenhundredand" , "eighthundredand" , "ninehundredand"]

f = 1000

for i in range(1, f, 1):
    print()
    n = str(i)
    if len(n) == 1:
        print(digitos[i], end=' ')
    elif len(n) == 2:
        if i < 20:
            print(ten[int(n[1])], end=' ')
        else:
            print(decimales[int(n[0]) - 1], end=' ')
            print(digitos[int(n[1])], end=' ')
    elif len(n) == 3:
        print(cientos[int(n[0]) - 1], end=' ')
        n = str(int(n[1:]))
        if len(n) == 1:
            print(digitos[(int(n)%100)], end=' ')
        elif len(n) == 2:
            if int(n) < 20:
                print(ten[int(n[1])], end=' ')
            else:
                print(decimales[int(n[0]) - 1], end=' ')
                print(digitos[int(n[1])], end=' ')
            
print("onethousand")
