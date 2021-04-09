#taller

import scipy.interpolate as sp
import numpy as np

x = np.array([0,1,2])

y = np.array([10.5,15.33,5.789])

dydx = np.array([1,(y[1]-y[0])/(x[1]-x[0]),(y[2]-y[1])/(x[2]-x[1])])

a = sp.CubicHermiteSpline(x,y,dydx)

polinomio = np.array([a.c[0,0],a.c[0,1],a.c[0,2],a.c[0,3]])



print (a.c)
