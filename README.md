# Numerical Methods Course

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![NumPy](https://img.shields.io/badge/NumPy-Latest-green)
![SciPy](https://img.shields.io/badge/SciPy-Latest-green)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Latest-orange)

## Course Overview

This repository contains implementations and examples of numerical methods using Python. The course covers fundamental numerical algorithms and their practical applications in engineering and scientific computing.

## Table of Contents

1. [Installation](#installation)
2. [Topics Covered](#topics-covered)
3. [Project Structure](#project-structure)
4. [Usage Examples](#usage-examples)
5. [Contributing](#contributing)
6. [License](#license)

## Installation

```bash
# Clone the repository
git clone https://github.com/Anikk1234/Numerical_Methods_MAT_431.git

# Navigate to the project directory
cd numerical

# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
# For Windows:
.venv\Scripts\activate
# For Unix/macOS:
source .venv/bin/activate

# Install required packages
pip install numpy scipy matplotlib
```

## Topics Covered

### 1. Root Finding Methods
- Bisection Method
- Newton-Raphson Method
- Secant Method
- Fixed-Point Iteration

### 2. Linear Algebra
- Gaussian Elimination
- LU Decomposition
- Matrix Operations
- Eigenvalue Problems

### 3. Interpolation
- Linear Interpolation
- Lagrange Polynomials
- Cubic Splines
- Bezier Curves

### 4. Numerical Integration
- Trapezoidal Rule
- Simpson's Rule
- Gaussian Quadrature

### 5. Differential Equations
- Euler's Method
- Runge-Kutta Methods
- Boundary Value Problems

### 6. Optimization
- Golden Section Search
- Gradient Descent
- Newton's Method for Optimization


## Usage Examples

### Root Finding Example
```python
import numpy as np
from scipy.optimize import fsolve

def find_root(f, x0):
    """
    Find root of function f starting from initial guess x0
    """
    return fsolve(f, x0)[0]

# Example: Find root of f(x) = x^2 - 4
f = lambda x: x**2 - 4
root = find_root(f, 1.0)
print(f"Root: {root}")  # Output: Root: 2.0
```

### Cylinder Volume Calculation
```python
def cylinder_volume(R, L):
    """
    Calculate volume of a cylinder
    R: radius
    L: length
    """
    return np.pi * R**2 * L

# Example usage
R, L = 1.0, 3.0
volume = cylinder_volume(R, L)
print(f"Cylinder Volume: {volume:.2f} cubic units")
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Course Instructor: [Instructor Name]
- Department of [Department Name]
- [University Name]

## Contact

Anikk1234 - [Your Email]

Last Updated: 2025-05-28 19:09:55 UTC
