from scipy.optimize import linprog

c=[-1,-2,1]
A=[
    [2,1,1],
    [-4,-2,-3],
    [2,5,5]
]
b=[14,28,30]

x_bounds=(0,None)
y_bounds=(0,None)
z_bounds=(0,None)

res=linprog(c,A_ub=A,b_ub=b,bounds=[x_bounds,y_bounds,z_bounds],method='highs')

print("Status:",res.message)
print(f"Optimal values: x = {res.x[0]:.2f}, y = {res.x[1]:.2f}, z = {res.x[2]:.2f}")
print(f"Maximum Z = {-res.fun:.2f}")