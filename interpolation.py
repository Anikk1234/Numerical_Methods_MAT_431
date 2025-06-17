#linear_interpolation
import numpy as np
import matplotlib.pyplot as plt

# Known data points
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 1, 4, 9, 16])

# Interpolated values
x_interp = np.linspace(0, 4, 100)
y_interp = np.interp(x_interp, x, y)

plt.plot(x, y, 'o', label='Data points')
plt.plot(x_interp, y_interp, label='Linear Interpolation')
plt.legend()
plt.title('Linear Interpolation')
plt.show()

#polynomial_interpolation
import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1, 2, 3, 4])
y = np.array([1, 2, 0, 2, 1])

# Fit a 4th degree polynomial
coeffs = np.polyfit(x, y, 4)
p = np.poly1d(coeffs)

x_interp = np.linspace(0, 4, 100)
y_interp = p(x_interp)

plt.plot(x, y, 'o', label='Data points')
plt.plot(x_interp, y_interp, label='Polynomial Interpolation')
plt.legend()
plt.title('Polynomial Interpolation')
plt.show()

#cubic_spline_interpolation
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

x = np.array([0, 1, 2, 3, 4])
y = np.array([1, 2, 0, 2, 1])

cs = CubicSpline(x, y)
x_interp = np.linspace(0, 4, 100)
y_interp = cs(x_interp)

plt.plot(x, y, 'o', label='Data points')
plt.plot(x_interp, y_interp, label='Cubic Spline Interpolation')
plt.legend()
plt.title('Cubic Spline Interpolation')
plt.show()


#nearest_neighbor_interpolation
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

x = np.array([0, 1, 2, 3, 4])
y = np.array([1, 2, 0, 2, 1])

f = interp1d(x, y, kind='nearest')
x_interp = np.linspace(0, 4, 100)
y_interp = f(x_interp)

plt.plot(x, y, 'o', label='Data points')
plt.step(x_interp, y_interp, label='Nearest Neighbor', where='mid')
plt.legend()
plt.title('Nearest Neighbor Interpolation')
plt.show()