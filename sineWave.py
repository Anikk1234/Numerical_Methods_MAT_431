import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize


def objective_function(x):
    return np.sin(x)


# Plotting the function
x_values = np.linspace(-10, 10, 400)
y_values = objective_function(x_values)

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='Objective Function: sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Objective Function Plot: sin(x)')
plt.grid(True)
plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)

# Mark the local minima points
minima_x = np.array([-3 * np.pi / 2, -np.pi / 2, np.pi / 2, 3 * np.pi / 2])
minima_y = objective_function(minima_x)
plt.scatter(minima_x, minima_y, color='red', s=50, zorder=3, label='Local Minima')

# Optimization with different initial guesses
initial_guesses = [0, 2, 4]
colors = ['green', 'blue', 'purple']

# Iterate over initial_guesses and perform minimization for each
results = []
for i, guess in enumerate(initial_guesses):
    result = minimize(objective_function, guess)
    results.append(result)

    # Mark the initial guesses and results on the plot
    plt.scatter([guess], [objective_function(guess)], color=colors[i], marker='o', s=100,
                label=f'Initial Guess: {guess}', zorder=4)
    plt.scatter([result.x[0]], [result.fun], color=colors[i], marker='x', s=100,
                label=f'Result from {guess}: {result.x[0]:.2f}', zorder=5)

    # Draw an arrow from initial guess to result
    plt.annotate('', xy=(result.x[0], result.fun), xytext=(guess, objective_function(guess)),
                 arrowprops=dict(arrowstyle='->', lw=1.5, color=colors[i]))

plt.legend(loc='upper right', bbox_to_anchor=(1.25, 1))
plt.tight_layout()
plt.show()

# Print results in a table format
print("\nOptimization Results:\n")
print(f"{'Initial Guess':<15} {'Optimal x':<15} {'Function Value':<15} {'Success':<10} {'Iterations':<10}")
print("-" * 65)

for i, result in enumerate(results):
    print(f"{initial_guesses[i]:<15.2f} {result.x[0]:<15.6f} {result.fun:<15.6f} {result.success:<10} {result.nit:<10}")

# Analytical explanation
print("\nAnalytical Explanation:")
print(
    "The sine function has multiple local minima at x = -3π/2, -π/2, π/2, 3π/2, ... (or generally at x = (2n+1)π/2 where n is an integer)")
print("Each local minimum has a value of sin(x) = -1")
print("The initial guess determines which local minimum the algorithm converges to:")
for i, guess in enumerate(initial_guesses):
    nearest_min = results[i].x[0]
    print(
        f"- Starting from x = {guess}, the algorithm converges to the minimum near x ≈ {nearest_min:.4f}, which is close to {nearest_min / np.pi:.4f}π")