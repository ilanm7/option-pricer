from math import exp
from pricer import bs_call, bs_put

S, K, r, sigma, T = 100, 100, 0.05, 0.2, 1

call = bs_call(S, K, r, sigma, T)
put = bs_put(S, K, r, sigma, T)

assert abs(call - 10.4506) < 0.0001
assert abs(put - 5.5735) < 0.0001
assert abs((call - put) - (S - K * exp(-r * T))) < 0.0001

print("Tests OK")