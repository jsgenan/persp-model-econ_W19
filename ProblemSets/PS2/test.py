from sympy import *
import numpy as np
import math
from matplotlib import pyplot as plt

#Each function should accept a function handle f, an array of points x, and a float h; 
#Each should return an array of the difference quotients evaluated at each point in x.
x, h  = symbols('x h')
f = (sin(x) + 1)**(sin(cos(x)))
#forward = (f.subs(x, x+h) - f)/h
forward = (-(sin(x) + 1)**sin(cos(x)) + (sin(h + x) + 1)**sin(cos(h + x)))/h
forward_center = -3*f + 4*f.subs(x, x+h) - f.subs(x, x+2*h)
x_plt = np.linspace(-math.pi, math.pi, 100)
h_plt = np.full_like(x, 0.0001)
result = lambdify(Matrix([[x_plt, h_plt]]), forward, 'numpy')