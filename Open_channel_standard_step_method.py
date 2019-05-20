"""
======================= Standard Step Method =======================

Variables
g - standard gravity -> 32.2 ft/s^2; 9.81 m/s^2
bU - bottom upstream
bD - bottom downstream
ZL - left side slope
ZR - right side slope
slope - longitudinal slope
n - Manning's roughness coefficients
ns - number of sections
L - length
iDownstream - invert downstream
iUpstream - invert upstream
iKinicial - inverts know
yKi - depth know
BETA - boundary conditions -> down to up = 1.0; up to down = - 1.0
Q - discharge
====================================================================
                @Authors: Beatriz, Diego, Edwin, Luiz
                            FEC - Unicamp
====================================================================

"""

# indices K -> conhecido
#         U -> desconhecido

from scipy import optimize
import matplotlib.pyplot as plt
import hydradepth as dp


def fy(y):
    Sfy = Sf(y)
    C1 = H(iK, yK)
    C2 = SfK(Q, n)
    C4 = inclina(ZL, ZR)
    return BETA*C1 - BETA*y - BETA*i - BETA/(2.0*g)*(Q/(y*(b+C4*y)))**2.0 + (deltax/2.0)*(Sfy + C2)


def derivada_fy(y):
    derivda_Sfy = SfP(y)
    C4 = inclina(ZL, ZR)
    return BETA*(-1.0) + BETA*(Q*Q/g) * (y*(b + C4*y))**(-3.0) * (b + 2*C4*y) + (deltax/2.0)*(derivda_Sfy)


def Sf(y):
    C3 = mann(Q, n)
    C4 = inclina(ZL, ZR)
    C5 = raiz_inclina(ZL, ZR)

    return (C3**2) * ((b*y + (C4*y**2.0))**(-10.0/3.0)) * (b + y*C5)**(4.0/3.0)


def SfP(y):
    C3 = mann(Q, n)
    C4 = inclina(ZL, ZR)
    C5 = raiz_inclina(ZL, ZR)
    return (4.0/3.0)*C3*C3*C5 * ((b*y + C4*y*y)**(-10.0/3.0)) * (b + C5*y)**(1.0/3.0) - (10.0/3.0)*(C3*C3) * (b + 2*C4*y) * (b + C5*y)**(4.0/3.0) * (y*(b + C4*y))**(-13.0/3.0)


def H(iK, yK):  # C1
    C4 = inclina(ZL, ZR)
    VK = Q/(yK*(b + C4*yK))

    return iK + yK + (VK**2.0)/(2*g)


def SfK(Q, n):  # C2
    A = yK*(b + 0.5*yK*(ZL+ZR))
    P = b + (yK**2.0 + yK*ZL*yK*ZL)**0.5 + (yK**2.0 + yK*ZR*yK*ZR)**0.5
    R = A/P
    return (Q*n / (1.486*A*R**(2.0/3.0)))**2.0


def mann(Q, n):  # C3
    return Q*n/1.486  # ft - 1.496; m - 1.000


def inclina(ZL, ZR):  # C4
    return (ZL + ZR) / 2.0


def raiz_inclina(ZL, ZR):  # C5
    return (1+(ZL)**2.0)**0.5 + (1+(ZR)**2.0)**0.5


# channel features
ZL = 2.0
ZR = 1.0
bU = 5.0
bD = 5.0
b = abs((bU + bD)/2)
n = 0.015  # manning's coefficient
L = 25.0
Initial_Station = 50
iDownstream = 35.21
iUpstream = 37.22
slope = (iUpstream - iDownstream) / L

# project features
Q = 285
g = 32.2  # ft/s^2
ns = 20  # number of sections - need to be integer
deltax = L/(ns-1)

# boundary condition
iKinicial = 35.21  # inverts know
BETA = 1  # down to up = 1.0; up to down = - 1.0
yKi = 2.15  # y know


# hydraulic verification
args = [b, ZL, ZR, g, Q]
yc = dp.critical(yKi, args)

args0 = [n, Q, slope, b, ZL, ZR]
yn = dp.normal(yKi, args0)


# create the inverts unknown
iU = ns * [iKinicial]

for x in range(1, ns):  # start in second '[1]' to keep the value of know invert in first section
    iU[x] = deltax * slope + iU[x-1]

# create the stations
station = (ns) * [Initial_Station]
for x in range(0, ns):
    station[x] = Initial_Station + deltax*x

# create the y unknow
y = (ns) * [yKi]

for x in range(1, ns):
    yK = y[x-1]
    iK = iU[x-1]
    i = iU[x]

    try:
        y[x] = optimize.newton(fy, y[x-1]+0.01, fprime=derivada_fy)
    except RuntimeError or ZeroDivisionError:
        y[x] = yc
        del y[x+1:]
        del station[x+1:]
        del iU[x+1:]
        break

# stage depth (invert + depth)
stagedepth = (len(y)) * [Initial_Station]
for x in range(len(y)):
    stagedepth[x] = iU[x] + y[x]

# critical depth for print
ycrit = (len(y)) * [yc]
for x in range(len(y)):
    ycrit[x] = iU[x] + yc

# normal depth for print
ynorm = (len(y)) * [yn]
for x in range(len(y)):
    ynorm[x] = iU[x] + yn

print("="*36)
print("--- STANDARD STEP METHOD RESULTS ---")
print("="*36)
print('NORMAL DEPTH = ' f'{yn:2.2f}' ' ft')
print('CRITICAL DEPTH = ' f'{yc:2.2f}'' ft')
print("-"*36)
print("STATION       STAGE       FLOW DEPTH")
print("              (ft)           (ft)")
print("-"*36)

for x in range(len(y)):
    print(f' {station[x]:2.2f}        {stagedepth[x]:2.2f}          {y[x]:2.2f}')
print("-"*36)

# printing graphic
with plt.style.context('Solarize_Light2'):
    plt.plot(station, iU, 'k', label='Invert')
    plt.plot(station, stagedepth, 'b--', label='Flow Depth')
    plt.plot(station, ycrit, 'r:', label='Critical Depth')
    plt.plot(station, ynorm, 'g-.', label='Normal Depth')

    legend = plt.legend(loc='best', shadow=True, fontsize='small')

    legend.get_frame().set_facecolor('#AAAC7B')
    plt.xlabel('STATION')
    plt.ylabel('DEPTH')
    plt.title('STANDARD STEP')
    plt.show()
