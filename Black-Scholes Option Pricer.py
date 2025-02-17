import numpy as np
import scipy.stats as si

# Defining the Black-Scholes price for a European option
def black_scholes(S, K, T, r, sigma, q, option_type = "call"):
    d1 = (np.log(S / K) + (r - q + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    if option_type == "call":
        price = S * np.exp(-q * T) * si.norm.cdf(d1) - K * np.exp(-r * T) * si.norm.cdf(d2)
    elif option_type == "put":
        price = K * np.exp(-r * T) * si.norm.cdf(-d2) - S * np.exp(-q * T) * si.norm.cdf(-d1)
    return price

# Example parameters
S = 100                 # Current stock price (€100)
K = 100                 # Strike price (€100)
T = 1                   # Time to maturity (1 year)
r = 0.05                # Risk-free rate (5%)
sigma = 0.2             # Volatility (20%)
q = 0                   # Dividend yield (0%)
option_type = "call"    # Type of option (call or put)

# Price calculation
bs_price = black_scholes(S, K, T, r, sigma, q, option_type)

# Display the result with 4 decimal places
print(f"Black-Scholes {option_type} option price: {bs_price:.4f}")