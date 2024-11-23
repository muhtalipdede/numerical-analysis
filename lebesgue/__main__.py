import numpy as np
import matplotlib.pyplot as plt

# Define interpolation points (equispaced or Chebyshev)
n = 10
a, b = -1, 1  # Interval
equispaced_points = np.linspace(a, b, n+1)
chebyshev_points = np.cos(np.pi * (2*np.arange(n+1) + 1) / (2*(n+1)))

# Define Lagrange basis functions
def lagrange_basis(x, i, points):
    numerator = np.prod([x - points[j] for j in range(len(points)) if j != i], axis=0)
    denominator = np.prod([points[i] - points[j] for j in range(len(points)) if j != i])
    return numerator / denominator

# Compute Lebesgue function
def lebesgue_function(x, points):
    return sum(np.abs(lagrange_basis(x, i, points)) for i in range(len(points)))

# Plot Lebesgue function for equispaced and Chebyshev points
x_vals = np.linspace(a, b, 1000)
lebesgue_equispaced = [lebesgue_function(x, equispaced_points) for x in x_vals]
lebesgue_chebyshev = [lebesgue_function(x, chebyshev_points) for x in x_vals]

plt.figure(figsize=(10, 6))
plt.plot(x_vals, lebesgue_equispaced, label="Equispaced Points", color="red")
plt.plot(x_vals, lebesgue_chebyshev, label="Chebyshev Points", color="blue")
plt.title("Lebesgue Function for Different Interpolation Points")
plt.xlabel("x")
plt.ylabel("Lebesgue Function Value")
plt.legend()
plt.grid()
plt.show()

# Lebesgue constants
lebesgue_constant_equispaced = max(lebesgue_equispaced)
lebesgue_constant_chebyshev = max(lebesgue_chebyshev)
print("Lebesgue Constant (Equispaced):", lebesgue_constant_equispaced)
print("Lebesgue Constant (Chebyshev):", lebesgue_constant_chebyshev)
