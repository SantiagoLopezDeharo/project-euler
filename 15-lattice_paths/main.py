# El problema es simplemente un proble de conteo, que se resuelve haciendo una combinacion de 40 en 20, ya que lo que queremos es de 40 posibles movimientos, determinar 20 posiciones de estas 40 para mover a la derecha( O abajo ), entonces basta ver cuantas combinaciones de 20 posiciones de 40 hay
import math
print (math.comb(40, 20)) 