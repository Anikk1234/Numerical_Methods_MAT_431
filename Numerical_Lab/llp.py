import numpy as np
from scipy.optimize import linprog
#
# def linear_programming_demo():
#     print("Linear Programming (Simplex) Program:")
#
#
#     c = [-1, -2, 1]
#
#     # Constraints (Ax <= b)
#     A = [
#         [2, 1, 1],
#         [-4, -2, -3],
#         [2, 5, 5]
#     ]
#     b = [14, 28, 30]
#
#
#     res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None), method='highs')
#
#     if res.success:
#         print("Status:", res.message)
#         print(f"Optimal values: x = {res.x[0]:.2f}, y = {res.x[1]:.2f}, z = {res.x[2]:.2f}")
#         print(f"Maximum Z = {-res.fun:.2f}")
#     else:
#         print("Optimization failed:", res.message)



n_vars = 3
n_constraints = 3

c_random = np.random.randint(-10, 11, n_vars)

A_random = np.random.randint(-10, 11, (n_constraints, n_vars))

b_random = np.random.randint(1, 51, n_constraints)

print(f"Random Objective Coefficients (c): {c_random}")
print(f"Random Constraints (A):\n{A_random}")
print(f"Random Limits (b): {b_random}")

res_rand= linprog(c_random, A_ub=A_random, b_ub=b_random, bounds=(0, None), method='highs')

print("Result for Random Problem:")
print("Status:", res_rand.message)

if res_rand.success:
    solution_str = ", ".join([f"x{i + 1}={val:.2f}" for i, val in enumerate(res_rand.x)])
    print(f"Optimal values: {solution_str}")
    print(f"Optimal Objective Value (Minimization) = {res_rand.fun:.2f}")
else:
    print("Could not find optimal solution (Random problems often have no solution or are infinite).")

if __name__ == "__main__":
  linear_programming_demo()