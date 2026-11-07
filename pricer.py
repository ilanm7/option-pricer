from math import log, sqrt, exp
from scipy.stats import norm


def bs_call(S, K, r, sigma, T):
    d1 = (log(S / K) + (r + sigma ** 2 / 2) * T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)
    return S * norm.cdf(d1) - K * exp(-r * T) * norm.cdf(d2)


def bs_put(S, K, r, sigma, T):
    d1 = (log(S / K) + (r + sigma ** 2 / 2) * T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)
    return K * exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)


print(bs_call(100, 100, 0.05, 0.2, 1))  # attendu : 10.4506
print(bs_put(100, 100, 0.05, 0.2, 1))   # attendu : 5.5735