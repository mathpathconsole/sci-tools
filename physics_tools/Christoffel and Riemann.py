from sympy import *
                                                     #Reşat Berk | Stars of the Sky
# Symbols and coordinates
r, theta, phi = symbols('r theta phi')
coords = [r, theta, phi]

# g_metric
g = Matrix([[1, 0, 0],
                [0, r**2, 0],
                [0, 0, r**2 *sin(theta)**2]])


# inverse for g_metric
g_inv = g.inv()

# Christoffel symbols
Chr = MutableDenseNDimArray.zeros(3, 3, 3)

for k in range(3):
    for i in range(3):
        for j in range(3):
            Chr[k, i, j] = 0.5 * sum(g_inv[k, l] * (diff(g[l, i], coords[j]) + diff(g[l, j], coords[i]) - diff(g[i, j], coords[l])) for l in range(3))

# Riemann tensor
Riemann = MutableDenseNDimArray.zeros(3, 3, 3, 3)

for r in range(3):
    for s in range(3):
        for i in range(3):
            for j in range(3):
                Riemann[r, s, i, j] = diff(Chr[r, i, j], coords[s]) - diff(Chr[r, j, i], coords[s]) + sum(Chr[r, s, k] * Chr[k, i, j] - Chr[r, s, j] * Chr[k, i, j] for k in range(3))

# results
print("Christoffel symbols:")
print(Chr)

print("\nRiemann tensor:")
print(Riemann)




