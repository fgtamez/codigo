# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 07:12:00 2022

@author: kiko
"""

import sympy

eq = '(-b-sqrt(b**2-4*a*c))/(2*a)'

o = sympy.latex(sympy.simplify(eq))

print(o)