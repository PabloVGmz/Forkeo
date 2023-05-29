import numpy as np

from .spatialDiscretization import *

class LF2:

    def __init__(self, sp: SpatialDiscretization, fields):
        self.sp = sp
        self.time = 0.0

    def step(self, fields, dt):
        E = fields['E']
        H = fields['H']
        
        H12 = H + 1/2*dt*self.sp.computeRHSH(fields)
        
        self.time += dt/2
        E += dt*self.sp.computeRHSE(fields)
        self.time += dt/2
        H = H12+dt*self.sp.computeRHSH(fields)
        
        