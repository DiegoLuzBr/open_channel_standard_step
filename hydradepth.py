"""
================= NORMAL DEPTH AND CRITICAL DEPTH ==================

Variables
g - standard gravity
b - bottom width
ZL - left side slope
ZR - right side slope
slope - longitudinal slope
n - Manning's roughness coefficients

====================================================================
                @Authors: Beatriz, Diego, Edwin, Luiz
                            FEC - Unicamp
====================================================================

"""
import sympy as sp
from scipy import optimize


# Normal Depth

norm = sp.symbols('norm')


def fy(norm, args0):
    n, Q, slope, b, ZL, ZR = args0
    geo = (n*Q)/((slope)**(1/2))
    area = norm*(b + 0.5*norm*(ZL+ZR))
    perimetro = b + (norm**2.0 + norm*ZL*norm*ZL)**0.5 + (norm**2.0 + norm*ZR*norm*ZR)**0.5
    raio = area / perimetro
    return geo - (area*raio**(2.0/3.0))


def dfdy(norm, args0):
    return sp.diff(fy(norm, args0), norm)


def normal(init_guess, args0):
    """ Make a initial guess to determine the normal depth"""
    f = sp.lambdify([norm], fy(norm, args0))  # tranforma as funções simbolicas em funcoes plenas do python
    df = sp.lambdify([norm], dfdy(norm, args0))
    normal = optimize.newton(f, init_guess, fprime=df)
    return normal


# Critical Depth

crit = sp.symbols('crit')



def alt_critical(crit, args):
    b, ZL, ZR, g, Q = args
    B = (b + ZL*crit + ZR*crit)
    area = (crit*(b + 0.5*crit*(ZL+ZR)))
    return ((Q**2)*B)/(g*area**3) - 1


def alt_criticalP(crit, args):
    return sp.diff(alt_critical(crit, args), crit)


def critical(init_guess, args):
    """ Make a initial guess to determine the critical depth"""
    f = sp.lambdify([crit], alt_critical(crit, args))  # tranforma as funções simbolicas em funcoes plenas do python
    df = sp.lambdify([crit], alt_criticalP(crit, args))
    critical = optimize.newton(f, init_guess, fprime=df)
    return critical
