#!/usr/bin/python


""" Kido Douglas
This code utilizes Black-Scholes model to simulate stock optionc price maturity"""

import numpy as np
from numba import jit
import time

# Black-Scholes
S0 = 235.57   # Initial stock price: Change based on company
K = 220    # Strike price: Estimate based on previous results
T = 0.5    # Time to maturity for half a yr in the context of this model
r = 0.05   # Risk-free rate (annualized): changes depending on time
sigma = 0.2  # Volatility of the asset (annualized)

N = 1000000  # Total number of Monte Carlo simulations

@jit(nopython=True)
def simulate_price_path(S0, T, r, sigma):
    Z = np.random.normal(0, 1)
    return S0 * np.exp((r - 0.5 * sigma ** 2)*T+sigma*np.sqrt(T)*Z)

@jit(nopython=True)
def compute_option_payoff(S0, K, T, r, sigma, n_sim):
    payoffs = np.zeros(n_sim)  # Pre-allocate np array

    for i in range(n_sim):
        ST = simulate_price_path(S0, T, r, sigma)
        payoffs[i] = max(ST - K, 0)

    # Calculate average
    average_payoff = np.mean(payoffs)
    return average_payoff * np.exp(-r * T)

if __name__ == "__main__":
    start_time = time.time()



    option_price = compute_option_payoff(S0, K, T, r, sigma, N)

    # Print the results
    print(f"Option Price: {option_price:.4f}")
    print(f"Execution Time: {time.time() - start_time:.2f} seconds")
