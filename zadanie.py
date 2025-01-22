import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
import seaborn as sns


n = int(input("daj n "))
h = 2 / n


def e(i, x):
    if x >= h * (i - 1) and x <= h * i:
        return (x - h * (i - 1)) / h * i
    elif x >= h * i and x <= h * (i + 1):
        return (h * (i + 1) - x) / h * i
    else:
        return 0


def e_prim(i, x):
    if x >= h * (i - 1) and x <= h * i:
        return 1 / h
    elif x >= h * i and x <= h * (i + 1):
        return -1 / h
    else:
        return 0


def L(v):
    return quad(lambda x: 100 * (x**2) * e(v, x), 0, 2)[0] - 40 * e(v, 0)


def k(x):
    if x >= 0 and x <= 1:
        return 1
    elif x > 1 and x <= 2:
        return 2 * x


def B(u, v):
    return quad(lambda x: k(x) * e_prim(u, x) * e_prim(v, x), 0, 2)[0] - e(u, 0) * e(
        v, 0
    )


def u(W, x):
    sum_val = -20
    for i in range(n):
        sum_val += W[i] * e(i, x)
    return sum_val


A = [[0 for _ in range(n)] for _ in range(n)]

for i in range(len(A)):
    for j in range(len(A[i])):
        A[i][j] = B(i, j)

V = [0 for _ in range(n)]

for i in range(len(V)):
    V[i] = L(i)

W = np.linalg.solve(A, V)

x_vals = np.linspace(0, 2, 1000)
y_vals = []
for x in x_vals:
    y_vals.append(u(W, x))

print(y_vals)

sns.set_style(style="darkgrid")
sns.lineplot(x=x_vals, y=y_vals, label="u(W, x)")
plt.xlim(0, 2)
plt.xlabel("x")
plt.ylabel("u(W, x)")
plt.title("Plot of u(W, x)")
plt.legend()
plt.show()
