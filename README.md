# 💹 Option Price Simulation using Monte Carlo Methods

A high-performance simulation of stock option pricing using the **Black-Scholes model** and **Monte Carlo techniques**, optimized with Numba for fast execution. This project was developed for **COMP-360: High Performance Computing** and is designed to run efficiently on the **Wesleyan University High Performance Computing Cluster** using a Bash job script.

🗓️ **Completed**: Fall 2024  
📚 **Course**: COMP-360  
📁 **Language**: Python + Bash (SLURM scheduler)  
⚙️ **Speed**: Simulates 1,000,000+ price paths in seconds using Numba JIT

---

## 🌟 Highlights

- **Black-Scholes Option Pricing** – Implements the theoretical model with Monte Carlo simulation.
- **Numba Optimization** – Uses `@jit(nopython=True)` to compile Python to fast machine code.
- **1 Million Simulations** – Executes massive simulations in under 10 seconds on the HPC cluster.
- **Fully Vectorized Payoff Calculation** – Efficient use of NumPy arrays for performance.
- **Cluster Integration** – Includes a fully configured SLURM Bash script to run on GPU partitions.

---

## 📖 Overview

This project models the price of a European call option using a stochastic simulation based on the Black-Scholes framework. The simulation approximates the expected option payoff by generating a large number of random stock price paths at maturity.

### Black-Scholes Formula

- **S₀**: Initial stock price
- **K**: Strike price
- **T**: Time to maturity
- **r**: Risk-free rate
- **σ**: Volatility

The code simulates a final stock price `S_T` using the formula:

```math
S_T = S₀ * exp((r - 0.5 * σ²) * T + σ * sqrt(T) * Z)
