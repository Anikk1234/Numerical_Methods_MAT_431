import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, lagrange, CubicSpline

def get_user_input():
    print("--- User Input Section ---")
    try:
        n = int(input("Enter the number of data points: "))
        if n < 2:
            print("Error.............")
            return None, None

        x_points = []
        y_points = []

        print(f"Enter {n} pairs of (x, y) coordinates:")
        for i in range(n):
            val = input(f"Point {i + 1} (format 'x y'): ").split()
            if len(val) < 2:
                x = float(val[0])
                y = float(input(f"  Enter y for x={x}: "))
            else:
                x = float(val[0])
                y = float(val[1])

            x_points.append(x)
            y_points.append(y)

        sorted_pairs = sorted(zip(x_points, y_points))
        x_points, y_points = zip(*sorted_pairs)
        return np.array(x_points), np.array(y_points)

    except ValueError:
        print("Invalid input. ")
        return None, None

def main():
    x, y = get_user_input()

    if x is None:
        return
    x_new = np.linspace(min(x), max(x), 100)

    f_linear = interp1d(x, y, kind='linear')
    y_linear = f_linear(x_new)

    f_spline = CubicSpline(x, y)
    y_spline = f_spline(x_new)

    poly_lagrange = lagrange(x, y)
    y_lagrange = poly_lagrange(x_new)

    f_nearest = interp1d(x, y, kind='nearest')
    y_nearest = f_nearest(x_new)

    plt.figure(figsize=(10, 6))

    plt.scatter(x, y, color='red', s=100, label='Data Points', zorder=5)

    plt.plot(x_new, y_linear, '--', label='Linear', linewidth=2, alpha=0.7)
    plt.plot(x_new, y_spline, '-', label='Cubic Spline', linewidth=2)
    plt.plot(x_new, y_lagrange, ':', label='Lagrange Polynomial', linewidth=2)
    plt.plot(x_new, y_nearest, '-.', label='Nearest Neighbor', alpha=0.5)

    plt.title(f"Comparison of Interpolation Methods (N={len(x)})")
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    print("Plot generated. Please check the popup window.")
    plt.show()

if __name__ == "__main__":
    main()
#------------------------------------------------------
#Random number generation:

# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.interpolate import interp1d, lagrange, CubicSpline

# def generate_random_data(n=8):
#     print(f"--- Generating {n} Random Points ---")
#     x = np.random.choice(range(20), size=n, replace=False)
#     x.sort()
#     y = np.random.randint(-10, 11, size=n)
#     print("X Points:", x)
#     print("Y Points:", y)
#
#     return x, y

# def main():
#     x, y = generate_random_data(n=8)
#
#     x_new = np.linspace(min(x), max(x), 100)
#
#     f_linear = interp1d(x, y, kind='linear')
#     y_linear = f_linear(x_new)
#
#     f_spline = CubicSpline(x, y)
#     y_spline = f_spline(x_new)
#
#     poly_lagrange = lagrange(x, y)
#     y_lagrange = poly_lagrange(x_new)
#
#     f_nearest = interp1d(x, y, kind='nearest')
#     y_nearest = f_nearest(x_new)
#
#     plt.figure(figsize=(10, 6))
#
#     plt.scatter(x, y, color='red', s=100, label='Random Points', zorder=5)
#
#     plt.plot(x_new, y_linear, '--', label='Linear', linewidth=2, alpha=0.7)
#     plt.plot(x_new, y_spline, '-', label='Cubic Spline', linewidth=2)
#     plt.plot(x_new, y_lagrange, ':', label='Lagrange Polynomial', linewidth=2)
#     plt.plot(x_new, y_nearest, '-.', label='Nearest Neighbor', alpha=0.4)
#
#     plt.title(f"Interpolation of {len(x)} Random Points")
#     plt.xlabel('X Axis')
#     plt.ylabel('Y Axis')
#     plt.legend()
#     plt.grid(True)
#
#     plt.tight_layout()
#     print("Plot generated. ")
#     plt.show()
#
# if __name__ == "__main__":
#     main()