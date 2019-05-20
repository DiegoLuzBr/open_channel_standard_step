# Open-Channel Flow Algorithm in Newton-Raphson Form in Python 3.x  


### Objective

This work is an adaption of the Paper ***"Open-Channel Flow Algorithm in Newton-Rapshon Form"*** by John N. Paine - *see more details in: [Journal of Irrigation and Drainage Engineering, Vol. 118, Issue 2 - March 1992](https://doi.org/10.1061/(ASCE)0733-9437(1992)118:2(306))*.  


The algorithm also involves a solution of a differential equation, because that is necessary that users input the **boundary condition**. If the unknow conditions are at the downstream, the users need enter the hydraulic control at the upstream, otherwise if the unknow conditions are at the upstream, the users need enter de hydraulic control at the downstream.

Paine, said:
>*The three algorithm variables can be defined based on the direction of
standard step method computation. If computations are being performed
from known conditions downstream: BETA = 1; Cx = total energy head at the
downstream section; and C2 = friction slope at the downstream section; where Cx and C2 are computed using the depth at the downstream section. Otherwise, if computations are being performed from known conditions upstream: BETA = — 1; Cx = total energy head at the upstream section; and C2 = friction slope at the upstream section; where Ct and C2 are computed using the depth at the upstream section.*

### Warning

Some physical conditions implies **failure** in the Newton-Rapshon Method, like when the ***length of the flow profile may be shorter than the length of the channel***, in a ***hydraulic jump*** or in the case of ***flow regime change***.  
To correct this problem, a hydraulic verification was made in the module *hydradepth.py*
Besides that, if the users are working in ***U.S. unit*** or ***International System unit***, the method ***C3 need to be adjusted***.

### Inputs

> g - standard gravity  
bU -> bottom upstream  
bD -> bottom downstream  
ZL -> left side slope  
ZR -> right side slope  
slope -> longitudinal slope  
n -> Manning's roughness coefficients  
ns -> number of sections  
L -> length  
iDownstream -> invert downstream  
iUpstream -> invert upstream  
iKinicial -> inverts know  
yKi -> depth know  
BETA -> boundary conditions -> down to up = 1.0; up to down = - 1.0  
Q -> discharge  
___
Diego Luz
