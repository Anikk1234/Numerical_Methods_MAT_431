import numpy as np
import math

def bisection(f,a,b,tol=1e-4):
    iters=0
    while (b-a)/2 > tol:
        iters +=1
        mid=(a+b)/2
        if f(a)*f(mid)<0:
            b=mid
        else:
            a=mid
    return (a+b)/2,iters

def trisection(f,a,b,tol=1e-4,mode='balanced'):
    iters=0
    while(b-a)>tol:
        iters+=1
        if mode == 'balanced':
            m1=a+(b-a)/3
            m2=a+2*(b-a)/3
        else:
            r1,r2=sorted([np.random.uniform(a,b),np.random.uniform(a,b)])
            m1,m2=r1,r2
        if f(a)*f(m1)<=0:
            b=m1
        elif f(m1)*f(m2)<=0:
            a,b=m1,m2
        else:
            a=m1
            a=m2
    return (a+b)/2,iters

f1= lambda x: x*(np.sin(x)**2)-np.exp(x)+5
f2= lambda x:(x**2)*np.cos(x)-x**3+5

tests = [
    {"name": "f1: x*sin^2(x) - e^x + 5", "func": f1, "bracket": [-2, 3]},
    {"name": "f2: x^2*cos(x) - x^3 + 5", "func": f2, "bracket": [-1, 3]}
]

for test in tests:
    print(f"\n--- Testing {test['name']} ---")
    root_bis, it_bis = bisection(test['func'], *test['bracket'])
    root_tri, it_tri = trisection(test['func'], *test['bracket'], mode='balanced')

    print(f"Vanilla Bisection: Root ~ {root_bis:.4f} ({it_bis} iterations)")
    print(f"Balanced Trisection: Root ~ {root_tri:.4f} ({it_tri} iterations)")


#Fixed Point Itteration:

def fixed_point(g,x0,tol=1e-4,max_iter=100):
    for i in range(max_iter):
        x_next=g(x0)
        if abs(x_next-x0)<tol:
            return x_next,i
        x0=x_next
    return x0,max_iter

g2=lambda x:(x**2*np.cos(x)+5)**(1/3)
root_fp,it_fp=fixed_point(g2,1.5)
print(f"\nFixed-Point Iteration (f2): Root ~ {root_fp:.4f} ({it_fp} iterations)")