import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# 1. Series expansion using SymPy
z_sym = sp.symbols('z')
f_sym = z_sym**2 * sp.log(1 + z_sym)
expansion = sp.series(f_sym, z_sym, 0, 9)
print("SymPy Series Expansion:")
sp.pprint(expansion)

# 2. Setup data for plotting
z = np.linspace(-0.5, 1.0, 400)
f_actual = z**2 * np.log(1 + z)

# Approximations
term1 = z**2 - (z**3)/2 + (z**4)/3 - (z**5)/4
term2 = term1 + (z**6)/5 - (z**7)/6

# 3. Plotting with Raw Strings (r"") to avoid SyntaxWarnings
plt.figure(figsize=(10, 6))
plt.plot(z, f_actual, 'k-', linewidth=3, label=r'Actual: $z^2 \log(1+z)$')
plt.plot(z, term1, 'r--', linewidth=1.5, label='First 4 Terms')
plt.plot(z, term2, 'b:', linewidth=2, label='First 6 Terms')

plt.title(r"Taylor Series Approximation of $z^2 \log(1+z)$")
plt.xlabel("z")
plt.ylabel("f(z)")
plt.legend()
plt.grid(True)
plt.show()