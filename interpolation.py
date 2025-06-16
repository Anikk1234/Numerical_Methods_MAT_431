from scipy.interpolate import interp1d
import numpy as np

xs = np.arange(10)
ys = 2 * xs + 1
interp_func = interp1d(xs, ys)
sharad = interp_func(np.arange(2.1, 3, 0.1))
print(sharad)


# spline interpolation:
from scipy.interpolate import UnivariateSpline
import numpy as np
xs = np.arange(10)
ys = xs ** 2 + np.sin(xs) + 1
interp_func = UnivariateSpline(xs, ys)
sharad = interp_func(np.arange(2.1, 3, 0.1))
print(sharad)


# Interpolation with Radial basis Function(RBF)
from scipy.interpolate import Rbf
import numpy as np
xs = np.arange(10)
ys = xs ** 2 + np.sin(xs) + 1
interp_func = Rbf(xs, ys)
sharad = interp_func(np.arange(2.1, 3, 0.1))
print(sharad)

