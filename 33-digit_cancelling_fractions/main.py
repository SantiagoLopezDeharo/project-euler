from numpy import np

for i in range(11, 100):
    for j in range(10, i):
        igual = -1
        for ii in str(i):
            for jj in str(j):
                if ii == jj:
                    igual = i
        if igual != -1:
                  
        np.isclose(a, b, rtol=1e-05, atol=1e-08, equal_nan=False)