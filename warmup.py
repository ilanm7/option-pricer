import numpy as np


def moyenne(valeurs):
    total = 0
    for v in valeurs:
        total = total + v
    return total / len(valeurs)


def simule(n):
    tirages = np.random.standard_normal(n)
    return tirages.mean(), tirages.std()


print(moyenne([1, 2, 3]))  # attendu : 2.0
print(simule(1_000_000))   # attendu : proche de (0, 1)