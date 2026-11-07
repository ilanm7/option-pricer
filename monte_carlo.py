import numpy as np

S, K, r, sigma, T = 100, 100, 0.05, 0.2, 1
n = 1_000_000

z = np.random.standard_normal(n)
ST = S * np.exp((r - sigma ** 2 / 2) * T + sigma * np.sqrt(T) * z)

gains = np.maximum(ST - K, 0)
prix = np.exp(-r * T) * gains.mean()

print(prix)  # attendu : environ 10.45