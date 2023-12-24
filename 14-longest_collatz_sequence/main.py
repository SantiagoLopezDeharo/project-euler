def calcular_largo(M, vi):
    if vi < 1000000 and M[vi] != 0:
        return M[vi]
    elif vi == 1:
        return 1
    elif vi % 2 == 0:
        return 1 + calcular_largo(M, int(vi/2))
    else:
        return 1 + calcular_largo(M, 3*vi + 1)

max = 1
maxL = 1
M = []
for i in range(1000000):
    M.append(0)


for i in range(1, 1000000, 1):
    L = calcular_largo(M, i)
    M[i] = L
    if L > maxL:
        maxL = L
        max = i

print(max)