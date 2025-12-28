import numpy as np

A=np.random.rand(6,4)
b=np.random.rand(6)

x,residue,rank,s=np.linalg.lstsq(A,b,rcond=None)

residual_norm = np.sqrt(residue[0]) if residue.size > 0 else np.linalg.norm(b - A @ x)

print(f"Solution x: {x}")
print(f"Error(Residue): {residual_norm}")


