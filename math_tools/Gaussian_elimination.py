#Gaussian elimination method - solve equation
#there is a sample below,
#a + 2b + 3c = 9
#2a - b +c = 8
#3a - c = 3  
#https://en.wikipedia.org/wiki/Gaussian_elimination --info
import numpy as np

#create a sample matrix(in example up)
matris = np.array([[1, 2, 3, 9],
                  [2, -1, 1, 8],
                  [3, 0, -1, 3]], dtype=float)

n = len(matris)

#Gaussian elimination method apply
for i in range(n):
    if matris[i][i] == 0:
        for j in range(i + 1, n):
            if matris[j][i] != 0:
                matris[i], matris[j] = matris[j].copy(), matris[i].copy()
                break

    for j in range(i + 1, n):
        factor = matris[j][i] / matris[i][i]
        matris[j][i:] -= factor * matris[i][i:]

#back elimination
x = np.zeros(n)
for i in range(n - 1, -1, -1):
    x[i] = (matris[i][-1] - np.dot(matris[i][i+1:n], x[i+1:])) / matris[i][i]

#result
print("Answer:")
for i in range(n):
    print(f"x{i} = {x[i]}")
