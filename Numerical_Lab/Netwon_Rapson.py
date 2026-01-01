# import numpy as np
# from scipy import optimize
#
# def netwon_rapson():
#     def f(x):
#         return x**3-x-2
#     def df(x):
#         return 3*x**2-1
#     def without_library(func,deriv,x0,tolerance=1e-6,maxiter=100):
#         x=x0
#         for i in range(maxiter):
#             fx=func(x)
#             dfx=deriv(x)
#             if dfx==0:
#                 print("Derivative is zero. No solution found.")
#                 return None
#             x_new=x-(fx/dfx)
#             print(f"Iteration {i + 1}: x = {x_new:.6f}")
#
#             if abs(x_new)<tolerance:
#                 return x_new
#             x=x_new
#         return x
#     root_manual=without_library(f,df,x0=1.5)
#     print(f"manual_root: {root_manual:.6f}")
#
#     root_scipy=optimize.newton(f,1.5,fprime=df)
#     print(f"Scipy result:{root_scipy:.6f}")
#
#
# if __name__ == "__main__":
#     netwon_rapson()
#----------------------------------------------------------------------
import numpy as np
from scipy import optimize



a = np.random.randint(1, 10)
b = np.random.randint(-10, 10)
c = np.random.randint(-20, -1)  # Negative C ensures at least one real root usually

print(f"Random Equation: {a}x^2 + ({b})x + ({c}) = 0")


# Define functions dynamically
def rand_f(x):
    return a * x ** 2 + b * x + c


def rand_df(x):
    return 2 * a * x + b


try:
    # Solve using Library
    rand_root = optimize.newton(rand_f, x0=5, fprime=rand_df)
    print(f"Found Root: {rand_root:.6f}")
    print(f"Verification (f(root)): {rand_f(rand_root):.10f} (should be close to 0)")
except RuntimeError:
    print("Could not find a root (Equation might not have real roots).")